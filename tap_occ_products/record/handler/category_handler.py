from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class CategoryHandler(BaseHandler):
    _handled_categories = {}
    _code = 0

    def generate(self, category, **options):
        if ',' in category.get('code'):
            code = category.get('code').split(',')[1].strip()
        else:
            code = category.get('code')

        if code in self._handled_categories:
            return self._handled_categories.get(code)

        self._code += 1
        category_id = options.get('tenant_id') + str(self._code)

        self._handled_categories[code] = category_id

        return {
            'id': category_id,
            'name': category.get('name')
        }
