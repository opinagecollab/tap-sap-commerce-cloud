import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductFeature(unittest.TestCase):

    def test_should_generate_product_feature_record(self):
        product_classifications = [
            build_record_handler(Record.PRODUCT_CLASSIFICATION).generate({
                'productCode': '123456',
                'featureCode': '123',
                'featureValue': '1/2'
            }),
            build_record_handler(Record.PRODUCT_CLASSIFICATION).generate({
                'productCode': '234567',
                'featureCode': '234',
                'featureValue': 'White'
            })
        ]

        self.assertEqual(product_classifications, [
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

