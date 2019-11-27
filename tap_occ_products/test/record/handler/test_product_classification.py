import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductClassification(unittest.TestCase):

    def test_should_generate_product_classification_record(self):
        product_classifications = [
            build_record_handler(Record.PRODUCT_CLASSIFICATION).generate({
                'productCode': '123456',
                'classificationCode': '123'
            }),
            build_record_handler(Record.PRODUCT_CLASSIFICATION).generate({
                'productCode': '234567',
                'classificationCode': '234'
            })
        ]

        self.assertEqual(product_classifications, [
            {
                'productCode': '123456',
                'classificationCode': '123'
            },
            {
                'productCode': '234567',
                'classificationCode': '234'
            }
        ])

