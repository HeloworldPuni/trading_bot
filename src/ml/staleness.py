"""
Model Staleness Detector - Solution #2
Detects when the trained model is missing features or outdated.
"""
import json
import os
import logging
from typing import List, Set, Optional, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class ModelStalenessChecker:
    """
    Checks if the current model was trained with all available features.
    Triggers retraining when new features are detected.
    """
    
    # Current expected features (from MarketState)
    CURRENT_FEATURES = [
        "market_regime", "volatility_level", "trend_strength",
        "dist_to_high", "dist_to_low",
        "macd", "macd_signal", "macd_hist",
        "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
        "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
        "htf_trend_spread", "htf_rsi", "htf_atr",
        "trading_session", "symbol", "repeats", "current_open_positions",
        "action_taken", "regime_confidence", "regime_stable", "momentum_shift_score"
    ]
    
    def __init__(self, model_dir: str = "models"):
        self.model_dir = model_dir
        self.feature_maps_path = os.path.join(model_dir, "feature_maps.json")
    
    def get_trained_features(self) -> Set[str]:
        """Get features the current model was trained on."""
        if not os.path.exists(self.feature_maps_path):
            return set()
        
        try:
            with open(self.feature_maps_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return set(data.get("feature_columns", []))
        except (json.JSONDecodeError, KeyError):
            return set()
    
    def check_staleness(self) -> Dict[str, Any]:
        """
        Check if model is stale (missing new features).
        Returns status dict with details.
        """
        current = set(self.CURRENT_FEATURES)
        trained = self.get_trained_features()
        
        if not trained:
            return {
                "status": "UNKNOWN",
                "message": "No feature_maps.json found - model features unknown",
                "missing_features": [],
                "extra_features": [],
                "needs_retrain": True
            }
        
        missing = current - trained
        extra = trained - current  # Features in model but removed from code
        
        if missing:
            return {
                "status": "STALE",
                "message": f"Model missing {len(missing)} new features",
                "missing_features": sorted(list(missing)),
                "extra_features": sorted(list(extra)),
                "needs_retrain": True
            }
        
        if extra:
            return {
                "status": "OUTDATED",
                "message": f"Model has {len(extra)} features no longer in code",
                "missing_features": [],
                "extra_features": sorted(list(extra)),
                "needs_retrain": False  # Still usable
            }
        
        return {
            "status": "OK",
            "message": "Model is up-to-date with all features",
            "missing_features": [],
            "extra_features": [],
            "needs_retrain": False
        }
    
    def print_status(self) -> bool:
        """Print staleness status. Returns True if retrain needed."""
        result = self.check_staleness()
        
        if result["status"] == "OK":
            print("[OK] Model features are current")
            return False
        elif result["status"] == "STALE":
            print(f"[WARN] MODEL STALE: Missing features: {result['missing_features']}")
            print("   Run: python scripts/train_policy.py to retrain")
            return True
        elif result["status"] == "UNKNOWN":
            print("[WARN] Model feature status unknown (no feature_maps.json)")
            return True
        else:
            print(f"[INFO] Model has extra features (still usable): {result['extra_features']}")
            return False
    
    def update_feature_maps(self, feature_columns: List[str], session_map: Dict, symbol_map: Dict):
        """Update feature_maps.json after training."""
        data = {
            "feature_columns": feature_columns,
            "session_map": session_map,
            "symbol_map": symbol_map,
            "updated_at": datetime.utcnow().isoformat()
        }
        os.makedirs(self.model_dir, exist_ok=True)
        with open(self.feature_maps_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        logger.info(f"Updated feature_maps.json with {len(feature_columns)} features")


def check_model_staleness() -> bool:
    """Quick check function. Returns True if retrain needed."""
    checker = ModelStalenessChecker()
    return checker.print_status()


if __name__ == "__main__":
    check_model_staleness()
