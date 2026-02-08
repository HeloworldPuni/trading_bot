import os
import shutil
import unittest

from src.config import Config
from src.core.portfolio import Portfolio


class TestPortfolioMultiPosition(unittest.TestCase):
    def setUp(self):
        self._orig_max_per_symbol = Config.MAX_POSITIONS_PER_SYMBOL
        self._orig_max_concurrent = Config.MAX_CONCURRENT_POSITIONS
        Config.MAX_POSITIONS_PER_SYMBOL = 2
        Config.MAX_CONCURRENT_POSITIONS = 10
        self.test_data_dir = "tests/data"
        os.makedirs(self.test_data_dir, exist_ok=True)
        self.state_path = os.path.join(self.test_data_dir, "portfolio_state.json")
        if os.path.exists(self.state_path):
            os.remove(self.state_path)

        self.portfolio = Portfolio(initial_balance=1000.0, load_state=False)
        self.portfolio.state_file = self.state_path

    def tearDown(self):
        Config.MAX_POSITIONS_PER_SYMBOL = self._orig_max_per_symbol
        Config.MAX_CONCURRENT_POSITIONS = self._orig_max_concurrent
        if os.path.exists(self.test_data_dir):
            shutil.rmtree(self.test_data_dir)

    def test_multi_positions_per_symbol(self):
        opened1 = self.portfolio.open_position(
            "BTC/USDT", "LONG", 100.0, 100.0, 110.0, 90.0, "d1", leverage=1
        )
        opened2 = self.portfolio.open_position(
            "BTC/USDT", "LONG", 101.0, 100.0, 111.0, 91.0, "d2", leverage=1
        )
        self.assertTrue(opened1)
        self.assertTrue(opened2)
        self.assertEqual(self.portfolio.count_positions_for_symbol("BTC/USDT"), 2)

        self.portfolio.update_metrics("BTC/USDT", 105.0)
        closed = self.portfolio.close_position("BTC/USDT", 105.0, reason="TP", decision_id="d1")
        self.assertIsNotNone(closed)
        self.assertEqual(self.portfolio.count_positions_for_symbol("BTC/USDT"), 1)

        closed2 = self.portfolio.close_position("BTC/USDT", 105.0, reason="TP")
        self.assertIsNotNone(closed2)
        self.assertEqual(self.portfolio.count_positions_for_symbol("BTC/USDT"), 0)


if __name__ == "__main__":
    unittest.main()
