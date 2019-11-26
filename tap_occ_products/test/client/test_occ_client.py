import unittest
import httpretty
import json
import warnings

from tap_occ_products.client.occ_client import OccClient
from tap_occ_products.test.resources import product_details, product_search_list


class TestOccClient(unittest.TestCase):
    def setUp(self):
        self.client = OccClient({
            'scheme': 'https',
            'base_url': 'test:9002',
            'base_path': '/rest/v2',
            'base_site': '/electronics'
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
        # TODO: use multiple pages by splitting list in two
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
