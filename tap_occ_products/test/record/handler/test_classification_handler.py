import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestClassificationHandler(unittest.TestCase):

    def test_should_generate_classification_record(self):
        classifications = [
            build_record_handler(Record.CLASSIFICATION).generate({
                'code': '123',
                'name': 'Technical details'
            }),
            build_record_handler(Record.CLASSIFICATION).generate({
                'code': '234',
                'name': 'Compatible memory cards'
            })
        ]

        self.assertEqual(classifications, [
            {
                'code': '123',
                'name': 'Technical details'
            },
            {
                'code': '234',
                'name': 'Compatible memory cards'
            }
        ])
