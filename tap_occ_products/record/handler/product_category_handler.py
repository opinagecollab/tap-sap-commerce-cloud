from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductCategoryHandler(BaseHandler):

    def generate(self, product_category, **options):
        return {
            'productCode': product_category.get('productCode'),
            'categoryCode': product_category.get('categoryCode')
        }
