import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestFeatureUnit(unittest.TestCase):

    def test_should_generate_feature_unit_record(self):
        feature_units = [
            build_record_handler(Record.FEATURE_UNIT).generate({
                'name': 'grams',
                'symbol': 'g',
                'unitType': '123'
            }),
            build_record_handler(Record.FEATURE_UNIT).generate({
                'name': 'hertz',
                'symbol': 'Hz',
                'unitType': '234'
            })
        ]

        self.assertEqual(feature_units, [
            {
                'name': 'grams',
                'symbol': 'g',
                'unitType': '123'
            },
            {
                'name': 'hertz',
                'symbol': 'Hz',
                'unitType': '234'
            }
        ])

    def test_should_ignore_handled_feature_unit_record(self):
        self.assertIsNone(build_record_handler(Record.FEATURE_UNIT).generate(
            {
                'name': 'grams',
                'symbol': 'g',
                'unitType': '123'
            }))
