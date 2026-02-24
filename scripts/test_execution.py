import sys
import os
import unittest
import numpy as np
from unittest.mock import MagicMock

sys.path.append(os.getcwd())

from src.core.definitions import Action, ActionDirection, StrategyType, MarketState, RiskLevel, MarketRegime, VolatilityLevel, TrendStrength
from src.execution.router import SmartRouter, OrderType, ExecutionStatus, ActionDirection
from src.execution.algo import ExecutionAlgo
from src.execution.paper import PaperExchange

class TestExecution(unittest.TestCase):
    
    def setUp(self):
        self.router = SmartRouter()
        self.algo = ExecutionAlgo()
        self.exchange = PaperExchange(latency_ms=0)
        
    def create_mock_state(self, spread=0.01, volatility="LOW", current_price=100.0):
        state = MagicMock(spec=MarketState)
        state.spread_pct = spread
        state.volatility_level = MagicMock()
        state.volatility_level.value = volatility
        state.current_price = current_price
        state.funding_extreme = False
        return state
        
    def create_mock_action(self, strategy=StrategyType.MEAN_REVERSION, weight=0.1):
        action = Action(
            strategy=strategy,
            direction=ActionDirection.LONG,
            risk_level=RiskLevel.LOW,
            target_weight=weight
        )
        return action

    def test_router_urgency(self):
        # 1. Low Urgency (MeanRev) + Wide Spread -> LIMIT
        state = self.create_mock_state(spread=0.10) # 10% spread (huge)
        action = self.create_mock_action(StrategyType.MEAN_REVERSION)
        
        req = self.router.route(action, state)
        self.assertEqual(req.order_type, OrderType.LIMIT)
        print("PASS: Router chose LIMIT for Low Urgency/Wide Spread")
        
        # 2. High Urgency (Momentum) + Tight Spread -> MARKET
        state = self.create_mock_state(spread=0.001) # 0.1% spread
        action = self.create_mock_action(StrategyType.MOMENTUM)
        
        req = self.router.route(action, state)
        self.assertEqual(req.order_type, OrderType.MARKET)
        print("PASS: Router chose MARKET for High Urgency/Tight Spread")

    def test_router_twap(self):
        # Large Order -> TWAP
        state = self.create_mock_state(spread=0.01)
        # Use MeanReversion (Low Urgency) so TWAP isn't skipped
        action = self.create_mock_action(StrategyType.MEAN_REVERSION, weight=0.5) 
        
        # Override threshold for test
        self.router.large_order_threshold = 0.2
        
        req = self.router.route(action, state)
        self.assertEqual(req.order_type, OrderType.TWAP)
        print("PASS: Router chose TWAP for Large Order")

    def test_algo_twap(self):
        total = 1.0
        duration = 60 # min
        schedule = self.algo.generate_twap_schedule(total, duration)
        
        self.assertEqual(len(schedule), 60) # 1 per min
        self.assertTrue(np.isclose(sum(schedule), total))
        print(f"PASS: TWAP Schedule generated {len(schedule)} slices summing to {sum(schedule):.2f}")

    def test_paper_limit_fill(self):
        # Place Buy Limit @ 99
        action = self.create_mock_action(StrategyType.MEAN_REVERSION)
        req = self.router.route(action, self.create_mock_state(current_price=100.0))
        req.order_type = OrderType.LIMIT
        req.limit_price = 99.0
        req.direction = ActionDirection.LONG
        
        # Execute (Current 100 > Limit 99) -> PENDING
        report = self.exchange.execute(req, 100.0)
        self.assertEqual(report.status, ExecutionStatus.PENDING)
        
        # Update Price drop to 98 -> FILLED
        fills = self.exchange.update(98.0)
        self.assertEqual(len(fills), 1)
        self.assertEqual(fills[0].status, ExecutionStatus.FILLED)
        print("PASS: Paper Exchange correctly filled Sell Limit on dip.")

if __name__ == '__main__':
    unittest.main()
