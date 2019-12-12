import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductFeature(unittest.TestCase):

    def test_should_generate_product_feature_record(self):
        product_feature = [
            build_record_handler(Record.PRODUCT_FEATURE).generate({
                'productCode': '123456',
                'featureCode': '123'
            }),
            build_record_handler(Record.PRODUCT_FEATURE).generate({
                'productCode': '234567',
                'featureCode': '234'
            })
        ]

        self.assertEqual(product_feature, [
            {
                'productCode': '123456',
                'featureCode': '123'
            },
            {
                'productCode': '234567',
                'featureCode': '234'
            }
        ])

