from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductHandler(BaseHandler):

    def generate(self, product, **options):
        return {
            'availableForPickup': product.get('availableForPickup'),
            'averageRating': product.get('averageRating'),
            'code': product.get('code'),
            'description': product.get('description'),
            'manufacturer': product.get('manufacturer'),
            'name': product.get('name'),
            'numberOfReviews': product.get('numberOfReviews'),
            'summary': product.get('summary'),
            'url': product.get('url'),
            'priceCode': options['price_code'],
            'stockCode': options['stock_code']
        }
