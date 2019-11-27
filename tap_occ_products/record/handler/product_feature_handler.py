from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductFeatureHandler(BaseHandler):

    def generate(self, product_feature, **options):
        return {
            'productCode': product_feature.get('productCode'),
            'featureCode': product_feature.get('featureCode'),
            'featureValue': product_feature.get('featureValue')
        }
