import unittest

from tap_sap_commerce_cloud.record.factory import build_record_handler
from tap_sap_commerce_cloud.record.record import Record


class TestProductHandler(unittest.TestCase):

    def test_should_generate_product_record(self):
        config = {
          "api_scheme": "https",
          "api_base_url": "localhost:9002",
          "api_base_path": "/rest/v2",
          "api_base_site": "/electronics",
          "ui_scheme": "http",
          "ui_base_url": "localhost:4200",
          "ui_base_site": "/electronics-spa",
          "ui_product_path": "/product"
        }
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
                    'images': [
                        {
                            "format": "thumbnail",
                            "imageType": "PRIMARY",
                            "url": "/medias/image.png"
                        }
                    ],
                    'name': 'Sony Product',
                    'description': 'Product description',
                    'summary': 'Product summary',
                    'manufacturer': 'Sony',
                    'averageRating': 3.7,
                    'numberOfReviews': 123,
                    'url': '/electronics/products/123456'
                },
                tenant_id='t1',
                category_id='t11',
                config=config
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
                    'images': [
                        {
                            "format": "thumbnail",
                            "imageType": "PRIMARY",
                            "url": "/medias/image.png"
                        }
                    ],
                    'name': 'Apple Product',
                    'description': 'Product description',
                    'summary': 'Product summary',
                    'manufacturer': 'Apple',
                    'averageRating': 4.9,
                    'numberOfReviews': 1283,
                    'url': '/electronics/products/234567'
                },
                tenant_id='t1',
                category_id='t12',
                config=config
            )
        ]

        self.assertEqual(products, [
            {
                'sku': '123456',
                'tenantId': 't1',
                'regularPrice': 1.23,
                'currency': 'USD',
                'salePrice': None,
                'stock': 10.0,
                'imageUri': 'https://localhost:9002/medias/image.png',
                'name': 'Sony Product',
                'description': 'Product description',
                'summary': 'Product summary',
                'manufacturer': 'Sony',
                'reviewAverage': 3.7,
                'reviewCount': 123,
                'detailsUri': 'http://localhost:4200/electronics-spa/product/123456'
            },
            {
                'sku': '234567',
                'tenantId': 't1',
                'regularPrice': 3.70,
                'salePrice': None,
                'currency': 'USD',
                'stock': None,
                'imageUri': 'https://localhost:9002/medias/image.png',
                'name': 'Apple Product',
                'description': 'Product description',
                'summary': 'Product summary',
                'manufacturer': 'Apple',
                'reviewAverage': 4.9,
                'reviewCount': 1283,
                'detailsUri': 'http://localhost:4200/electronics-spa/product/234567'
            }
        ])
