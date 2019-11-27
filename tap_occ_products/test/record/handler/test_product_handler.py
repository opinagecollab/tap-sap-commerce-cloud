import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductHandler(unittest.TestCase):

    def test_should_generate_product(self):
        products = [
            build_record_handler(Record.PRODUCT).generate(
                {
                    'code': '123456',
                    'availableForPickup': True,
                    'averageRating': 4.56,
                    'description': 'Product description',
                    'manufacturer': 'Sony',
                    'name': 'Sony Product',
                    'numberOfReviews': 12,
                    'stock': 10,
                    'summary': 'Product summary',
                    'url': 'http://product.url'
                },
                price_code=1
            ),
            build_record_handler(Record.PRODUCT).generate(
                {
                    'code': '234567',
                    'availableForPickup': False,
                    'averageRating': 1.23,
                    'description': 'Product description',
                    'manufacturer': 'Apple',
                    'name': 'Apple Product',
                    'numberOfReviews': 32,
                    'stock': 9,
                    'summary': 'Product summary',
                    'url': 'http://product.url'
                },
                price_code=2
            )
        ]

        self.assertEqual(products, [
            {
                'code': '123456',
                'availableForPickup': True,
                'averageRating': 4.56,
                'description': 'Product description',
                'manufacturer': 'Sony',
                'name': 'Sony Product',
                'numberOfReviews': 12,
                'stock': 10,
                'summary': 'Product summary',
                'url': 'http://product.url',
                'priceCode': 1
            },
            {
                'code': '234567',
                'availableForPickup': False,
                'averageRating': 1.23,
                'description': 'Product description',
                'manufacturer': 'Apple',
                'name': 'Apple Product',
                'numberOfReviews': 32,
                'priceCode': 2,
                'stock': 9,
                'summary': 'Product summary',
                'url': 'http://product.url'
            }
        ])