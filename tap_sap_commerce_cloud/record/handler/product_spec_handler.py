from tap_sap_commerce_cloud.record.handler.base import BaseHandler
from tap_sap_commerce_cloud.record.handler.decorators import Singleton


@Singleton
class ProductSpecHandler(BaseHandler):

    def generate(self, spec, **options):
        return {
            'tenantId': options.get('tenant_id'),
            'sku': options.get('sku'),
            'specId': options.get('spec_id'),
            'value': "{} {}".format(spec.get('featureValues', [{}])[0].get('value'), spec.get('featureUnit', {}).get('symbol')),
            'pureValue': spec.get('featureValues')[0].get('value'),
            'type': None,
            'interpretedType': None,
            'interpretedValue': None
        }
