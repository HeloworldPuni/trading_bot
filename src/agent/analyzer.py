"""
Observer + Analyst layer
Transforms trade history into diagnostics for planning.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Dict, List


class ObserverAnalyzer:
    def build_diagnostics(self, trade_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        total = len(trade_history)
        if total == 0:
            return {
                "total_trades": 0,
                "win_rate": 0.0,
                "avg_pnl_pct": 0.0,
                "by_strategy": {},
                "by_regime": {},
                "loss_categories": {},
                "top_issue": "NO_DATA",
            }

        wins = 0
        pnl_pct_total = 0.0
        by_strategy = defaultdict(lambda: {"trades": 0, "wins": 0, "avg_pnl_pct": 0.0})
        by_regime = defaultdict(lambda: {"trades": 0, "wins": 0, "avg_pnl_pct": 0.0})
        loss_categories = defaultdict(int)

        for t in trade_history:
            pnl = float(t.get("realized_pnl_pct", 0.0))
            won = pnl > 0
            if won:
                wins += 1
            pnl_pct_total += pnl

            strat = str(t.get("strategy") or "UNKNOWN")
            regime = str(t.get("entry_regime") or t.get("exit_regime") or "UNKNOWN")

            by_strategy[strat]["trades"] += 1
            by_strategy[strat]["wins"] += 1 if won else 0
            by_strategy[strat]["avg_pnl_pct"] += pnl

            by_regime[regime]["trades"] += 1
            by_regime[regime]["wins"] += 1 if won else 0
            by_regime[regime]["avg_pnl_pct"] += pnl

            cat = t.get("loss_category")
            if cat:
                loss_categories[str(cat)] += 1

        for bucket in [by_strategy, by_regime]:
            for _, stats in bucket.items():
                trades = max(1, stats["trades"])
                stats["win_rate"] = stats["wins"] / trades
                stats["avg_pnl_pct"] = stats["avg_pnl_pct"] / trades

        top_issue = "NO_LOSS_CATEGORY"
        if loss_categories:
            top_issue = max(loss_categories, key=loss_categories.get)

        return {
            "total_trades": total,
            "win_rate": wins / total,
            "avg_pnl_pct": pnl_pct_total / total,
            "by_strategy": dict(by_strategy),
            "by_regime": dict(by_regime),
            "loss_categories": dict(loss_categories),
            "top_issue": top_issue,
        }

