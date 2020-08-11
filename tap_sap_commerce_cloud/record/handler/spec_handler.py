from tap_sap_commerce_cloud.record.handler.base import BaseHandler
from tap_sap_commerce_cloud.record.handler.decorators import Singleton


@Singleton
class SpecHandler(BaseHandler):
    _handled_codes = {}
    _code = 0

    def generate(self, spec, **options):
        if ',' in spec.get('code'):
            code = spec.get('code').split(',')[1].strip()
        else:
            code = spec.get('code')

        if code in self._handled_codes:
            return self._handled_codes.get(code)

        self._code += 1

        #chagne ID format to ex.t1-111
        spec_id = options.get('tenant_id') + "-" + str(self._code)

        self._handled_codes[code] = spec_id

        return {
            'id': spec_id,
            'name': spec.get('name'),
            'baseUnitName': spec.get('featureUnit', {}).get('name'),
            'baseUnitSymbol': spec.get('featureUnit', {}).get('symbol'),
            'comparable': spec.get('comparable'),
            'majorityUnitName' : None,
            'majorityUnitSymbol': None
        }
