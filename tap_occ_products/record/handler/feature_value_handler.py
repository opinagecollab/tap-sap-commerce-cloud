from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureValueHandler(BaseHandler):

    def generate(self, feature_value, **options):
        return None
