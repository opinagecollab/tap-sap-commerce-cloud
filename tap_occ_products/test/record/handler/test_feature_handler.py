import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestFeatureHandler(unittest.TestCase):

    def test_should_generate_feature_record(self):
        features = [
            build_record_handler(Record.FEATURE).generate(
                {
                    'code': '123',
                    'comparable': True,
                    'description': 'Feature description',
                    'name': 'Feature name',
                    'range': False,
                    'type': 'Feature type'
                },
                unit_code='123',
                classification_code='123'
            ),
            build_record_handler(Record.FEATURE).generate(
                {
                    'code': '234',
                    'comparable': True,
                    'description': 'Feature description',
                    'name': 'Feature name',
                    'range': False,
                    'type': 'Feature type'
                },
                unit_code='234',
                classification_code='234'
            )
        ]

        self.assertEqual(features, [
            {
                'code': '123',
                'comparable': True,
                'classificationCode': '123',
                'description': 'Feature description',
                'name': 'Feature name',
                'range': False,
                'type': 'Feature type',
                'unitCode': '123'
            },
            {
                'code': '234',
                'comparable': True,
                'classificationCode': '234',
                'description': 'Feature description',
                'name': 'Feature name',
                'range': False,
                'type': 'Feature type',
                'unitCode': '234'
            }
        ])

    def test_should_ignore_handled_feature_record(self):
        self.assertIsNone(build_record_handler(Record.FEATURE).generate(
            {
                'code': '123',
                'comparable': True,
                'description': 'Feature description',
                'name': 'Feature name',
                'range': False,
                'type': 'Feature type'
            },
            unit_code='123',
            classification_code='123'))
