from tap_sap_commerce_cloud.record.handler.base import BaseHandler
from tap_sap_commerce_cloud.record.handler.decorators import Singleton


@Singleton
class CustomerSpecificPriceHandler(BaseHandler):

    def generate(self, customer_specific_price, **options):
        return {
            'customerId': options.get('customer_id'),
            'tenantId': options.get('tenant_id'),
            'sku': customer_specific_price.get('code'),
            'price': customer_specific_price.get('price')
        }
