
import pandas as pd
import numpy as np
import logging
from typing import List, Dict
from sklearn.feature_selection import mutual_info_regression

logger = logging.getLogger(__name__)

class FeatureSelector:
    """
    Phase 6 Retrofit: Feature Selection.
    Uses Mutual Information to select top predictive features.
    """
    def __init__(self, top_k: int = 10):
        self.top_k = top_k
        self.selected_features: List[str] = []
        self.feature_scores: Dict[str, float] = {}

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """
        Fits feature selector on training data.
        """
        if X.empty or y.empty:
            logger.warning("FeatureSelector: Empty data for fit.")
            return

        # Ensure numeric
        X_numeric = X.select_dtypes(include=[np.number]).fillna(0)
        
        # Calculate scores
        # Using mutual_info_regression for continuous target (e.g. returns)
        # If classification, use mutual_info_classif
        try:
            scores = mutual_info_regression(X_numeric, y, random_state=42)
            
            self.feature_scores = {
                feat: score for feat, score in zip(X_numeric.columns, scores)
            }
            
            # Select top K
            sorted_feats = sorted(self.feature_scores.items(), key=lambda x: x[1], reverse=True)
            self.selected_features = [f[0] for f in sorted_feats[:self.top_k]]
            
            logger.info(f"Selected Top {self.top_k} Features: {self.selected_features}")
            
        except Exception as e:
            logger.error(f"Feature Selection Failed: {e}")
            self.selected_features = list(X_numeric.columns[:self.top_k])

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        if not self.selected_features:
            return X
            
        valid_feats = [f for f in self.selected_features if f in X.columns]
        return X[valid_feats]
