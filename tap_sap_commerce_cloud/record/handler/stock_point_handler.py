from tap_sap_commerce_cloud.record.handler.base import BaseHandler
from tap_sap_commerce_cloud.record.handler.decorators import Singleton


@Singleton
class StockPointHandler(BaseHandler):
    _counter = 0

    def generate(self, product, **options):
        self._counter += 1

        return {
            'id': "{}.{}".format(options.get('timestamp'), self._counter),
            'tenantId': options.get('tenant_id'),
            'sku': product.get('code'),
            'timestamp': options.get('timestamp'),
            'stock': product.get('stock', {}).get('stockLevel')
        }
