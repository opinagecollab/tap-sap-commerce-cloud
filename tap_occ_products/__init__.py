#!/usr/bin/env python3
import os
import json
import singer

from datetime import datetime, timezone
from singer import utils, metadata
from tap_occ_products.client.occ_client import OccClient
from tap_occ_products.record.record import Record
from tap_occ_products.record.factory import build_record_handler


REQUIRED_CONFIG_KEYS = ['scheme', 'base_url', 'base_path', 'base_site']

LOGGER = singer.get_logger()
LOGGER.setLevel(level='DEBUG')

TENANT_ID = 't1'


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
            stream_key_properties.append('id')

        if schema_name == Record.CUSTOMER_SPECIFIC_PRICE.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('customerId')
            stream_key_properties.append('tenantId')
            stream_key_properties.append('sku')

        if schema_name == Record.PRICE_POINT.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('id')

        if schema_name == Record.PRODUCT.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('sku')
            stream_key_properties.append('tenantId')

        if schema_name == Record.PRODUCT_SPEC.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('tenantId')
            stream_key_properties.append('sku')
            stream_key_properties.append('specId')

        if schema_name == Record.SPEC.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('id')

        if schema_name == Record.STOCK_POINT.value:
            stream_metadata.append(is_selected)
            stream_key_properties.append('id')

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
        timestamp = datetime.now(timezone.utc).isoformat()

        price_point_record = \
            build_record_handler(Record.PRICE_POINT).generate(product, timestamp=timestamp, tenant_id=TENANT_ID)
        LOGGER.debug('Writing price_point record: {}'.format(price_point_record))
        singer.write_record(Record.PRICE_POINT.value, price_point_record)

        stock_point_record = \
            build_record_handler(Record.STOCK_POINT).generate(product, timestamp=timestamp, tenant_id=TENANT_ID)
        LOGGER.debug('Writing stock_point record: {}'.format(stock_point_record))
        singer.write_record(Record.STOCK_POINT.value, stock_point_record)

        category_id = None
        if 'categories' in product:
            category = product.get('categories')[0]
            category_record = build_record_handler(Record.CATEGORY).generate(category, tenant_id=TENANT_ID)

            # category record builder returns a record if the category hasn't been handled yet
            # otherwise, it returns the id of an already handled category record
            if isinstance(category_record, dict):
                category_id = category_record.get('id')

                LOGGER.debug('Writing category record: {}'.format(category_record))
                singer.write_record(Record.CATEGORY.value, category_record)
            else:
                category_id = category_record

        product_record = \
            build_record_handler(Record.PRODUCT).generate(product, tenant_id=TENANT_ID, category_id=category_id)
        LOGGER.debug('Writing product record: {}'.format(product_record))
        singer.write_record(Record.PRODUCT.value, product_record)

        if 'classifications' in product:
            for classification in product['classifications']:

                spec_id = None
                for feature in classification['features']:
                    # ignore specs without values
                    if not feature.get('featureValues'):
                        continue

                    # ignore specs with multiple values
                    if len(feature.get('featureValues')) > 1:
                        continue

                    spec_record = build_record_handler(Record.SPEC).generate(feature, tenant_id=TENANT_ID)

                    if isinstance(spec_record, dict):
                        spec_id = spec_id.get('id')

                        LOGGER.debug('Writing spec record: {}'.format(spec_record))
                        singer.write_record(Record.SPEC.value, spec_record)
                    else:
                        spec_id = spec_record

                    product_spec_record = \
                        build_record_handler(Record.PRODUCT_SPEC).generate(
                            feature, tenant_id=TENANT_ID, sku=product.get('code'), spec_id=spec_id)

                    LOGGER.debug('Writing product spec record: {}'.format(product_spec_record))
                    singer.write_record(Record.PRODUCT_FEATURE.value, product_spec_record)

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
