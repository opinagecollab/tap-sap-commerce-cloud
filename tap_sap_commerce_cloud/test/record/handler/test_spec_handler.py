import unittest

from tap_sap_commerce_cloud.record.factory import build_record_handler
from tap_sap_commerce_cloud.record.record import Record


class TestSpecHandler(unittest.TestCase):
    def test_should_generate_spec_record(self):
        specs = [
            build_record_handler(Record.SPEC).generate({
                    'code': 'specCode123',
                    'comparable': True,
                    'name': 'weight',
                    'featureUnit': {
                        'name': 'kilogram',
                        'symbol': 'kg'
                    }
                },
                tenant_id='t1'
            ),
            build_record_handler(Record.SPEC).generate({
                    'code': 'specCode234',
                    'comparable': True,
                    'name': 'color',
                    'featureUnit': {
                        'name': '.',
                        'symbol': '.'
                    }
                },
                tenant_id='t1'
            )
        ]

        self.assertEqual(specs, [
            {
                'id': 't1-1',
                'name': 'weight',
                'baseUnitName': 'kilogram',
                'baseUnitSymbol': 'kg',
                'comparable': True,
                'majorityUnitName' : None,
                'majorityUnitSymbol': None
            },
            {
                'id': 't1-2',
                'name': 'color',
                'baseUnitName': '.',
                'baseUnitSymbol': '.',
                'comparable': True,
                'majorityUnitName' : None,
                'majorityUnitSymbol': None
            }
        ])

    def test_should_ignore_handled_spec_record(self):
        self.assertEqual(build_record_handler(Record.SPEC).generate(
            {
                'code': 'specCode123',
                'comparable': True,
                'name': 'weight',
                'featureUnit': {
                    'name': 'kilogram',
                    'symbol': 'kg'
                }
            },
            tenant_id='t1'
        ), 't1-1')
