import unittest
import httpretty
import json
import warnings

from tap_occ_products.client.occ_client import OccClient

body = {
    'type': 'productCategorySearchPageWsDTO',
    'breadcrumbs': [],
    'currentQuery': {},
    'facets': [],
    'freeTextSearch': '',
    'pagination': {
        'currentPage': 0,
        'pageSize': 100,
        'sort': 'relevance',
        'totalPages': 1,
        'totalResults': 1
    },
    'products': [
        {
            'availableForPickup': True,
            'averageRating': 0,
            'code': '123456',
            'configurable': False,
            'configuratorType': '',
            'description': 'Product description',
            'images': [
                {
                    'format': 'thumbnail',
                    'imageType': 'PRIMARY',
                    'url': '/medias/thumbnail'
                },
                {
                    'format': 'product',
                    'imageType': 'PRIMARY',
                    'url': '/medias/product'
                }
            ],
            'manufacturer': 'Manufacturer',
            'multidimensional': False,
            'name': 'Product',
            'price': {
                'currencyIso': 'CAD',
                'formattedValue': '$100.00',
                'priceType': 'BUY',
                'value': 100.00
            },
            'priceRange': {},
            'stock': {
                'stockLevel': 4,
                'stockLevelStatus': 'lowStock'
            },
            'summary': 'Product summary',
            'url': '',
            'volumePricesFlag': False
        }
    ]
}


class TestOccClient(unittest.TestCase):
    def setUp(self):
        self.client = OccClient({
            'scheme': 'https',
            'base_url': 'test:9002',
            'base_path': '/rest/v2',
            'base_site': '/electronics'
        })

        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*")

    def test_should_build_proper_url(self):
        self.assertEqual(
            self.client.url,
            'https://test:9002/rest/v2/electronics/products/search?fields=FULL&pageSize=100&currentPage={}'
        )

    @httpretty.activate
    def test_should_get_products(self):
        initial_page = 0
        httpretty.register_uri(
            httpretty.GET,
            self.client.url.format(initial_page),
            body=json.dumps(body)
        )

        products = self.client.get_products()
        self.assertEqual(body['products'], products)
