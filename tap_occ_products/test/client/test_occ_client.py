import unittest
import httpretty
import json
import warnings

from tap_occ_products.client.occ_client import OccClient

product_search_list = {
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
        'totalResults': 2
    },
    'products': [
        {
            'availableForPickup': True,
            'code': '123456',
            'name': 'Product',
            'price': {
                'currencyIso': 'CAD',
                'value': 100.00
            },
            'stock': {
                'stockLevel': 4
            },
            'url': ''
        },
        {
            'availableForPickup': True,
            'code': '234567',
            'name': 'Product',
            'price': {
                'currencyIso': 'CAD',
                'value': 29.99
            },
            'stock': {
                'stockLevel': 12
            },
            'url': ''
        }
    ]
}

product_details = {
    '123456': {
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
    },
    '234567': {
        'availableForPickup': True,
        'averageRating': 0,
        'code': '234567',
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
            'formattedValue': '$29.99',
            'priceType': 'BUY',
            'value': 29.99
        },
        'priceRange': {},
        'stock': {
            'stockLevel': 12,
            'stockLevelStatus': 'lowStock'
        },
        'summary': 'Product summary',
        'url': '',
        'volumePricesFlag': False
    },
}


class TestOccClient(unittest.TestCase):
    def setUp(self):
        self.client = OccClient({
            'scheme': 'https',
            'baseUrl': 'test:9002',
            'basePath': '/rest/v2',
            'baseSite': '/electronics'
        })

        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*")

    def test_should_build_proper_search_url(self):
        self.assertEqual(
            self.client.search_url,
            'https://test:9002/rest/v2/electronics/products/search?fields=BASIC&pageSize=100&currentPage={}'
        )

    def test_should_build_proper_product_url(self):
        self.assertEqual(
            self.client.product_url,
            'https://test:9002/rest/v2/electronics/products/{}?fields=FULL'
        )

    @httpretty.activate
    def test_should_get_products(self):
        initial_page = 0
        httpretty.register_uri(
            httpretty.GET,
            self.client.search_url.format(initial_page),
            body=json.dumps(product_search_list))

        product_list = []
        for sku in product_details:
            httpretty.register_uri(
                httpretty.GET,
                self.client.product_url.format(sku),
                body=json.dumps(product_details[sku]))

            product_list.append(product_details[sku])

        result = self.client.get_products()
        self.assertEqual(product_list, result)
