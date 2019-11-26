from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class FeatureUnitHandler(BaseHandler):

    def generate(self, feature_unit, **options):
        return None
