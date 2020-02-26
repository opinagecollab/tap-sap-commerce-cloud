import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestProductHandler(unittest.TestCase):

    def test_should_generate_product_record(self):
        products = [
            build_record_handler(Record.PRODUCT).generate(
                {
                    'code': '123456',
                    'price': {
                        'currencyIso': 'USD',
                        'value': 1.23
                    },
                    'stock': {
                        'stockLevel': 10.0
                    },
                    'name': 'Sony Product',
                    'description': 'Product description',
                    'summary': 'Product summary',
                    'manufacturer': 'Sony',
                    'averageRating': 3.7,
                    'numberOfReviews': 123
                },
                tenant_id='t1',
                category_id='t11'
            ),
            build_record_handler(Record.PRODUCT).generate(
                {
                    'code': '234567',
                    'price': {
                        'currencyIso': 'USD',
                        'value': 3.70
                    },
                    'stock': {
                        'stockStatus': 'inStock'
                    },
                    'name': 'Apple Product',
                    'description': 'Product description',
                    'summary': 'Product summary',
                    'manufacturer': 'Apple',
                    'averageRating': 4.9,
                    'numberOfReviews': 1283
                },
                tenant_id='t1',
                category_id='t12'
            )
        ]

        self.assertEqual(products, [
            {
                'sku': '123456',
                'tenantId': 't1',
                'categoryId': 't11',
                'regularPrice': 1.23,
                'currency': 'USD',
                'salePrice': None,
                'stock': 10.0,
                'name': 'Sony Product',
                'description': 'Product description',
                'summary': 'Product summary',
                'manufacturer': 'Sony',
                'reviewAverage': 3.7,
                'reviewCount': 123
            },
            {
                'sku': '234567',
                'tenantId': 't1',
                'categoryId': 't12',
                'regularPrice': 3.70,
                'salePrice': None,
                'currency': 'USD',
                'stock': None,
                'name': 'Apple Product',
                'description': 'Product description',
                'summary': 'Product summary',
                'manufacturer': 'Apple',
                'reviewAverage': 4.9,
                'reviewCount': 1283
            }
        ])
