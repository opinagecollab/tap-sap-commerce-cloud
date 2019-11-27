from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class CategoryHandler(BaseHandler):
    _handled_codes = []

    def generate(self, category, **options):
        if category['code'] in self._handled_codes:
            return None

        self._handled_codes.append(category['code'])

        return {
            'code': category.get('code'),
            'name': category.get('name'),
            'url': category.get('url')
        }
