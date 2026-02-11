
import numpy as np
import logging
from typing import Dict, Any, List
from scipy.stats import ks_2samp

logger = logging.getLogger(__name__)

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

            # Run KS Test if we have enough data
            if len(self.current_data[feature]) >= 30 and len(self.reference_data[feature]) >= 30:
                try:
                    stat, p_value = ks_2samp(self.reference_data[feature], self.current_data[feature])
                    if p_value < self.threshold:
                        drift_flags[feature] = True
                        logger.warning(f"Drift detected in {feature} (p={p_value:.4f})")
                    else:
                        drift_flags[feature] = False
                except Exception:
                    pass
                    
        return drift_flags
