import unittest

from tap_sap_commerce_cloud.record.factory import build_record_handler
from tap_sap_commerce_cloud.record.record import Record


class TestCustomerSpecificPriceHandler(unittest.TestCase):
    def test_should_generate_customer_specific_price_record(self):
        classifications = [
            build_record_handler(Record.CUSTOMER_SPECIFIC_PRICE).generate({
                    'code': 'abc123',
                    'price': 50.0
                },
                tenant_id='t1',
                customer_id='c1'
            ),
            build_record_handler(Record.CUSTOMER_SPECIFIC_PRICE).generate({
                    'code': 'abc123',
                    'price': 70.0
                },
                tenant_id='t1',
                customer_id='c2'
            )
        ]

        self.assertEqual(classifications, [
            {
                'customerId': 'c1',
                'tenantId': 't1',
                'sku': 'abc123',
                'price': 50.0
            },
            {
                'customerId': 'c2',
                'tenantId': 't1',
                'sku': 'abc123',
                'price': 70.0
            }
        ])
