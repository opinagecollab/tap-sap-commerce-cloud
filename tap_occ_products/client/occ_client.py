from urllib.parse import urlunparse

import singer
import requests

LOGGER = singer.get_logger()


class OccClient:
    PRODUCT_SEARCH_PATH = '/products/search?fields=FULL&pageSize=100&currentPage={}'

    def __init__(self, config):
        self.scheme = config['scheme']
        self.base_url = config['base_url']
        self.base_path = config['base_path']
        self.base_site = config['base_site']

        self.url = urlunparse((
            self.scheme, self.base_url, self.base_path + self.base_site + self.PRODUCT_SEARCH_PATH, None, None, None
        ))

    def get_products(self):
        initial_page = 0
        products = []

        response = self.get_products_from_page(initial_page)
        for product in response['products']:
            products.append(product)

        for page in range(1, response['pagination']['totalPages']):
            response = self.get_products_from_page(page)
            for product in response['products']:
                products.append(product)

        return products

    def get_products_from_page(self, page):
        response = requests.get(self.url.format(page))

        if response.status_code != 200:
            raise Exception('Failed to fetch products with status code: {}'.format(response.status_code))

        return response.json()
