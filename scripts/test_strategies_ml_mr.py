import sys
import os
import pandas as pd
import numpy as np
import logging

sys.path.append(os.getcwd())

from src.strategies.mean_reversion import MeanReversionStrategy
from src.strategies.base import StrategySignal

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def main():
    print("=== Testing Strategy ML Integration (MeanReversion) ===")
    
    # 1. Instantiate Strategy
    strat = MeanReversionStrategy(rsi_buy=40, rsi_sell=60)
    
    if strat.ml_model:
        print(f"✅ ML Model Loaded: {strat.name}")
    else:
        print(f"❌ ML Model NOT Loaded for {strat.name}")
        return

    # 2. Construct a Mock Row
    row = pd.Series({
        # Technicals
        'close': 50000.0,
        'high': 51000.0,
        'low': 49000.0,
        'bb_upper': 52000.0, # Close < BB Lower for Buy
        'bb_lower': 50100.0, # Close < Lower
        'rsi': 35.0,         # < 40 -> Buy
        'funding_rate': 0.0001,
        'atr': 500.0,
        
        # Features (Phase 2)
        'vol_expansion': 1.2,
        'funding_divergence': 0.5,
        'spread_rel': 2.0,
        'ofi': 100.0,
        
        # Regimes
        'trend_regime': 0, # Range -> OK for MeanReversion
        'vol_regime': 1
    })
    
    context = pd.Series({
        'trend_regime': 0,
        'vol_regime': 1
    })
    
    # 3. Generate Signal
    # Logic: Close < BB Lower (50000 < 50100) and RSI < 40 -> Buy Signal
    
    print("\nGenerating Signal...")
    signal = strat.generate_signal(row, context)
    
    print(f"Signal: {signal.signal}")
    print(f"Confidence: {signal.confidence:.4f}")
    print(f"Metadata: {signal.metadata}")
    
    if 'ml_probability' in signal.metadata:
        print("✅ ML Filter Applied (Probability found in metadata)")
        prob = signal.metadata['ml_probability']
        print(f"Model Probability: {prob:.4f}")
    else:
        print("❌ ML Filter NOT Applied")

if __name__ == "__main__":
    main()
