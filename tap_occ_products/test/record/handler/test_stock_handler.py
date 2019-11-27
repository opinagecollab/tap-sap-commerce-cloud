import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestStockHandler(unittest.TestCase):

    def test_should_generate_stock_record(self):
        stocks = [
            build_record_handler(Record.STOCK).generate({
                'stockLevel': 123,
                'stockLevelStatus': 'inStock'
            }),

            build_record_handler(Record.STOCK).generate({
                'stockLevel': 234,
                'stockLevelStatus': 'inStock'
            })
        ]

        self.assertEqual(stocks, [
            {
                'code': '1',
                'stockLevel': 123,
                'stockLevelStatus': 'inStock'
            },
            {
                'code': '2',
                'stockLevel': 234,
                'stockLevelStatus': 'inStock'
            }
        ])
