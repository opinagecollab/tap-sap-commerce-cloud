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
            'code': feature.get('code'),
            'comparable': feature.get('comparable'),
            'description': feature.get('description'),
            'name': feature.get('name'),
            'range': feature.get('range'),
            'type': feature.get('type'),
            'classificationCode': options['classification_code'],
            'unitCode': options['unit_code']
        }
