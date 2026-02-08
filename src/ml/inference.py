
import logging
import pandas as pd
import joblib
import os
import json
from src.core.definitions import MarketRegime, VolatilityLevel, TrendStrength, StrategyType, MarketState, Action
from src.ml.registry import ModelRegistry

logger = logging.getLogger(__name__)

class PolicyInference:
    FEATURE_MAPS_PATH = "models/feature_maps.json"
    
    def __init__(self, model_path: Optional[str] = None):
        self.registry = ModelRegistry()
        self.model_path = model_path or self.registry.get_active_model_path() or "models/policy_model_v1.pkl"
        self.model = None
        self.ensemble = {}
        
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
                    if path and os.path.exists(path):
                        try:
                            data = joblib.load(path)
                            if isinstance(data, dict) and "model" in data:
                                self.ensemble[regime] = data["model"]
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
        model = self.model
        regime_val = state.market_regime.value
        
        if regime_val == MarketRegime.BULL_TREND.value:
            model = self.ensemble.get("bull", model)
        elif regime_val == MarketRegime.BEAR_TREND.value:
            model = self.ensemble.get("bear", model)
        elif regime_val == MarketRegime.SIDEWAYS_LOW_VOL.value:
            model = self.ensemble.get("sideways", model)

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

            # 2. DataFrame for Model
            df = pd.DataFrame([features])
            
            # 3. Predict Proba
            # Both XGBoost and LightGBM follow sklearn's predict_proba
            probs = model.predict_proba(df)[0]
            confidence = float(probs[1]) # Class 1 = 'Good'
            
            return confidence
        except Exception as e:
            logger.warning(f"Inference failed: {e}")
            return 0.5
