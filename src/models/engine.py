import os

import pandas as pd


class StrategyModel:
    def __init__(self, name: str):
        self.name = name
        self.model = None
        self.feature_cols = []
        self.path = os.path.join("models", f"{name}.joblib")

    def _init_model(self):
        try:
            from sklearn.ensemble import RandomForestClassifier

            return RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced")
        except Exception:
            return None

    def train(self, X: pd.DataFrame, y: pd.Series):
        self.model = self._init_model()
        if self.model is None:
            raise RuntimeError("scikit-learn is required to train strategy models.")
        self.feature_cols = list(X.columns)
        self.model.fit(X[self.feature_cols], y)

    def predict_proba(self, row: pd.Series) -> float:
        if self.model is None:
            return 0.5
        x = pd.DataFrame([row.to_dict()])
        for col in self.feature_cols:
            if col not in x.columns:
                x[col] = 0.0
        x = x[self.feature_cols]
        return float(self.model.predict_proba(x)[0][1])

    def save(self):
        if self.model is None:
            return
        os.makedirs("models", exist_ok=True)
        import joblib

        joblib.dump({"model": self.model, "feature_cols": self.feature_cols}, self.path)

    def load(self):
        if not os.path.exists(self.path):
            return False
        import joblib

        data = joblib.load(self.path)
        self.model = data.get("model", data)
        self.feature_cols = data.get("feature_cols", [])
        return True
