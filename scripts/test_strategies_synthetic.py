import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.strategies.mean_reversion import MeanReversionStrategy
from src.features.regime import RegimeDetector

def main():
    print("Testing MeanReversionStrategy with Synthetic Data...")
    
    # 1. Create a single row of data that SHOULD trigger a Buy
    # Context: Range (Trend=0), Normal Vol (Vol=1) -> Allowed
    # Data: Close < Lower BB, RSI < 30
    
    row = pd.Series({
        'close': 100.0,
        'bb_lower': 102.0, # Close is below Lower Band
        'bb_upper': 110.0,
        'rsi': 25.0,       # Oversold
        'atr': 1.0
    })
    
    context = pd.Series({
        'trend_regime': 0, # Range
        'vol_regime': 1    # Normal
    })
    
    strat = MeanReversionStrategy()
    signal = strat.generate_signal(row, context)
    
    print(f"Scenario 1 (Perfect Buy): Signal={signal.signal} Confidence={signal.confidence:.2f}")
    
    if signal.signal == 1:
        print("PASS: Bought correctly.")
    else:
        print(f"FAIL: Did not buy. Metadata: {signal.metadata}")
        
    # 2. Test Regime Filter
    # Context: Trend (Trend=1) -> Should Block
    context_bad = pd.Series({
        'trend_regime': 1, # Trending
        'vol_regime': 1
    })
    
    signal_bad = strat.generate_signal(row, context_bad)
    print(f"Scenario 2 (Trend Filter): Signal={signal_bad.signal}")
    
    if signal_bad.signal == 0:
        print("PASS: Blocked by Regime.")
    else:
        print("FAIL: Ignored Regime Filter.")

if __name__ == "__main__":
    main()
