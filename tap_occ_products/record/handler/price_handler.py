from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class PriceHandler(BaseHandler):
    _code = 0

    def generate(self, price, **options):
        self._code += 1

        return {
            'code': str(self._code),
            'currencyIso': price.get('currencyIso'),
            'formattedValue': price.get('formattedValue'),
            'priceType': price.get('priceType'),
            'value': price.get('value')
        }
