"""
Experiment manager
Evaluates candidate configurations against champion baseline metrics.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class ExperimentCriteria:
    min_trades: int = 30
    min_win_rate_delta: float = 0.0
    min_sharpe_delta: float = 0.0
    max_drawdown_increase: float = 0.0


class ExperimentManager:
    def evaluate(
        self,
        candidate: Dict[str, Any],
        champion: Dict[str, Any],
        criteria: ExperimentCriteria = ExperimentCriteria(),
    ) -> Dict[str, Any]:
        cand_trades = int(candidate.get("trades", 0))
        if cand_trades < criteria.min_trades:
            return {
                "approved": False,
                "reason": f"Insufficient sample: {cand_trades} < {criteria.min_trades}",
            }

        win_rate_delta = float(candidate.get("win_rate", 0.0)) - float(champion.get("win_rate", 0.0))
        sharpe_delta = float(candidate.get("sharpe", 0.0)) - float(champion.get("sharpe", 0.0))
        dd_increase = float(candidate.get("max_drawdown", 0.0)) - float(champion.get("max_drawdown", 0.0))

        approved = (
            win_rate_delta >= criteria.min_win_rate_delta
            and sharpe_delta >= criteria.min_sharpe_delta
            and dd_increase <= criteria.max_drawdown_increase
        )

        return {
            "approved": approved,
            "metrics": {
                "win_rate_delta": win_rate_delta,
                "sharpe_delta": sharpe_delta,
                "drawdown_increase": dd_increase,
            },
            "reason": "PASS" if approved else "FAIL",
        }

