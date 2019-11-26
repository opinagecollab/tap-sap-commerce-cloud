#!/usr/bin/env python3
import os
import json
import singer

from singer import utils, metadata
from tap_occ_products.client.occ_client import OccClient

REQUIRED_CONFIG_KEYS = ['scheme', 'base_url', 'base_path', 'base_site']
LOGGER = singer.get_logger()
LOGGER.setLevel(level='INFO')


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


# Load schemas from schemas folder
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

        if schema_name == 'feature':
            stream_metadata.append({
                'metadata': {
                    'selected': True
                },
                'breadcrumb': []
            })

        catalog_entry = {
            'stream': schema_name,
            'tap_stream_id': schema_name,
            'schema': schema,
            'metadata': stream_metadata,
            'key_properties': stream_key_properties
        }
        streams.append(catalog_entry)

    return {'streams': streams}


def get_selected_streams(catalog):
    '''
    Gets selected streams.  Checks schema's 'selected' first (legacy)
    and then checks metadata (current), looking for an empty breadcrumb
    and mdata with a 'selected' entry
    '''
    selected_streams = []
    for stream in catalog['streams']:
        stream_metadata = metadata.to_map(stream['metadata'])
        # stream metadata will have an empty breadcrumb
        if metadata.get(stream_metadata, (), 'selected'):
            selected_streams.append(stream['tap_stream_id'])

    return selected_streams


def sync(config, state, catalog):
    LOGGER.debug('Syncing selected streams')
    selected_stream_ids = get_selected_streams(catalog)

    # Loop over streams in catalog
    for stream in catalog['streams']:
        stream_id = stream['tap_stream_id']
        stream_schema = stream['schema']
        if stream_id in selected_stream_ids:
            LOGGER.debug('Syncing stream: {}'.format(stream_id))

            if stream_id == 'feature':
                occ_client = OccClient(config)

                LOGGER.debug('Writing {} schema: {}'.format('feature', stream_schema))
                singer.write_schema('feature', stream_schema, 'code')

                products = occ_client.get_products()

                for product in products:

                    if 'classifications' not in product:
                        continue

                    for classification in product['classifications']:
                        for feature in classification['features']:
                            singer.write_records(
                                'feature',
                                [
                                    {
                                        'code': feature['code'],
                                        'comparable': feature['comparable'],
                                        'name': feature['name'],
                                        'range': feature['range'],
                                        'unitCode': 'a',
                                        'classificationCode': 'a',
                                        'valueGroupCode': 'a',
                                        'productCode': 'a'
                                    }
                                ])
            else:
                LOGGER.warn('Unknown stream: {}'.format(stream_id))
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
