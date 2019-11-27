from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ClassificationHandler(BaseHandler):
    _handled_codes = []

    def generate(self, classification, **options):
        if classification['code'] in self._handled_codes:
            return None

        self._handled_codes.append(classification['code'])

        return {
            'code': classification.get('code'),
            'name': classification.get('name')
        }
