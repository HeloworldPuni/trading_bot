"""
Meta-Learning System - Phase D
Tracks the bot's own performance patterns and adapts behavior accordingly.

TODO: Integrate into main.py trading loop:
  - Call meta_learner.record_trade_result() on position close
  - Use meta_learner.should_trade(confidence) instead of hardcoded threshold
  - Use meta_learner.get_position_scaling() for dynamic sizing
"""
import os
import json
import logging
from typing import Dict, List, Any, Optional
from collections import deque
from datetime import datetime

from src.config import Config

logger = logging.getLogger(__name__)

class MetaLearner:
    """
    Phase D: Self-improvement system that learns from the bot's own mistakes.
    
    Key Capabilities:
    1. Adaptive Confidence Thresholds - Adjusts based on recent accuracy
    2. Failure Pattern Detection - Identifies conditions causing losses
    3. Loss Category Analysis - Tracks which types of losses are most common
    """
    
    def __init__(self, history_window: int = 50, state_file: str = "data/meta_learner_state.json"):
        self.history_window = history_window
        self.state_file = state_file
        
        # Sliding window of recent trade results
        self.recent_results: deque = deque(maxlen=history_window)
        
        # Adaptive thresholds (start with defaults)
        self.confidence_threshold = 0.50  # Minimum confidence to act
        self.boost_threshold = 0.70        # Confidence level for position boost
        
        # Loss category tracking
        self.loss_categories: Dict[str, int] = {
            "REGIME_SHIFT": 0,
            "VOLATILITY_SPIKE": 0,
            "BAD_TIMING": 0,
            "MARKET_MOVE": 0,
            "UNKNOWN": 0
        }
        
        # Performance metrics
        self.total_trades = 0
        self.winning_trades = 0
        
        # Load existing state if available
        self._load_state()
        
        logger.info(f"MetaLearner initialized. Confidence threshold: {self.confidence_threshold:.2f}")
    
    def _load_state(self):
        """Load previous state from disk."""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r") as f:
                    state = json.load(f)
                    self.confidence_threshold = state.get("confidence_threshold", 0.50)
                    self.boost_threshold = state.get("boost_threshold", 0.70)
                    self.loss_categories = state.get("loss_categories", self.loss_categories)
                    self.total_trades = state.get("total_trades", 0)
                    self.winning_trades = state.get("winning_trades", 0)
                    logger.info(f"MetaLearner state loaded. Win rate: {self.get_win_rate():.1%}")
            except Exception as e:
                logger.warning(f"Could not load MetaLearner state: {e}")
    
    def _save_state(self):
        """Persist state to disk."""
        try:
            os.makedirs(os.path.dirname(self.state_file), exist_ok=True)
            state = {
                "confidence_threshold": self.confidence_threshold,
                "boost_threshold": self.boost_threshold,
                "loss_categories": self.loss_categories,
                "total_trades": self.total_trades,
                "winning_trades": self.winning_trades,
                "last_updated": datetime.utcnow().isoformat()
            }
            with open(self.state_file, "w") as f:
                json.dump(state, f, indent=2)
        except Exception as e:
            logger.warning(f"Could not save MetaLearner state: {e}")
    
    def record_trade_result(self, won: bool, loss_category: Optional[str] = None, 
                            confidence: float = 0.5, regime: str = "UNKNOWN"):
        """
        Record the outcome of a trade for learning.
        """
        self.total_trades += 1
        if won:
            self.winning_trades += 1
            self.recent_results.append(1)
        else:
            self.recent_results.append(0)
            # Track loss category
            category = loss_category if loss_category else "UNKNOWN"
            if category in self.loss_categories:
                self.loss_categories[category] += 1
        
        # Adapt thresholds every 10 trades
        if self.total_trades % 10 == 0:
            self._adapt_thresholds()
            self._save_state()
    
    def _adapt_thresholds(self):
        """
        Dynamically adjust confidence thresholds based on recent performance.
        """
        if len(self.recent_results) < 10:
            return
            
        recent_win_rate = sum(self.recent_results) / len(self.recent_results)
        
        # If winning a lot, we can be more aggressive (lower threshold)
        if recent_win_rate > 0.6:
            self.confidence_threshold = max(0.40, self.confidence_threshold - 0.02)
            logger.info(f"🎯 MetaLearner: High win rate ({recent_win_rate:.1%}), lowered threshold to {self.confidence_threshold:.2f}")
        
        # If losing a lot, be more conservative (raise threshold)
        elif recent_win_rate < 0.4:
            self.confidence_threshold = min(0.65, self.confidence_threshold + 0.03)
            logger.warning(f"⚠️ MetaLearner: Low win rate ({recent_win_rate:.1%}), raised threshold to {self.confidence_threshold:.2f}")
    
    def get_win_rate(self) -> float:
        """Get overall win rate."""
        if self.total_trades == 0:
            return 0.5
        return self.winning_trades / self.total_trades
    
    def get_recent_win_rate(self) -> float:
        """Get win rate from recent trades only."""
        if len(self.recent_results) == 0:
            return 0.5
        return sum(self.recent_results) / len(self.recent_results)
    
    def should_trade(self, confidence: float, regime_stable: bool = True) -> bool:
        """
        Decide whether to trade based on confidence and current conditions.
        Uses adaptive thresholds learned from performance.
        """
        # Additional caution if regime is unstable
        threshold = self.confidence_threshold
        if not regime_stable:
            threshold += 0.1  # Require higher confidence in unstable regimes
        
        return confidence >= threshold
    
    def get_position_scaling(self, confidence: float) -> float:
        """
        Returns a position size multiplier based on confidence.
        """
        if confidence >= self.boost_threshold:
            return 1.2  # 20% larger position
        elif confidence >= self.confidence_threshold:
            return 1.0  # Normal size
        else:
            return 0.8  # Reduced size
    
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
            "recommendation": None
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
        
        # Generate recommendation based on primary issue
        recommendations = {
            "REGIME_SHIFT": "Consider adding regime transition detection or faster exit triggers during uncertain periods.",
            "VOLATILITY_SPIKE": "Consider tighter stop losses during high ATR periods or avoiding trades when ATR is spiking.",
            "BAD_TIMING": "Entry timing may need refinement. Consider waiting for confirmation candles.",
            "MARKET_MOVE": "Markets moved against you. This is normal variance - check position sizing.",
            "UNKNOWN": "Unable to categorize losses. Review trade logs for patterns."
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
            "top_loss_category": max(self.loss_categories, key=self.loss_categories.get) if sum(self.loss_categories.values()) > 0 else "N/A"
        }
