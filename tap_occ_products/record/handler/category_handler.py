from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class CategoryHandler(BaseHandler):

    def generate(self, category, **options):
        return {
            'code': category['code'],
            'name': category['name'],
            'url': category['url']
        }
