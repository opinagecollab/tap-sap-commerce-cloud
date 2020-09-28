from tap_sap_commerce_cloud.record.record import Record
from tap_sap_commerce_cloud.record.handler.category_handler import CategoryHandler
from tap_sap_commerce_cloud.record.handler.customer_specific_price_handler import CustomerSpecificPriceHandler
from tap_sap_commerce_cloud.record.handler.price_point_handler import PricePointHandler
from tap_sap_commerce_cloud.record.handler.product_handler import ProductHandler
from tap_sap_commerce_cloud.record.handler.product_spec_handler import ProductSpecHandler
from tap_sap_commerce_cloud.record.handler.category_product_handler import CategoryProductHandler
from tap_sap_commerce_cloud.record.handler.spec_handler import SpecHandler
from tap_sap_commerce_cloud.record.handler.stock_point_handler import StockPointHandler


def build_record_handler(record: Record):
    if record == Record.CATEGORY:
        # pylint: disable=no-member
        return CategoryHandler.get_instance()

    if record == Record.CUSTOMER_SPECIFIC_PRICE:
        # pylint: disable=no-member
        return CustomerSpecificPriceHandler.get_instance()

    if record == Record.PRICE_POINT:
        # pylint: disable=no-member
        return PricePointHandler.get_instance()

    if record == Record.PRODUCT:
        # pylint: disable=no-member
        return ProductHandler.get_instance()

    if record == Record.CATEGORY_PRODUCT:
        # pylint: disable=no-member
        return CategoryProductHandler.get_instance()

    if record == Record.PRODUCT_SPEC:
        # pylint: disable=no-member
        return ProductSpecHandler.get_instance()

    if record == Record.SPEC:
        # pylint: disable=no-member
        return SpecHandler.get_instance()

    if record == Record.STOCK_POINT:
        # pylint: disable=no-member
        return StockPointHandler.get_instance()