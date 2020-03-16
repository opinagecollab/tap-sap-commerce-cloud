from urllib.parse import urlunparse

import singer
import requests
import urllib3

LOGGER = singer.get_logger()


class OccClient:
    PRODUCT_SEARCH_PATH = '/products/search?fields=BASIC&pageSize=100&currentPage={}'
    PRODUCT_PATH = '/products/{}?fields=FULL'

    def __init__(self, config):
        self.scheme = config['api_scheme']
        self.base_url = config['api_base_url']
        self.base_path = config['api_base_path']
        self.base_site = config['api_base_site']

        self.search_url = urlunparse((
            self.scheme, self.base_url, self.base_path + self.base_site + self.PRODUCT_SEARCH_PATH, None, None, None
        ))

        self.product_url = urlunparse((
            self.scheme, self.base_url, self.base_path + self.base_site + self.PRODUCT_PATH, None, None, None
        ))

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def fetch_products(self):
        initial_page = 0
        products = []

        response = self.fetch_product_list(initial_page)
        for product in response['products']:
            products.append(self.fetch_product_details(product['code']))

        for page in range(1, response['pagination']['totalPages']):
            response = self.fetch_product_list(page)
            for product in response['products']:
                products.append(self.fetch_product_details(product['code']))

        return products

    def fetch_product_list(self, page):
        response = requests.get(self.search_url.format(page), verify=False, timeout=10)

        if response.status_code != 200:
            raise Exception('Failed to fetch product list with status code: {}'.format(response.status_code))

        return response.json()

    def fetch_product_details(self, sku):
        response = requests.get(self.product_url.format(sku), verify=False, timeout=10)
        if response.status_code != 200:
            raise Exception('Failed to fetch product details with status code: {}'.format(response.status_code))

        return response.json()
