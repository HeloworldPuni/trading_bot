
import logging
import pandas as pd
import joblib
import os
import json
from typing import Optional
from src.core.definitions import MarketRegime, VolatilityLevel, TrendStrength, StrategyType, MarketState, Action
from src.ml.registry import ModelRegistry

logger = logging.getLogger(__name__)

class PolicyInference:
    FEATURE_MAPS_PATH = "models/feature_maps.json"
    FEATURE_COLS_BASE = [
        "market_regime", "volatility_level", "trend_strength",
        "dist_to_high", "dist_to_low",
        "macd", "macd_signal", "macd_hist",
        "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
        "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
        "htf_trend_spread", "htf_rsi", "htf_atr",
        "trading_session", "symbol", "repeats", "current_open_positions",
        "action_taken"
    ]
    FEATURE_COLS_EXTRA = [
        "regime_confidence", "regime_stable", "momentum_shift_score"
    ]
    
    def __init__(self, model_path: Optional[str] = None):
        self.registry = ModelRegistry()
        self.model_path = model_path or self.registry.get_active_model_path() or "models/policy_model_v1.pkl"
        self.ensemble = {}
        self.calibrator = None
        self.ensemble_calibrators = {}
        
        # Hard-coded v4 features (consistent with DatasetBuilder)
        self.feature_cols = [
            "market_regime", "volatility_level", "trend_strength",
            "dist_to_high", "dist_to_low", "macd", "macd_signal", "macd_hist",
            "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
            "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
            "htf_trend_spread", "htf_rsi", "htf_atr",
            "trading_session", "symbol", "repeats", "current_open_positions",
            "action_taken", "regime_confidence", "regime_stable", "momentum_shift_score"
        ]
        
        # Consistent mappings from enums
        self.regime_map = {e.value: i for i, e in enumerate(MarketRegime)}
        self.vol_map = {e.value: i for i, e in enumerate(VolatilityLevel)}
        self.trend_map = {e.value: i for i, e in enumerate(TrendStrength)}
        self.strategy_map = {e.value: i for i, e in enumerate(StrategyType)}
        
        # Load persistent maps (ensures training/inference consistency)
        self._load_feature_maps()
        
        self._load_model()

    def _load_feature_maps(self):
        """Load session and symbol maps from persistent file."""
        # Defaults
        self.session_map = {"ASIA": 0, "LONDON": 1, "NY": 2, "OTHER": 3, "OVERLAP": 4}
        self.symbol_map = {"BTC/USDT": 0, "ETH/USDT": 1, "SOL/USDT": 2, "UNKNOWN": 99}
        
        if os.path.exists(self.FEATURE_MAPS_PATH):
            try:
                with open(self.FEATURE_MAPS_PATH, "r") as f:
                    maps = json.load(f)
                self.session_map = maps.get("session_map", self.session_map)
                self.symbol_map = maps.get("symbol_map", self.symbol_map)
                logger.info(f"Loaded feature maps: {len(self.symbol_map)} symbols")
            except Exception as e:
                logger.warning(f"Failed to load feature maps: {e}, using defaults")

    def _load_model(self):
        # 1. Main Model
        if self.model_path and os.path.exists(self.model_path):
            try:
                data = joblib.load(self.model_path)
                if isinstance(data, dict) and "model" in data:
                    self.model = data["model"]
                    if isinstance(data.get("feature_cols"), list):
                        self.feature_cols = data["feature_cols"]
                    self.calibrator = data.get("calibrator")
                else:
                    self.model = data
                logger.info(f"PolicyInference: Main model loaded from {self.model_path}")
            except Exception as e:
                logger.error(f"PolicyInference: Failed to load main model: {e}")
        
        # 2. Ensemble Experts from Registry
        active_version = self.registry.data.get("active_version")
        if active_version:
            model_info = self.registry.data["models"].get(active_version)
            if model_info and model_info.get("type") == "ensemble":
                experts = model_info.get("experts", {})
                for regime, info in experts.items():
                    path = info.get("path")
                    # Ensure path is absolute relative to root
                    if not os.path.isabs(path):
                        root = os.path.dirname(self.registry.registry_path)
                        path = os.path.join(os.path.dirname(root), path)
                    
                    if os.path.exists(path):
                        try:
                            data = joblib.load(path)
                            if isinstance(data, dict) and "model" in data:
                                self.ensemble[regime] = data["model"]
                                self.ensemble_calibrators[regime] = data.get("calibrator")
                            else:
                                self.ensemble[regime] = data
                            logger.info(f"PolicyInference: Expert '{regime}' loaded from Registry ({active_version})")
                        except Exception as e:
                            logger.error(f"PolicyInference: Failed to load expert '{regime}': {e}")

        # 3. Fallback: Local Ensemble Experts (if registry not found/empty)
        if not self.ensemble:
            regimes = ["bull", "bear", "sideways"]
            for r in regimes:
                path = f"models/policy_{r}.pkl"
                if os.path.exists(path):
                    try:
                        data = joblib.load(path)
                        if isinstance(data, dict) and "model" in data:
                            self.ensemble[r] = data["model"]
                            if isinstance(data.get("feature_cols"), list):
                                self.feature_cols = data["feature_cols"]
                            self.ensemble_calibrators[r] = data.get("calibrator")
                        else:
                            self.ensemble[r] = data
                        logger.info(f"PolicyInference: Expert '{r}' loaded from local storage.")
                    except Exception as e:
                        logger.error(f"PolicyInference: Failed to load local expert '{r}': {e}")

        if not self.model and not self.ensemble:
            logger.warning("PolicyInference: No models found. Shadow mode will return neutral scores.")

    def predict_confidence(self, state: MarketState, action: Action, repeats: int = 0) -> float:
        """
        Returns probability (0.0 to 1.0) that the proposed action is 'Good'.
        Routes to Ensemble Expert if available, fallback to Main model.
        """
        # Select Model
        model = getattr(self, "model", None)
        calibrator = getattr(self, "calibrator", None)
        regime_val = state.market_regime.value
        
        if regime_val in [MarketRegime.BULL_TREND.value]:
            model = self.ensemble.get("bull", model)
            calibrator = self.ensemble_calibrators.get("bull", calibrator)
        elif regime_val in [MarketRegime.BEAR_TREND.value]:
            model = self.ensemble.get("bear", model)
            calibrator = self.ensemble_calibrators.get("bear", calibrator)
        elif regime_val in [MarketRegime.SIDEWAYS_LOW_VOL.value, MarketRegime.SIDEWAYS_HIGH_VOL.value, MarketRegime.TRANSITION.value]:
            model = self.ensemble.get("sideways", model)
            calibrator = self.ensemble_calibrators.get("sideways", calibrator)

        if action.strategy == StrategyType.WAIT:
            return 0.5 # Wait actions are treated as neutral baseline
            
        if model is None:
            return 0.5 # Default neutral

        try:
            # 1. Map features exactly like DatasetBuilder
            features = {
                "market_regime": self.regime_map.get(state.market_regime.value, -1),
                "volatility_level": self.vol_map.get(state.volatility_level.value, -1),
                "trend_strength": self.trend_map.get(state.trend_strength.value, -1),
                "dist_to_high": state.dist_to_high,
                "dist_to_low": state.dist_to_low,
                
                # Phase 31 Indicators
                "macd": state.macd,
                "macd_signal": state.macd_signal,
                "macd_hist": state.macd_hist,
                "bb_upper": state.bb_upper,
                "bb_lower": state.bb_lower,
                "bb_mid": state.bb_mid,
                "atr": state.atr,
                "volume_delta": state.volume_delta,
                "spread_pct": state.spread_pct,
                "body_pct": state.body_pct,
                "gap_pct": state.gap_pct,
                "volume_zscore": state.volume_zscore,
                "liquidity_proxy": state.liquidity_proxy,
                "htf_trend_spread": state.htf_trend_spread,
                "htf_rsi": state.htf_rsi,
                "htf_atr": state.htf_atr,

                "trading_session": self.session_map.get(state.trading_session, 3),
                "symbol": self.symbol_map.get(state.symbol, 0),
                "repeats": repeats,
                "current_open_positions": state.current_open_positions,
                "action_taken": self.strategy_map.get(action.strategy.value, 0),
                
                # Phase C: Anticipatory Regime Detection
                "regime_confidence": state.regime_confidence,
                "regime_stable": 1 if state.regime_stable else 0,
                "momentum_shift_score": state.momentum_shift_score
            }

            # 2. Determine feature columns (align with model expectations)
            feature_cols = list(self.feature_cols) if self.feature_cols else list(features.keys())
            if hasattr(model, "feature_names_in_"):
                feature_cols = list(model.feature_names_in_)
            elif hasattr(model, "n_features_in_"):
                expected = int(model.n_features_in_)
                if expected == len(self.FEATURE_COLS_BASE):
                    feature_cols = list(self.FEATURE_COLS_BASE)
                elif expected == len(self.FEATURE_COLS_BASE) + len(self.FEATURE_COLS_EXTRA):
                    feature_cols = list(self.FEATURE_COLS_BASE + self.FEATURE_COLS_EXTRA)
                else:
                    feature_cols = feature_cols[:expected]

            # 3. DataFrame for Model (ensure column order + defaults)
            row = {k: features.get(k, 0.0) for k in feature_cols}
            df = pd.DataFrame([row], columns=feature_cols)
            
            # 4. Predict Proba
            # Both XGBoost and LightGBM follow sklearn's predict_proba
            probs = model.predict_proba(df)[0]
            confidence = float(probs[1]) # Class 1 = 'Good'

            if calibrator is not None:
                try:
                    confidence = float(calibrator.predict_proba([[confidence]])[0][1])
                except Exception as e:
                    logger.warning(f"Calibration failed: {e}")
            
            return confidence
        except Exception as e:
            import traceback
            logger.error(f"Inference failed: {e}\n{traceback.format_exc()}")
            return 0.5
