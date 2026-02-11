import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict

import pandas as pd

logger = logging.getLogger(__name__)


@dataclass
class StrategySignal:
    signal: int
    confidence: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class AbstractBaseStrategy(ABC):
    def __init__(self, name: str, model_threshold: float = 0.5):
        self.name = name
        self.model_threshold = float(model_threshold)
        self.ml_model = None
        self._load_model()

    def _load_model(self):
        candidates = [
            os.path.join("models", f"{self.name}.joblib"),
            os.path.join("models", f"{self.name}.pkl"),
        ]
        for path in candidates:
            if not os.path.exists(path):
                continue
            try:
                import joblib

                self.ml_model = joblib.load(path)
                logger.info("Loaded strategy model: %s", path)
                return
            except Exception as e:
                logger.warning("Could not load strategy model %s: %s", path, e)

    def apply_model_filter(self, raw_signal: StrategySignal, features: pd.Series) -> StrategySignal:
        if raw_signal.signal == 0:
            return raw_signal

        if self.ml_model is None:
            return raw_signal

        try:
            x = pd.DataFrame([features.to_dict()])
            model = self.ml_model
            # Support dict payloads with embedded estimator.
            if isinstance(model, dict) and "model" in model:
                model = model["model"]
            prob = float(model.predict_proba(x)[0][1]) if hasattr(model, "predict_proba") else 0.5
            out = StrategySignal(
                signal=raw_signal.signal if prob >= self.model_threshold else 0,
                confidence=prob if prob >= self.model_threshold else 0.0,
                metadata=dict(raw_signal.metadata),
            )
            out.metadata["ml_probability"] = prob
            if out.signal == 0:
                out.metadata["reason"] = "ML Filter Rejected"
            return out
        except Exception as e:
            logger.warning("Model filter failed for %s: %s", self.name, e)
            return raw_signal

    @abstractmethod
    def generate_signal(self, row: pd.Series, context: pd.Series | None = None) -> StrategySignal:
        raise NotImplementedError
