from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class PriceHandler(BaseHandler):

    def generate(self, price, **options):
        return None
