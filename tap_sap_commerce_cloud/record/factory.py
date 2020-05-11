from tap_occ_products.record.record import Record
from tap_occ_products.record.handler.category_handler import CategoryHandler
from tap_occ_products.record.handler.customer_specific_price_handler import CustomerSpecificPriceHandler
from tap_occ_products.record.handler.price_point_handler import PricePointHandler
from tap_occ_products.record.handler.product_handler import ProductHandler
from tap_occ_products.record.handler.product_spec_handler import ProductSpecHandler
from tap_occ_products.record.handler.spec_handler import SpecHandler
from tap_occ_products.record.handler.stock_point_handler import StockPointHandler


def build_record_handler(record: Record):
    if record == Record.CATEGORY:
        return CategoryHandler.get_instance()

    if record == Record.CUSTOMER_SPECIFIC_PRICE:
        return CustomerSpecificPriceHandler.get_instance()

    if record == Record.PRICE_POINT:
        return PricePointHandler.get_instance()

    if record == Record.PRODUCT:
        return ProductHandler.get_instance()

    if record == Record.PRODUCT_SPEC:
        return ProductSpecHandler.get_instance()

    if record == Record.SPEC:
        return SpecHandler.get_instance()

    if record == Record.STOCK_POINT:
        return StockPointHandler.get_instance()