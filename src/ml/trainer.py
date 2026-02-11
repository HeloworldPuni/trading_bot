
import logging
import pandas as pd
import xgboost as xgb
import lightgbm as lgb
from sklearn.metrics import accuracy_score, roc_auc_score
import joblib
import os
import optuna
from sklearn.linear_model import LogisticRegression

logger = logging.getLogger(__name__)

class PolicyTrainer:
    def __init__(self, model_type="xgboost", **kwargs):
        self.model_type = model_type.lower()
        self.params = kwargs
        
        # Default Params if empty
        if not self.params:
            if self.model_type == "xgboost":
                self.params = {
                    "max_depth": 4,
                    "learning_rate": 0.05,
                    "n_estimators": 200,
                    "subsample": 0.8,
                    "colsample_bytree": 0.8,
                    "eval_metric": "logloss",
                    "random_state": 42
                }
            elif self.model_type == "lightgbm":
                self.params = {
                    "max_depth": 4,
                    "learning_rate": 0.05,
                    "n_estimators": 200,
                    "subsample": 0.8,
                    "colsample_bytree": 0.8,
                    "objective": "binary",
                    "metric": "auc",
                    "verbose": -1,
                    "random_state": 42
                }
        
        self.model = self._init_model()
        self.calibrator = None
        
        self.feature_cols = [
            "market_regime", "volatility_level", "trend_strength",
            "dist_to_high", "dist_to_low", 
            "macd", "macd_signal", "macd_hist",
            "bb_upper", "bb_lower", "bb_mid", "atr", "volume_delta",
            "spread_pct", "body_pct", "gap_pct", "volume_zscore", "liquidity_proxy",
            "htf_trend_spread", "htf_rsi", "htf_atr",
            "trading_session", "symbol", "repeats", "current_open_positions",
            "action_taken", "regime_confidence", "regime_stable", "momentum_shift_score"
        ]
        self.target_col = "decision_quality"

    def _init_model(self):
        if self.model_type == "xgboost":
            return xgb.XGBClassifier(**self.params)
        elif self.model_type == "lightgbm":
            return lgb.LGBMClassifier(**self.params)
        else:
            raise ValueError(f"Unsupported model type: {self.model_type}")

    def train(self, train_df: pd.DataFrame, val_df: pd.DataFrame):
        """
        Trains the selected model and calculates metrics.
        """
        X_train = train_df[self.feature_cols]
        y_train = train_df[self.target_col]
        X_val = val_df[self.feature_cols]
        y_val = val_df[self.target_col]

        logger.info(f"Training {self.model_type} on {len(X_train)} rows...")
        
        if self.model_type == "xgboost":
            # Auto-balance classes if unbalanced (Winners are usually majority in strategy-filtered data)
            pos_count = sum(y_train == 1)
            neg_count = sum(y_train == 0)
            if pos_count > 0 and neg_count > 0:
                # scale_pos_weight = total_negative_examples / total_positive_examples
                balance_weight = neg_count / pos_count
                self.model.set_params(scale_pos_weight=balance_weight)
                logger.info(f"XGBoost: Applied scale_pos_weight={balance_weight:.4f} (Pos:{pos_count}, Neg:{neg_count})")
            
            self.model.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
        else:
            self.model.fit(X_train, y_train, eval_set=[(X_val, y_val)])

        # Predictions
        train_preds = self.model.predict(X_train)
        val_preds = self.model.predict(X_val)
        val_probs = self.model.predict_proba(X_val)[:, 1]

        # Metrics
        train_acc = accuracy_score(y_train, train_preds)
        val_acc = accuracy_score(y_val, val_preds)
        val_auc = roc_auc_score(y_val, val_probs)

        metrics = {
            "train_accuracy": train_acc,
            "validation_accuracy": val_acc,
            "validation_roc_auc": val_auc
        }

        # Probability calibration (Platt scaling on validation probabilities)
        try:
            calib = LogisticRegression(solver="lbfgs")
            calib.fit(val_probs.reshape(-1, 1), y_val)
            self.calibrator = calib
            logger.info("Probability calibration fitted (Platt scaling).")
        except Exception as e:
            logger.warning(f"Calibration skipped: {e}")

        logger.info(f"Training Results ({self.model_type}): {metrics}")
        return metrics

    def optimize(self, train_df: pd.DataFrame, val_df: pd.DataFrame, n_trials=30):
        """
        Runs an Optuna study to find the best hyper-parameters.
        """
        X_train = train_df[self.feature_cols]
        y_train = train_df[self.target_col]
        X_val = val_df[self.feature_cols]
        y_val = val_df[self.target_col]

        def objective(trial):
            if self.model_type == "xgboost":
                params = {
                    "max_depth": trial.suggest_int("max_depth", 3, 10),
                    "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
                    "n_estimators": trial.suggest_int("n_estimators", 100, 500),
                    "subsample": trial.suggest_float("subsample", 0.6, 0.9),
                    "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 0.9),
                    "eval_metric": "logloss",
                    "random_state": 42
                }
                # Include balancing in optimization
                pos_count = sum(y_train == 1)
                neg_count = sum(y_train == 0)
                if pos_count > 0 and neg_count > 0:
                    params["scale_pos_weight"] = neg_count / pos_count
                
                model = xgb.XGBClassifier(**params)
            elif self.model_type == "lightgbm":
                params = {
                    "max_depth": trial.suggest_int("max_depth", 3, 10),
                    "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3, log=True),
                    "n_estimators": trial.suggest_int("n_estimators", 100, 500),
                    "subsample": trial.suggest_float("subsample", 0.6, 0.9),
                    "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 0.9),
                    "num_leaves": trial.suggest_int("num_leaves", 20, 150),
                    "objective": "binary",
                    "metric": "auc",
                    "verbose": -1,
                    "random_state": 42
                }
                model = lgb.LGBMClassifier(**params)
            
            model.fit(X_train, y_train)
            val_probs = model.predict_proba(X_val)[:, 1]
            return roc_auc_score(y_val, val_probs)

        logger.info(f"Starting {self.model_type} optimization ({n_trials} trials)...")
        study = optuna.create_study(direction="maximize")
        study.optimize(objective, n_trials=n_trials)

        logger.info(f"Optimization finished. Best AUC: {study.best_value:.4f}")
        self.params.update(study.best_params)
        self.model = self._init_model()
        
        return study.best_params

    def save_model(self, path: str):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        save_data = {
            "model": self.model,
            "model_type": self.model_type,
            "params": self.params,
            "feature_cols": self.feature_cols,
            "calibrator": self.calibrator
        }
        joblib.dump(save_data, path)
        logger.info(f"Model ({self.model_type}) saved to {path}")

    def load_model(self, path: str):
        if os.path.exists(path):
            data = joblib.load(path)
            if isinstance(data, dict) and "model" in data:
                self.model = data["model"]
                self.model_type = data.get("model_type", "xgboost")
                self.params = data.get("params", {})
                self.feature_cols = data.get("feature_cols", self.feature_cols)
                self.calibrator = data.get("calibrator")
            else:
                self.model = data
            logger.info(f"Model ({self.model_type}) loaded from {path}")
        else:
            logger.error(f"Model file not found: {path}")
