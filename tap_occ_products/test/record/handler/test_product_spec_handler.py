import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductSpecHandler(unittest.TestCase):
    def test_should_generate_product_spec_record(self):
        specs = [
            build_record_handler(Record.PRODUCT_SPEC).generate({
                    'featureUnit': {
                        'name': 'gram',
                        'symbol': 'g'
                    },
                    'featureValues': [
                        {
                            'value': '320'
                        }
                    ]
                },
                tenant_id='t1',
                sku='abc123',
                spec_id='t11'
            ),

            build_record_handler(Record.PRODUCT_SPEC).generate({
                    'featureUnit': {
                        'name': 'gigahertz',
                        'symbol': 'GHz'
                    },
                    'featureValues': [
                        {
                            'value': '1.8'
                        }
                    ]
                },
                tenant_id='t1',
                sku='abc123',
                spec_id='t12'
            )
        ]

        self.assertEqual(specs, [
            {
                'tenantId': 't1',
                'sku': 'abc123',
                'specId': 't11',
                'value': '320 g',
                'pureValue': '320',
                'type': None,
                'interpretedType': None,
                'interpretedValue': None,
            },
            {
                'tenantId': 't1',
                'sku': 'abc123',
                'specId': 't12',
                'value': '1.8 GHz',
                'pureValue': '1.8',
                'type': None,
                'interpretedType': None,
                'interpretedValue': None,
            },
        ])
