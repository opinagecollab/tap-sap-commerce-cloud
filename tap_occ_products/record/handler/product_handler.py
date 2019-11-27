from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductHandler(BaseHandler):

    def generate(self, product, **options):
        return {
            'availableForPickup': product['availableForPickup'],
            'averageRating': product['averageRating'],
            'code': product['code'],
            'description': product['description'],
            'manufacturer': product['manufacturer'],
            'name': product['name'],
            'numberOfReviews': product['numberOfReviews'],
            'priceCode': options['price_code'],
            'stock': product['stock'],
            'summary': product['summary'],
            'url': product['url']
        }
