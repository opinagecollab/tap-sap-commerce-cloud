#!/usr/bin/env python3
import os
import json
import singer

from singer import utils, metadata
from tap_occ_products.client.occ_client import OccClient
from tap_occ_products.record.record import Record
from tap_occ_products.record.factory import build_record_handler


REQUIRED_CONFIG_KEYS = ['scheme', 'base_url', 'base_path', 'base_site']

LOGGER = singer.get_logger()
LOGGER.setLevel(level='DEBUG')


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schemas():
    LOGGER.debug('Loading schema files')
    schemas = {}

    for filename in os.listdir(get_abs_path('schemas')):
        path = get_abs_path('schemas') + '/' + filename
        file_raw = filename.replace('.json', '')
        with open(path) as file:
            schemas[file_raw] = json.load(file)

    return schemas


def discover():
    LOGGER.debug('Discovering available schemas')
    raw_schemas = load_schemas()
    streams = []

    for schema_name, schema in raw_schemas.items():
        stream_metadata = []
        stream_key_properties = []

        is_selected = \
            {
                'metadata': {
                    'selected': True
                },
                'breadcrumb': []
            }

        if schema_name == Record.CATEGORY.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        if schema_name == Record.CLASSIFICATION.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        if schema_name == Record.FEATURE.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        if schema_name == Record.FEATURE_UNIT.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('unitType')

        if schema_name == Record.PRICE.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        if schema_name == Record.PRODUCT.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        if schema_name == Record.PRODUCT_CATEGORY.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('productCode')
            stream_key_properties.append('categoryCode')

        if schema_name == Record.PRODUCT_FEATURE.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('productCode')
            stream_key_properties.append('featureCode')
            stream_key_properties.append('featureValue')

        if schema_name == Record.STOCK.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('code')

        catalog_entry = {
            'stream': schema_name,
            'tap_stream_id': schema_name,
            'schema': schema,
            'metadata': stream_metadata,
            'key_properties': stream_key_properties
        }
        streams.append(catalog_entry)

    return {
        'streams': streams
    }


def get_selected_streams(catalog):
    """
    Gets selected streams.  Checks schema's 'selected' first (legacy)
    and then checks metadata (current), looking for an empty breadcrumb
    and metadata with a 'selected' entry
    """
    selected_streams = []
    for stream in catalog['streams']:
        stream_metadata = metadata.to_map(stream['metadata'])
        # stream metadata will have an empty breadcrumb
        if metadata.get(stream_metadata, (), 'selected'):
            selected_streams.append(stream['tap_stream_id'])

    return selected_streams


def sync(config, state, catalog):
    LOGGER.info('Syncing selected streams')
    selected_stream_ids = get_selected_streams(catalog)

    for stream in catalog['streams']:
        stream_id = stream['tap_stream_id']
        stream_schema = stream['schema']
        stream_key_properties = stream['key_properties']
        if stream_id in selected_stream_ids:
            LOGGER.debug('Writing {} schema: \n {} \n and key properties: {}'.format(
                stream_id, stream_schema, stream_key_properties))
            singer.write_schema(stream_id, stream_schema, stream_key_properties)
        else:
            LOGGER.warn('Ignoring unselected stream: {}'.format(stream_id))

    LOGGER.info('Fetching OCC products')
    products = OccClient(config).fetch_products()

    for product in products:
        LOGGER.info('Syncing product with code: {}'.format(product['code']))

        price_record = build_record_handler(Record.PRICE).generate(product['price'])
        LOGGER.debug('Writing price record: {}'.format(price_record))
        singer.write_record(Record.PRICE.value, price_record)

        stock_record = build_record_handler(Record.STOCK).generate(product['stock'])
        LOGGER.debug('Writing stock record: {}'.format(stock_record))
        singer.write_record(Record.STOCK.value, stock_record)

        product_record = build_record_handler(Record.PRODUCT).generate(
            product, price_code=price_record['code'], stock_code=stock_record['code'])
        LOGGER.debug('Writing product record: {}'.format(product_record))
        singer.write_record(Record.PRODUCT.value, product_record)

        if 'categories' in product:
            for category in product['categories']:
                category_record = build_record_handler(Record.CATEGORY).generate(category)

                if category_record:
                    LOGGER.debug('Writing category record: {}'.format(category_record))
                    singer.write_record(Record.CATEGORY.value, category_record)
                    LOGGER.debug('Writing product category record: {}'.format({
                                'productCode': product['code'],
                                'categoryCode': category_record['code']
                            }))
                    singer.write_record(Record.PRODUCT_CATEGORY.value,
                                        build_record_handler(Record.PRODUCT_CATEGORY).generate({
                                            'productCode': product['code'],
                                            'categoryCode': category_record['code']
                                        }))

        if 'classifications' in product:
            for classification in product['classifications']:
                classification_record = build_record_handler(Record.CLASSIFICATION).generate(classification)

                if classification_record:
                    LOGGER.debug('Writing classification record: {}'.format(classification_record))
                    singer.write_record(Record.CLASSIFICATION.value, classification_record)

                for feature in classification['features']:
                    feature_unit_record = build_record_handler(Record.FEATURE_UNIT).generate(feature['featureUnit'])

                    if feature_unit_record:
                        LOGGER.debug('Writing feature unit record: {}'.format(feature_unit_record))
                        singer.write_record(Record.FEATURE_UNIT.value, feature_unit_record)

                    feature_record = build_record_handler(Record.FEATURE).generate(
                        feature,
                        unit_code=feature['featureUnit']['unitType'],
                        classification_code=classification['code'])

                    if feature_record:
                        LOGGER.debug('Writing feature record: {}'.format(feature_record))
                        singer.write_record(Record.FEATURE.value, feature_record)

                    for value in feature['featureValues']:
                        product_feature_record = build_record_handler(Record.PRODUCT_FEATURE).generate({
                            'productCode': product['code'],
                            'featureCode': feature['code'],
                            'featureValue': value['value']
                        })
                        LOGGER.debug('Writing product feature record: {}'.format(product_feature_record))
                        singer.write_record(Record.PRODUCT_FEATURE.value, product_feature_record)

    return


@utils.handle_top_exception(LOGGER)
def main():

    # Parse command line arguments
    args = utils.parse_args(REQUIRED_CONFIG_KEYS)

    # If discover flag was passed, run discovery mode and dump output to stdout
    if args.discover:
        catalog = discover()
        print(json.dumps(catalog, indent=2))
    # Otherwise run in sync mode
    else:
        if args.catalog:
            catalog = args.catalog
        else:
            catalog = discover()

        sync(args.config, args.state, catalog)


if __name__ == '__main__':
    main()
