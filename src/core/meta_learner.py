"""
Meta-Learning System - Phase D
Tracks the bot's own performance patterns and adapts behavior accordingly.

Integrated into main.py trading loop:
  - record_trade_result() on position close
  - should_trade() gating for confidence
  - get_position_scaling() for dynamic sizing
"""

import json
import logging
import os
from collections import deque
from datetime import UTC, datetime
from typing import Any, Dict, List, Optional, Tuple

from src.config import Config

logger = logging.getLogger(__name__)


class MetaLearner:
    """
    Phase D: Self-improvement system that learns from the bot's own mistakes.

    Key capabilities:
    1. Adaptive confidence thresholds based on recent win rate
    2. Loss category analytics
    3. Strategy+regime context adaptation policy
    """

    def __init__(self, history_window: int = 50, state_file: str = "data/meta_learner_state.json"):
        self.history_window = history_window
        self.state_file = state_file

        # Sliding window of recent trade results
        self.recent_results: deque = deque(maxlen=history_window)

        # Adaptive thresholds (start with defaults)
        self.confidence_threshold = 0.50
        self.boost_threshold = 0.70

        # Global loss category tracking
        self.loss_categories: Dict[str, int] = self._empty_loss_categories()

        # Context buckets keyed by "<STRATEGY>|<REGIME>"
        self.context_stats: Dict[str, Dict[str, Any]] = {}

        # Adaptive policy controls
        self.policy_enabled = Config.ADAPTIVE_POLICY_ENABLED
        self.policy_min_samples = Config.ADAPTIVE_POLICY_MIN_SAMPLES
        self.policy_min_dominance = Config.ADAPTIVE_POLICY_MIN_DOMINANCE
        self.policy_max_score_penalty = Config.ADAPTIVE_POLICY_MAX_SCORE_PENALTY
        self.policy_max_threshold_bonus = Config.ADAPTIVE_POLICY_MAX_THRESHOLD_BONUS
        self.policy_min_size_multiplier = Config.ADAPTIVE_POLICY_MIN_SIZE_MULTIPLIER
        self.policy_max_size_multiplier = Config.ADAPTIVE_POLICY_MAX_SIZE_MULTIPLIER
        self.policy_recovery_win_rate = Config.ADAPTIVE_POLICY_RECOVERY_WIN_RATE

        # Performance metrics
        self.total_trades = 0
        self.winning_trades = 0

        # Load existing state if available
        self._load_state()

        logger.info("MetaLearner initialized. Confidence threshold: %.2f", self.confidence_threshold)

    @staticmethod
    def _empty_loss_categories() -> Dict[str, int]:
        return {
            "REGIME_SHIFT": 0,
            "VOLATILITY_SPIKE": 0,
            "BAD_TIMING": 0,
            "MARKET_MOVE": 0,
            "UNKNOWN": 0,
        }

    @staticmethod
    def _context_key(strategy: Optional[str], regime: Optional[str]) -> str:
        strat = str(strategy or "UNKNOWN").upper()
        reg = str(regime or "UNKNOWN").upper()
        return f"{strat}|{reg}"

    @staticmethod
    def _parse_context_key(key: str) -> Tuple[str, str]:
        if "|" in key:
            strat, regime = key.split("|", 1)
            return strat, regime
        return key, "UNKNOWN"

    def _new_context_bucket(self) -> Dict[str, Any]:
        return {
            "total": 0,
            "wins": 0,
            "losses": 0,
            "loss_categories": self._empty_loss_categories(),
        }

    def _get_context_bucket(self, strategy: Optional[str], regime: Optional[str]) -> Dict[str, Any]:
        key = self._context_key(strategy, regime)
        if key not in self.context_stats:
            self.context_stats[key] = self._new_context_bucket()
        return self.context_stats[key]

    def _load_state(self) -> None:
        """Load previous state from disk."""
        if not os.path.exists(self.state_file):
            return
        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                state = json.load(f)
            self.confidence_threshold = state.get("confidence_threshold", 0.50)
            self.boost_threshold = state.get("boost_threshold", 0.70)
            self.loss_categories = state.get("loss_categories", self.loss_categories)
            self.context_stats = state.get("context_stats", {})
            self.total_trades = state.get("total_trades", 0)
            self.winning_trades = state.get("winning_trades", 0)
            logger.info("MetaLearner state loaded. Win rate: %.1f%%", self.get_win_rate() * 100)
        except Exception as e:
            logger.warning("Could not load MetaLearner state: %s", e)

    def _save_state(self) -> None:
        """Persist state to disk."""
        try:
            os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
            state = {
                "confidence_threshold": self.confidence_threshold,
                "boost_threshold": self.boost_threshold,
                "loss_categories": self.loss_categories,
                "context_stats": self.context_stats,
                "total_trades": self.total_trades,
                "winning_trades": self.winning_trades,
                "last_updated": datetime.now(UTC).isoformat(),
            }
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logger.warning("Could not save MetaLearner state: %s", e)

    def _record_context_result(
        self,
        won: bool,
        strategy: Optional[str],
        regime: Optional[str],
        loss_category: Optional[str],
    ) -> None:
        bucket = self._get_context_bucket(strategy=strategy, regime=regime)
        bucket["total"] += 1
        if won:
            bucket["wins"] += 1
            return

        bucket["losses"] += 1
        category = str(loss_category or "UNKNOWN").upper()
        if category not in bucket["loss_categories"]:
            category = "UNKNOWN"
        bucket["loss_categories"][category] += 1

    def record_trade_result(
        self,
        won: bool,
        loss_category: Optional[str] = None,
        confidence: float = 0.5,
        regime: str = "UNKNOWN",
        strategy: Optional[str] = None,
        entry_regime: Optional[str] = None,
        exit_reason: Optional[str] = None,
    ) -> None:
        """
        Record the outcome of a trade for learning.
        """
        _ = confidence
        _ = exit_reason

        self.total_trades += 1
        if won:
            self.winning_trades += 1
            self.recent_results.append(1)
        else:
            self.recent_results.append(0)
            category = str(loss_category or "UNKNOWN").upper()
            if category in self.loss_categories:
                self.loss_categories[category] += 1
            else:
                self.loss_categories["UNKNOWN"] += 1

        self._record_context_result(
            won=won,
            strategy=strategy,
            regime=entry_regime or regime,
            loss_category=loss_category,
        )

        # Adapt thresholds every 10 trades
        if self.total_trades % 10 == 0:
            self._adapt_thresholds()

        # Save after every trade to avoid data loss on restart
        self._save_state()

    def sync_from_history(self, trade_history: List[Dict[str, Any]]) -> None:
        """
        Full recount from portfolio trade history to guarantee accuracy.
        Called on startup to ensure MetaLearner matches actual trade records.
        """
        history_count = len(trade_history)
        if history_count == 0:
            return

        old_total = self.total_trades
        old_wins = self.winning_trades

        self.total_trades = history_count
        self.winning_trades = sum(1 for t in trade_history if t.get("realized_pnl_usd", 0) > 0)

        self.loss_categories = self._empty_loss_categories()
        self.context_stats = {}

        for trade in trade_history:
            won = trade.get("realized_pnl_usd", 0) > 0
            cat = str(trade.get("loss_category") or "UNKNOWN").upper()
            if not won:
                if cat in self.loss_categories:
                    self.loss_categories[cat] += 1
                else:
                    self.loss_categories["UNKNOWN"] += 1

            self._record_context_result(
                won=won,
                strategy=trade.get("strategy"),
                regime=trade.get("entry_regime") or trade.get("exit_regime") or "UNKNOWN",
                loss_category=trade.get("loss_category"),
            )

        self.recent_results.clear()
        for trade in trade_history[-self.history_window:]:
            won = trade.get("realized_pnl_usd", 0) > 0
            self.recent_results.append(1 if won else 0)

        self._adapt_thresholds()
        self._save_state()

        if old_total != self.total_trades or old_wins != self.winning_trades:
            logger.warning(
                "MetaLearner resynced: %s->%s trades, %s->%s wins",
                old_total,
                self.total_trades,
                old_wins,
                self.winning_trades,
            )
        logger.info(
            "MetaLearner synced: %s trades, WR: %.1f%%, Threshold: %.2f",
            self.total_trades,
            self.get_win_rate() * 100,
            self.confidence_threshold,
        )

    def _adapt_thresholds(self) -> None:
        """
        Dynamically adjust confidence thresholds based on recent performance.
        """
        if len(self.recent_results) < 10:
            return

        recent_win_rate = sum(self.recent_results) / len(self.recent_results)

        if recent_win_rate > 0.6:
            self.confidence_threshold = max(0.40, self.confidence_threshold - 0.02)
            logger.info(
                "MetaLearner: High win rate (%.1f%%), lowered threshold to %.2f",
                recent_win_rate * 100,
                self.confidence_threshold,
            )
        elif recent_win_rate < 0.4:
            self.confidence_threshold = min(0.65, self.confidence_threshold + 0.03)
            logger.warning(
                "MetaLearner: Low win rate (%.1f%%), raised threshold to %.2f",
                recent_win_rate * 100,
                self.confidence_threshold,
            )

    def get_win_rate(self) -> float:
        if self.total_trades == 0:
            return 0.5
        return self.winning_trades / self.total_trades

    def get_recent_win_rate(self) -> float:
        if len(self.recent_results) == 0:
            return 0.5
        return sum(self.recent_results) / len(self.recent_results)

    def _aggregate_strategy_context(self, strategy: Optional[str]) -> Optional[Dict[str, Any]]:
        """Aggregate context across regimes for a strategy."""
        if not strategy:
            return None
        strategy = str(strategy).upper()
        aggregate = self._new_context_bucket()
        found = False
        for key, bucket in self.context_stats.items():
            strat, _ = self._parse_context_key(key)
            if strat != strategy:
                continue
            found = True
            aggregate["total"] += int(bucket.get("total", 0))
            aggregate["wins"] += int(bucket.get("wins", 0))
            aggregate["losses"] += int(bucket.get("losses", 0))
            cat_counts = bucket.get("loss_categories", {})
            for cat in aggregate["loss_categories"]:
                aggregate["loss_categories"][cat] += int(cat_counts.get(cat, 0))
        return aggregate if found else None

    def get_policy_adjustments(
        self,
        strategy: Optional[str],
        regime: Optional[str],
        regime_stable: bool = True,
    ) -> Dict[str, Any]:
        """
        Convert historical loss patterns into bounded policy adjustments.
        """
        baseline = {
            "score_multiplier": 1.0,
            "confidence_buffer": 0.0,
            "size_multiplier": 1.0,
            "dominant_loss_category": "NONE",
            "sample_size": 0,
            "applied": False,
        }
        if not self.policy_enabled:
            return baseline

        key = self._context_key(strategy, regime)
        bucket = self.context_stats.get(key) or self._aggregate_strategy_context(strategy)
        if not bucket:
            return baseline

        total = int(bucket.get("total", 0))
        losses = int(bucket.get("losses", 0))
        baseline["sample_size"] = total

        if total < self.policy_min_samples or losses < self.policy_min_samples:
            return baseline

        loss_mix = bucket.get("loss_categories", {})
        dominant = max(loss_mix, key=lambda x: loss_mix.get(x, 0))
        dominant_count = int(loss_mix.get(dominant, 0))
        if dominant_count <= 0:
            return baseline

        dominance = dominant_count / max(1, losses)
        if dominance < self.policy_min_dominance:
            return baseline

        baseline["dominant_loss_category"] = dominant

        context_loss_rate = losses / max(1, total)
        intensity = max(0.5, min(1.0, (0.65 * dominance) + (0.35 * context_loss_rate)))

        category_penalties = {
            "REGIME_SHIFT": {"score": 0.18, "threshold": 0.05, "size": 0.18},
            "VOLATILITY_SPIKE": {"score": 0.22, "threshold": 0.06, "size": 0.24},
            "BAD_TIMING": {"score": 0.15, "threshold": 0.04, "size": 0.14},
            "MARKET_MOVE": {"score": 0.08, "threshold": 0.02, "size": 0.10},
            "UNKNOWN": {"score": 0.10, "threshold": 0.03, "size": 0.12},
        }
        penalties = category_penalties.get(dominant, category_penalties["UNKNOWN"])

        regime_label = str(regime or "UNKNOWN").upper()
        instability_boost = 1.0
        if dominant == "REGIME_SHIFT" and (not regime_stable or regime_label == "TRANSITION"):
            instability_boost = 1.15

        score_penalty = penalties["score"] * intensity * instability_boost
        threshold_bonus = penalties["threshold"] * intensity * instability_boost
        size_penalty = penalties["size"] * intensity * instability_boost

        # Soften penalties if recent behavior recovered.
        if self.get_recent_win_rate() >= self.policy_recovery_win_rate:
            score_penalty *= 0.8
            threshold_bonus *= 0.75
            size_penalty *= 0.8

        score_penalty = min(self.policy_max_score_penalty, score_penalty)
        threshold_bonus = min(self.policy_max_threshold_bonus, threshold_bonus)

        score_multiplier = 1.0 - score_penalty
        size_multiplier = 1.0 - size_penalty
        size_multiplier = max(
            self.policy_min_size_multiplier,
            min(self.policy_max_size_multiplier, size_multiplier),
        )

        baseline.update(
            {
                "score_multiplier": score_multiplier,
                "confidence_buffer": threshold_bonus,
                "size_multiplier": size_multiplier,
                "applied": True,
            }
        )
        return baseline

    def should_trade(self, confidence: float, regime_stable: bool = True) -> bool:
        """
        Decide whether to trade based on confidence and current conditions.
        Uses adaptive thresholds learned from performance.
        """
        threshold = self.confidence_threshold
        if not regime_stable:
            threshold += 0.1
        return confidence >= threshold

    def get_position_scaling(self, confidence: float) -> float:
        """
        Returns a position size multiplier based on confidence.
        """
        if confidence >= self.boost_threshold:
            return 1.2
        if confidence >= self.confidence_threshold:
            return 1.0
        return 0.8

    def get_loss_analysis(self) -> Dict[str, Any]:
        """
        Get analysis of loss categories for debugging/improvement.
        """
        total_losses = sum(self.loss_categories.values())
        if total_losses == 0:
            return {"message": "No losses recorded yet"}

        analysis = {
            "total_losses": total_losses,
            "categories": {},
            "primary_issue": None,
            "recommendation": None,
        }

        max_category = None
        max_count = 0

        for category, count in self.loss_categories.items():
            pct = (count / total_losses) * 100
            analysis["categories"][category] = {"count": count, "percent": round(pct, 1)}
            if count > max_count:
                max_count = count
                max_category = category

        analysis["primary_issue"] = max_category

        recommendations = {
            "REGIME_SHIFT": "Consider faster exits and stricter confidence in transition regimes.",
            "VOLATILITY_SPIKE": "Consider lower size and tighter risk when ATR expands.",
            "BAD_TIMING": "Entry timing may need stronger confirmation.",
            "MARKET_MOVE": "Likely variance and sizing; review exposure and clustering.",
            "UNKNOWN": "Unable to categorize losses. Review trade logs for patterns.",
        }
        analysis["recommendation"] = recommendations.get(max_category, "Review trade logs.")

        return analysis

    def get_summary(self) -> Dict[str, Any]:
        """Get a summary of the meta-learner state for dashboard display."""
        return {
            "total_trades": self.total_trades,
            "win_rate": self.get_win_rate(),
            "recent_win_rate": self.get_recent_win_rate(),
            "confidence_threshold": self.confidence_threshold,
            "top_loss_category": max(self.loss_categories, key=self.loss_categories.get)
            if sum(self.loss_categories.values()) > 0
            else "N/A",
            "policy_enabled": self.policy_enabled,
            "context_buckets": len(self.context_stats),
        }
