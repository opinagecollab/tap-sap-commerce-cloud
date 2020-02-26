from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class StockPointHandler(BaseHandler):
    def generate(self, product, **options):
        return {
            'tenantId': options.get('tenant_id'),
            'sku': product.get('code'),
            'timestamp': options.get('timestamp'),
            'stock': product.get('stock', {}).get('stockLevel')
        }
