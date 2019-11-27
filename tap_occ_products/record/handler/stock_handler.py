from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class StockHandler(BaseHandler):
    _code = 0

    def generate(self, stock, **options):
        self._code += 1

        return {
            'code': str(self._code),
            'stockLevel': stock.get('stockLevel'),
            'stockLevelStatus': stock.get('stockLevelStatus')
        }