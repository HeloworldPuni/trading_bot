
import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis, jarque_bera

class DistributionAnalyzer:
    """
    Phase 3 Retrofit: Statistical Distributions.
    Analyzes skewness, kurtosis, and normality.
    """
    @staticmethod
    def analyze_returns(returns: pd.Series) -> dict:
        if len(returns) < 10:
            return {"is_normal": False}
            
        clean = returns.dropna()
        s = skew(clean)
        k = kurtosis(clean)
        jb_stat, jb_p = jarque_bera(clean)
        
        return {
            "skewness": s,
            "kurtosis": k,
            "jb_p_value": jb_p,
            "is_normal": jb_p > 0.05
        }
