from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureUnitHandler(BaseHandler):
    _handled_unit_types = []

    def generate(self, feature_unit, **options):
        if feature_unit['unitType'] in self._handled_unit_types:
            return None

        self._handled_unit_types.append(feature_unit['unitType'])

        return {
            'name': feature_unit.get('name'),
            'symbol': feature_unit.get('symbol'),
            'unitType': feature_unit.get('unitType')
        }
