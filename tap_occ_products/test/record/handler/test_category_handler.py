import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestCategoryHandler(unittest.TestCase):
    def test_should_generate_category_record(self):
        categories = [
            build_record_handler(Record.CATEGORY).generate(
                {
                    'code': '1234',
                    'name': 'laptops',
                    'url': '/laptops'
                }
            ),
            build_record_handler(Record.CATEGORY).generate(
                {
                    'code': '2345',
                    'name': 'e-readers',
                    'url': '/e-readers'
                }
            )
        ]

        self.assertEqual(categories, [
            {
                'code': '1234',
                'name': 'laptops',
                'url': '/laptops'
            },
            {
                'code': '2345',
                'name': 'e-readers',
                'url': '/e-readers'
            }
        ])

    def test_should_ignore_handled_category_record(self):
        self.assertIsNone(build_record_handler(Record.CATEGORY).generate(
            {
                'code': '1234',
                'name': 'laptops',
                'url': '/laptops'
            }))

