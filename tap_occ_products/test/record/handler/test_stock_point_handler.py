import unittest
from datetime import datetime, timezone

from tap_occ_products.record.factory import build_record_handler
from tap_occ_products.record.record import Record


class TestStockPointHandler(unittest.TestCase):
    def test_should_generate_stock_point_record(self):
        timestamp = datetime.now(timezone.utc).isoformat()

        stock_points = [
            build_record_handler(Record.STOCK_POINT).generate({
                'code': 'abc123',
                'stock': {
                    'stockLevel': 10
                }
            },
                tenant_id='t1',
                timestamp=timestamp
            ),
            build_record_handler(Record.STOCK_POINT).generate({
                'code': 'abc234',
                'stock': {
                    'stockLevel': 20
                }
            },
                tenant_id='t1',
                timestamp=timestamp
            )
        ]

        self.assertEqual(stock_points, [
            {
                'tenantId': 't1',
                'sku': 'abc123',
                'stock': 10,
                'timestamp': timestamp
            },
            {
                'tenantId': 't1',
                'sku': 'abc234',
                'stock': 20,
                'timestamp': timestamp
            }
        ])
