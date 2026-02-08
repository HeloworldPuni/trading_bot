
import logging
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
import joblib
import os
import json

logger = logging.getLogger(__name__)

class PolicyEvaluator:
    def __init__(self, model_path: str):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found: {model_path}")
        self.model = joblib.load(model_path)
        self.feature_cols = [
            "market_regime", "volatility_level", "trend_strength",
            "dist_to_high", "dist_to_low", "trading_session",
            "symbol", "repeats", "current_open_positions",
            "action_taken"
        ]
        self.target_col = "decision_quality"

    def evaluate(self, test_df: pd.DataFrame) -> dict:
        """
        Evaluates the model on test data and returns a report.
        """
        X_test = test_df[self.feature_cols]
        y_test = test_df[self.target_col]

        logger.info(f"Evaluating model on {len(X_test)} rows...")

        # Predictions
        preds = self.model.predict(X_test)
        probs = self.model.predict_proba(X_test)[:, 1]

        # Basic Metrics
        acc = accuracy_score(y_test, preds)
        auc = roc_auc_score(y_test, probs)
        
        # Confusion Matrix
        tn, fp, fn, tp = confusion_matrix(y_test, preds).ravel()

        # Feature Importance - handle both XGBoost and LightGBM
        importance = {}
        if hasattr(self.model, 'get_booster'):
            # XGBoost
            importance = self.model.get_booster().get_score(importance_type='gain')
        elif hasattr(self.model, 'feature_importances_'):
            # LightGBM, sklearn, or any model with feature_importances_
            for i, imp in enumerate(self.model.feature_importances_):
                col_name = self.feature_cols[i] if i < len(self.feature_cols) else f"f{i}"
                importance[col_name] = float(imp)
        sorted_importance = sorted(importance.items(), key=lambda x: x[1], reverse=True)

        report = {
            "metrics": {
                "test_accuracy": float(acc),
                "test_roc_auc": float(auc),
                "confusion_matrix": {
                    "tn": int(tn),
                    "fp": int(fp),
                    "fn": int(fn),
                    "tp": int(tp)
                }
            },
            "feature_importance": {name: float(val) for name, val in sorted_importance}
        }

        return report

    def save_report(self, report: dict, path: str):
        """
        Saves the evaluation report to a JSON file.
        """
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        logger.info(f"Report saved to {path}")
