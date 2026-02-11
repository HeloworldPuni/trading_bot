import logging
from typing import Any, Dict, List

import numpy as np

logger = logging.getLogger(__name__)

try:
    from scipy.stats import ks_2samp
    HAS_SCIPY = True
except Exception as exc:  # pragma: no cover - environment dependent
    ks_2samp = None
    HAS_SCIPY = False
    logger.warning("scipy unavailable for KS drift test; using z-score fallback: %s", exc)

class DriftDetector:
    """
    Phase 10 Retrofit: Data Drift Detection.
    Uses Kolmogorov-Smirnov (KS) test to detect shifts in feature distributions.
    """
    def __init__(self, reference_window: int = 500, current_window: int = 100, p_value_threshold: float = 0.05):
        self.reference_data: Dict[str, List[float]] = {}
        self.current_data: Dict[str, List[float]] = {}
        self.reference_window = reference_window
        self.current_window = current_window
        self.threshold = p_value_threshold

    def update(self, feature_vector: Dict[str, float]) -> Dict[str, bool]:
        """
        Updates sliding windows and checks for drift.
        Returns a dict of flagged features (True = Drift Detected).
        """
        drift_flags = {}
        
        for feature, value in feature_vector.items():
            if not isinstance(value, (int, float)):
                continue

            # Initialize lists
            if feature not in self.reference_data:
                self.reference_data[feature] = []
                self.current_data[feature] = []

            # Update Reference Window (Fixed or Rolling - here Rolling for simplicity)
            self.reference_data[feature].append(value)
            if len(self.reference_data[feature]) > self.reference_window:
                self.reference_data[feature].pop(0)

            # Update Current Window
            self.current_data[feature].append(value)
            if len(self.current_data[feature]) > self.current_window:
                self.current_data[feature].pop(0)

            # Run drift test if we have enough data
            if len(self.current_data[feature]) >= 30 and len(self.reference_data[feature]) >= 30:
                try:
                    if HAS_SCIPY and ks_2samp is not None:
                        _, p_value = ks_2samp(self.reference_data[feature], self.current_data[feature])
                        if p_value < self.threshold:
                            drift_flags[feature] = True
                            logger.warning(f"Drift detected in {feature} (p={p_value:.4f})")
                        else:
                            drift_flags[feature] = False
                    else:
                        ref = np.array(self.reference_data[feature], dtype=float)
                        cur = np.array(self.current_data[feature], dtype=float)
                        ref_std = float(np.std(ref))
                        if ref_std <= 1e-12:
                            drift_flags[feature] = False
                        else:
                            z = abs(float(np.mean(cur) - np.mean(ref)) / ref_std)
                            drift_flags[feature] = z >= 3.0
                            if drift_flags[feature]:
                                logger.warning("Drift detected in %s (fallback z=%.2f)", feature, z)
                except Exception:
                    pass
                    
        return drift_flags


class DriftMonitor:
    """
    Backward-compatible real-time drift monitor used by main.py.
    Uses rolling z-score alerts per numeric feature.
    """
    def __init__(self, window: int = 200, alert_z: float = 3.0):
        self.window = max(20, int(window))
        self.alert_z = float(alert_z)
        self.history: Dict[str, List[float]] = {}

    def update(self, feature_vector: Dict[str, Any]) -> List[str]:
        alerts: List[str] = []

        for feature, value in feature_vector.items():
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                continue

            series = self.history.setdefault(feature, [])
            series.append(float(value))
            if len(series) > self.window:
                series.pop(0)

            if len(series) < max(30, self.window // 4):
                continue

            baseline = np.array(series[:-1], dtype=float)
            current = float(series[-1])
            std = float(np.std(baseline))
            if std <= 1e-12:
                continue

            mean = float(np.mean(baseline))
            z = abs((current - mean) / std)
            if z >= self.alert_z:
                alerts.append(f"{feature} z={z:.2f}")

        return alerts
