from urllib.parse import urlunparse

from tap_sap_commerce_cloud.record.handler.base import BaseHandler
from tap_sap_commerce_cloud.record.handler.decorators import Singleton


@Singleton
class ProductHandler(BaseHandler):

    def generate(self, product, **options):
        return {
            'sku': product.get('code'),
            'tenantId': options.get('tenant_id'),
            'regularPrice': product.get('price', {}).get('value'),
            'salePrice': None,
            'currency': product.get('price', {}).get('currencyIso'),
            'stock': product.get('stock', {}).get('stockLevel'),
            'imageUri': urlunparse((
                options.get('config').get('api_scheme'),
                options.get('config').get('api_base_url'),
                product.get('images')[0].get('url'),
                None,
                None,
                None
            )) if len(product.get('images', [])) > 0 else None,
            'detailsUri': urlunparse((
                options.get('config').get('ui_scheme'),
                options.get('config').get('ui_base_url'),
                options.get('config').get('ui_base_site') +
                options.get('config').get('ui_product_path') +
                '/' + product.get('code'),
                None,
                None,
                None
            )) if not product.get('url', None) is None else None,
            'name': product.get('name'),
            'description': product.get('description'),
            'summary': product.get('summary'),
            'manufacturer': product.get('manufacturer'),
            'reviewAverage': product.get('averageRating'),
            'reviewCount': product.get('numberOfReviews')
        }
