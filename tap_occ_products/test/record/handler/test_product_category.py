import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductCategory(unittest.TestCase):

    def test_should_generate_product_category_record(self):
        product_categories = [
            build_record_handler(Record.PRODUCT_CATEGORY).generate({
                'productCode': '123456',
                'categoryCode': '1234'
            }),
            build_record_handler(Record.PRODUCT_CATEGORY).generate({
                'productCode': '234567',
                'categoryCode': '2345'
            }),
        ]

        self.assertEqual(product_categories, [
            {
                'productCode': '123456',
                'categoryCode': '1234'
            },
            {
                'productCode': '234567',
                'categoryCode': '2345'
            }
        ])
