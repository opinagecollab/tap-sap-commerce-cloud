from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureHandler(BaseHandler):

    def generate(self, feature, **options):
        return None
