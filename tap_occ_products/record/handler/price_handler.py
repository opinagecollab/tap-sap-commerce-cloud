from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class PriceHandler(BaseHandler):
    _code = 0

    def generate(self, price, **options):
        self._code += 1

        return {
            'code': self._code,
            'currencyIso': price['currencyIso'],
            'formattedValue': price['formattedValue'],
            'priceType': price['priceType'],
            'value': price['value']
        }
