import unittest

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestPriceHandler(unittest.TestCase):

    def test_should_generate_price_record(self):
        prices = [
            build_record_handler(Record.PRICE).generate({
                'currencyIso': 'USD',
                'formattedValue': '$260.87',
                'priceType': 'BUY',
                'value': 260.87
            }),
            build_record_handler(Record.PRICE).generate({
                'currencyIso': 'CAD',
                'formattedValue': '130.99',
                'priceType': 'BUY',
                'value': 130.99
            })
        ]

        self.assertEqual(prices, [
            {
                'code': 1,
                'currencyIso': 'USD',
                'formattedValue': '$260.87',
                'priceType': 'BUY',
                'value': 260.87
            }, {
                'code': 2,
                'currencyIso': 'CAD',
                'formattedValue': '130.99',
                'priceType': 'BUY',
                'value': 130.99
            }])
