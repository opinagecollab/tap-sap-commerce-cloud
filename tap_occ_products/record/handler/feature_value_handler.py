from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureValueHandler(BaseHandler):

    def generate(self, feature_value, **options):
        return {
            'productCode': feature_value.get('productCode'),
            'featureCode': feature_value.get('featureCode'),
            'featureValue': feature_value.get('featureValue')
        }
