from tap_occ_products.record.handler.base import BaseHandler
from tap_occ_products.record.handler.decorators import Singleton


@Singleton
class ProductCategoryHandler(BaseHandler):

    def generate(self, codes, **options):
        return {
            'productCode': codes['productCode'],
            'categoryCode': codes['categoryCode']
        }
