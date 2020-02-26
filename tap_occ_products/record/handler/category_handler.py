from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class CategoryHandler(BaseHandler):
    _handled_categories = {}
    _code = 0

    def generate(self, category, **options):
        if category.get('code') in self._handled_categories:
            return self._handled_categories.get(category.get('code'))

        self._code += 1
        category_id = options.get('tenant_id') + str(self._code)

        self._handled_categories[category.get('code')] = category_id

        return {
            'id': category_id,
            'name': category.get('name')
        }
