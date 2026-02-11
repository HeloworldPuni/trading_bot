import logging
from dataclasses import dataclass
from typing import Dict, List

import pandas as pd

from src.strategies.base import AbstractBaseStrategy, StrategySignal

logger = logging.getLogger(__name__)


@dataclass
class ArbOpportunity:
    type: str
    path: str
    profit_pct: float
    timestamp: float


class ArbitrageStrategy:
    """
    Utility scanner for triangular/funding opportunities.
    """

    def __init__(self, min_profit_pct: float = 0.001, fee_rate: float = 0.001):
        self.min_profit_pct = float(min_profit_pct)
        self.fee_rate = float(fee_rate)

    def scan_triangular(self, prices: Dict[str, float]) -> List[ArbOpportunity]:
        btc_usdt = prices.get("BTC/USDT")
        eth_btc = prices.get("ETH/BTC")
        eth_usdt = prices.get("ETH/USDT")
        if not (btc_usdt and eth_btc and eth_usdt):
            return []

        amt_btc = 100.0 / float(btc_usdt)
        amt_eth = amt_btc / float(eth_btc)
        final_usdt = amt_eth * float(eth_usdt)
        gross = (final_usdt - 100.0) / 100.0
        net = gross - (3 * self.fee_rate)

        if net > self.min_profit_pct:
            return [ArbOpportunity("TRIANGULAR", "USDT->BTC->ETH->USDT", net, 0.0)]
        return []

    def scan_funding(self, funding_rates: Dict[str, float]) -> List[ArbOpportunity]:
        """
        funding_rates should be decimal fractions (0.001 = 0.1%).
        """
        opps = []
        for symbol, rate in funding_rates.items():
            if abs(float(rate)) >= self.min_profit_pct:
                opps.append(ArbOpportunity("FUNDING", symbol, abs(float(rate)), 0.0))
        return opps


class FundingArbitrageStrategy(AbstractBaseStrategy):
    """
    Strategy wrapper used by legacy tests/scripts.
    """

    def __init__(self, funding_threshold: float = 0.05, model_threshold: float = 0.5):
        # funding_threshold expressed in percentage points (0.05 => 0.05%)
        self.funding_threshold = float(funding_threshold)
        super().__init__(name="FundingArbitrage", model_threshold=model_threshold)

    def generate_signal(self, row: pd.Series, context: pd.Series | None = None) -> StrategySignal:
        rate = float(row.get("funding_rate", 0.0))
        if rate >= self.funding_threshold:
            raw = StrategySignal(-1, min(1.0, 0.55 + rate), {"reason": "High positive funding"})
        elif rate <= -self.funding_threshold:
            raw = StrategySignal(1, min(1.0, 0.55 + abs(rate)), {"reason": "High negative funding"})
        else:
            raw = StrategySignal(0, 0.0, {"reason": "Funding neutral"})
        return self.apply_model_filter(raw, row)
