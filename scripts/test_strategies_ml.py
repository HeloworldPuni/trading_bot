import sys
import os
import pandas as pd
import numpy as np
import logging

sys.path.append(os.getcwd())

from src.strategies.trend import TrendFollowingStrategy
from src.strategies.base import StrategySignal

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    print("=== Testing Strategy ML Integration ===")
    
    # 1. Instantiate Strategy
    # Using the lower threshold used in training to ensure signal generation logic triggers
    strat = TrendFollowingStrategy(adx_threshold=10)
    
    if strat.ml_model:
        print(f"✅ ML Model Loaded: {strat.name}")
    else:
        print(f"❌ ML Model NOT Loaded for {strat.name}")
        return

    # 2. Construct a Mock Row with ALL features expected by the model
    # Model expects: Technicals + Phase 2 Features + Regimes
    
    row = pd.Series({
        # Technicals (from dataset.py _add_technical_indicators)
        'close': 50000.0,
        'high': 51000.0,
        'low': 49000.0,
        'ema_20': 50100.0,
        'ema_50': 49000.0, # Fast > Slow -> Bullish
        'adx': 40.0,       # > 10 -> Strong Trend
        'bb_upper': 52000.0,
        'bb_lower': 48000.0,
        'rsi': 60.0,
        'funding_rate': 0.0001,
        'atr': 500.0,
        
        # Phase 2 Features (Joined in dataset.py)
        'vol_expansion': 1.2,
        'funding_divergence': 0.5,
        'spread_rel': 2.0,
        'ofi': 100.0,
        
        # Regimes (Indices joined in dataset.py, usually passed as context but also in X)
        # Wait, dataset.py adds trend_regime/vol_regime to X.
        # apply_model_filter passes 'features' (row).
        # So row MUST have trend_regime and vol_regime IF they were in X.
        'trend_regime': 1,
        'vol_regime': 1
    })
    
    context = pd.Series({
        'trend_regime': 1,
        'vol_regime': 1
    })
    
    # 3. Generate Signal
    # This should:
    # a) Check Context (Trend=1 -> OK)
    # b) Check Logic (EMA Fast > Slow + ADX > 10 -> Signal 1)
    # c) Call apply_model_filter -> usage of ML Model
    
    print("\nGenerating Signal...")
    signal = strat.generate_signal(row, context)
    
    print(f"Signal: {signal.signal}")
    print(f"Confidence: {signal.confidence:.4f}")
    print(f"Metadata: {signal.metadata}")
    
    if 'ml_probability' in signal.metadata:
        print("✅ ML Filter Applied (Probability found in metadata)")
        prob = signal.metadata['ml_probability']
        print(f"Model Probability: {prob:.4f}")
        
        # Verify
        # Manual prediction
        # We need to reshape row to DataFrame for predict_proba
        # And ensure columns match exactly (order might matter for RandomForest?)
        # sklearn RF usually cares about feature order/names.
        # StrategyModel.predict_proba handles Series -> DataFrame.T conversion.
        # But if column order is different from X_train, it might be wrong if feature_names_in_ is checked.
        # recent sklearn checks names.
    else:
        print("❌ ML Filter NOT Applied")

if __name__ == "__main__":
    main()
