from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductHandler(BaseHandler):

    def generate(self, product, **options):
        return {
            'sku': product.get('code'),
            'tenantId': options.get('tenant_id'),
            'categoryId': options.get('category_id'),
            'regularPrice': product.get('price', {}).get('value'),
            'salePrice': None,
            'currency': product.get('price', {}).get('currencyIso'),
            'stock': product.get('stock', {}).get('stockLevel'),
            'name': product.get('name'),
            'description': product.get('description'),
            'summary': product.get('summary'),
            'manufacturer': product.get('manufacturer'),
            'reviewAverage': product.get('averageRating'),
            'reviewCount': product.get('numberOfReviews')
        }
