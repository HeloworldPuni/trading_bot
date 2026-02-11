
import numpy as np
import logging
import pandas as pd

try:
    from hmmlearn.hmm import GaussianHMM
except ImportError:
    # Fallback to GaussianMixture if hmmlearn not installed
    from sklearn.mixture import GaussianMixture as GaussianHMM
    
logger = logging.getLogger(__name__)

class HMMRegimeClassifier:
    """
    Phase 4 retrofitted: Hidden Markov Model for market regime classification.
    """
    def __init__(self, n_components: int = 2):
        self.n_components = n_components
        self.model = GaussianHMM(n_components=n_components, random_state=42)
        self.is_fitted = False

    def _reshape(self, returns: np.ndarray) -> np.ndarray:
        arr = np.asarray(returns, dtype=float)
        return arr.reshape(-1, 1)

    def fit(self, returns: np.ndarray):
        X = self._reshape(returns)
        try:
            self.model.fit(X)
            self.is_fitted = True
            logger.info("HMM Regime Model Fitted.")
        except Exception as e:
            logger.error(f"HMM Fit Failed: {e}")
            self.is_fitted = False

    def predict(self, returns: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            return np.zeros(len(returns))
        X = self._reshape(returns)
        return self.model.predict(X)

    def fit_predict(self, returns: np.ndarray) -> np.ndarray:
        self.fit(returns)
        return self.predict(returns)

    def predict_proba(self, returns: np.ndarray) -> pd.DataFrame:
        if not self.is_fitted:
            cols = [f"state_{i}" for i in range(self.n_components)]
            return pd.DataFrame(np.zeros((len(returns), self.n_components)), columns=cols)
        X = self._reshape(returns)
        try:
            probs = self.model.predict_proba(X)
        except Exception:
            # Fallback for models without predict_proba support.
            states = self.model.predict(X)
            probs = np.zeros((len(states), self.n_components))
            for i, s in enumerate(states):
                probs[i, int(s)] = 1.0
        cols = [f"state_{i}" for i in range(self.n_components)]
        return pd.DataFrame(probs, columns=cols)
