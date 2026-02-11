
import numpy as np
import logging

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

    def fit(self, returns: np.ndarray):
        X = returns.reshape(-1, 1)
        try:
            self.model.fit(X)
            self.is_fitted = True
            logger.info("HMM Regime Model Fitted.")
        except Exception as e:
            logger.error(f"HMM Fit Failed: {e}")

    def predict(self, returns: np.ndarray) -> np.ndarray:
        if not self.is_fitted:
            return np.zeros(len(returns))
        X = returns.reshape(-1, 1)
        return self.model.predict(X)
