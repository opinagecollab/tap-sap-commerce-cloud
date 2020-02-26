import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestCategoryHandler(unittest.TestCase):
    def test_should_generate_category_record(self):
        categories = [
            build_record_handler(Record.CATEGORY).generate({
                    'code': 'c123',
                    'name': 'laptops',
                },
                tenant_id='t1'
            ),
            build_record_handler(Record.CATEGORY).generate(
                {
                    'code': 'c234',
                    'name': 'e-readers',
                },
                tenant_id='t1'
            )
        ]

        self.assertEqual(categories, [
            {
                'id': 't11',
                'name': 'laptops',
            },
            {
                'id': 't12',
                'name': 'e-readers',
            }
        ])

    def test_should_ignore_handled_category_record(self):
        self.assertEqual(build_record_handler(Record.CATEGORY).generate(
            {
                'code': 'c123',
                'name': 'laptops'
            },
            tenant_id='t1'
        ), 't11')

