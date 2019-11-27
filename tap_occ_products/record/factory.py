from tap_occ_products.record.record import Record
from tap_occ_products.record.handler.category_handler import CategoryHandler
from tap_occ_products.record.handler.classification_handler import ClassificationHandler
from tap_occ_products.record.handler.feature_handler import FeatureHandler
from tap_occ_products.record.handler.feature_unit_handler import FeatureUnitHandler
from tap_occ_products.record.handler.feature_value_handler import FeatureValueHandler
from tap_occ_products.record.handler.price_handler import PriceHandler
from tap_occ_products.record.handler.product_handler import ProductHandler
from tap_occ_products.record.handler.product_category_handler import ProductCategoryHandler
from tap_occ_products.record.handler.product_classification_handler import ProductClassificationHandler


def build_record_handler(record: Record):
    if record == Record.CATEGORY:
        return CategoryHandler.get_instance()

    if record == Record.CLASSIFICATION:
        return ClassificationHandler.get_instance()

    if record == Record.FEATURE:
        return FeatureHandler.get_instance()

    if record == Record.FEATURE_UNIT:
        return FeatureUnitHandler.get_instance()

    if record == Record.FEATURE_VALUE:
        return FeatureValueHandler.get_instance()

    if record == Record.PRICE:
        return PriceHandler.get_instance()

    if record == Record.PRODUCT:
        return ProductHandler.get_instance()

    if record == Record.PRODUCT_CATEGORY:
        return ProductCategoryHandler.get_instance()

    if record == Record.PRODUCT_CLASSIFICATION:
        return ProductClassificationHandler.get_instance()