from enum import Enum


class Record(Enum):
    CATEGORY = 'category'
    CLASSIFICATION = 'classification'
    FEATURE = 'feature'
    FEATURE_UNIT = 'feature_unit'
    FEATURE_VALUE = 'feature_value'
    PRICE = 'price'
    PRODUCT = 'product'
    PRODUCT_CATEGORY = 'product_category'
    PRODUCT_FEATURE = 'product_feature'
    STOCK = 'stock'
