from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureHandler(BaseHandler):
    _handled_codes = []

    def generate(self, feature, **options):
        if feature['code'] in self._handled_codes:
            return None

        self._handled_codes.append(feature['code'])

        return {
            'code': feature['code'],
            'comparable': feature['comparable'],
            'description': feature['description'],
            'name': feature['name'],
            'range': feature['range'],
            'type': feature['type'],
            'classificationCode': options['classification_code'],
            'unitCode': options['unit_code']
        }
