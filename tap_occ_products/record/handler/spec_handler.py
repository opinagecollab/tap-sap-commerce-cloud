from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class SpecHandler(BaseHandler):
    _handled_codes = {}
    _code = 0

    def generate(self, spec, **options):
        if spec.get('code') in self._handled_codes:
            return self._handled_codes.get(spec.get('code'))

        self._code += 1
        spec_id = options.get('tenant_id') + str(self._code)

        self._handled_codes[spec['code']] = spec_id

        return {
            'id': spec_id,
            'name': spec.get('name'),
            'unitName': spec.get('featureUnit', {}).get('name'),
            'unitSymbol': spec.get('featureUnit', {}).get('symbol'),
            'comparable': spec.get('comparable')
        }
