import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestFeatureValueHandler(unittest.TestCase):
    def test_should_generate_feature_value_record(self):
        feature_values = [
            build_record_handler(Record.FEATURE_VALUE).generate({
                'productCode': '123456',
                'featureCode': '123',
                'featureValue': '1/2'
            }),
            build_record_handler(Record.FEATURE_VALUE).generate({
                'productCode': '234567',
                'featureCode': '234',
                'featureValue': 'White'
            })
        ]

        self.assertEqual(feature_values, [
            {
                'productCode': '123456',
                'featureCode': '123',
                'featureValue': '1/2'
            },
            {
                'productCode': '234567',
                'featureCode': '234',
                'featureValue': 'White'
            }
        ])
