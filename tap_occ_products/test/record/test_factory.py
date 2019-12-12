import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record

from tap_occ_products.record.handler.category_handler import CategoryHandler
from tap_occ_products.record.handler.classification_handler import ClassificationHandler
from tap_occ_products.record.handler.feature_handler import FeatureHandler
from tap_occ_products.record.handler.feature_unit_handler import FeatureUnitHandler
from tap_occ_products.record.handler.feature_value_handler import FeatureValueHandler
from tap_occ_products.record.handler.price_handler import PriceHandler
from tap_occ_products.record.handler.product_handler import ProductHandler
from tap_occ_products.record.handler.product_category_handler import ProductCategoryHandler
from tap_occ_products.record.handler.product_feature_handler import ProductFeatureHandler


class TestFactory(unittest.TestCase):

    def test_should_build_category_handler(self):
        category_handler = build_record_handler(Record.CATEGORY)
        self.assertTrue(isinstance(category_handler, CategoryHandler))

    def test_should_build_classification_handler(self):
        classification_handler = build_record_handler(Record.CLASSIFICATION)
        self.assertTrue(isinstance(classification_handler, ClassificationHandler))

    def test_should_build_feature_handler(self):
        feature_handler = build_record_handler(Record.FEATURE)
        self.assertTrue(isinstance(feature_handler, FeatureHandler))

    def test_should_build_feature_unit_handler(self):
        feature_unit_handler = build_record_handler(Record.FEATURE_UNIT)
        self.assertTrue(isinstance(feature_unit_handler, FeatureUnitHandler))

    def test_should_build_feature_value_handler(self):
        feature_value_handler = build_record_handler(Record.FEATURE_VALUE)
        self.assertTrue(isinstance(feature_value_handler, FeatureValueHandler))

    def test_should_build_price_handler(self):
        price_handler = build_record_handler(Record.PRICE)
        self.assertTrue(isinstance(price_handler, PriceHandler))

    def test_should_build_product_handler(self):
        product_handler = build_record_handler(Record.PRODUCT)
        self.assertTrue(isinstance(product_handler, ProductHandler))

    def test_should_build_product_category_handler(self):
        product_category_handler = build_record_handler(Record.PRODUCT_CATEGORY)
        self.assertTrue(isinstance(product_category_handler, ProductCategoryHandler))

    def test_should_build_product_feature_handler(self):
        product_feature_handler = build_record_handler(Record.PRODUCT_FEATURE)
        self.assertTrue(isinstance(product_feature_handler, ProductFeatureHandler))
