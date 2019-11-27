from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ClassificationHandler(BaseHandler):
    _handled_codes = []

    def generate(self, classification, **options):
        return {
            'code': classification['code'],
            'name': classification['name']
        }
