from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductFeatureHandler(BaseHandler):

    def generate(self, product_feature, **options):
        return {
            'productCode': product_feature['productCode'],
            'featureCode': product_feature['featureCode'],
            'featureValue': product_feature['featureValue']
        }
