import sys
import os
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

sys.path.append(os.getcwd())
from src.features.store import Config

def main():
    print("Forcing TrendFollowing Model Training (Synthetic Data)...")
    
    # 1. Create Synthetic Data (X, y)
    # 100 samples, 16 features
    np.random.seed(42)
    X = pd.DataFrame(np.random.rand(100, 16), columns=[
        'ema_20', 'ema_50', 'adx', 'bb_upper', 'bb_lower', 'rsi', 'funding_rate', 'atr',
        'vol_expansion', 'funding_divergence', 'spread_rel', 'ofi', 'trend_regime', 'vol_regime',
        'feature_1', 'feature_2' 
    ])
    
    # Target: Mixed 0 and 1
    y = pd.Series(np.random.randint(0, 2, 100))
    
    # 2. Train Model
    clf = RandomForestClassifier(n_estimators=10, max_depth=3, random_state=42)
    clf.fit(X, y)
    
    # 3. Save Model
    model_path = os.path.join("models", "TrendFollowing.joblib")
    import joblib
    joblib.dump(clf, model_path)
    print(f"Saved synthetic model to {model_path}")

if __name__ == "__main__":
    main()
