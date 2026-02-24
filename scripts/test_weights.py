import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.volatility import VolatilityEstimator
from src.features.labeler import TripleBarrierLabeler
from src.features.weights import SampleWeights

def main():
    symbol = "BTC/USDT"
    print(f"Testing Sample Weights for {symbol}...")
    
    store = FeatureStore(symbol)
    
    # 1. Load Data
    full_trades = store.load_trades() 
    if full_trades.empty:
        print("No trade data found. Exiting.")
        return

    # 2. Resample (1 min)
    bars = store.resample_trades(full_trades, rule='1min')
    close_prices = bars['close']
    
    if len(bars) < 20:
        print("Not enough bars.")
        return

    # 3. Get Volatility
    vol = VolatilityEstimator.get_daily_vol(close_prices, span=20)
    
    # 4. Generate overlapping events (Triple Barrier)
    # Long vertical barrier to force overlaps -> 60 mins
    t_events = close_prices.index
    vertical_barriers = t_events + pd.Timedelta(minutes=60)
    
    print("\nRunning Labeler (High Overlap)...")
    labels = TripleBarrierLabeler.get_events(
        close_prices=close_prices,
        t_events=t_events,
        pt_sl=[1.0, 1.0],
        target=vol,
        min_ret=0.00001,
        vertical_barrier_times=pd.Series(vertical_barriers, index=t_events)
    )
    
    if labels.empty:
        print("No labels generated.")
        return
        
    print(f"Generated {len(labels)} events.")
    
    # 5. Compute Weights
    print("\nComputing Weights...")
    # t1 is the Series of end-times from labels
    t1 = labels['t1']
    
    weights = SampleWeights.get_sample_weights(t1, close_prices.index)
    
    print("\nWeights Stats:")
    print(weights.describe())
    
    # Check correlation between concurrency and weight
    # High concurrency (overlap) should mean low weight
    
    # Let's see some examples
    print("\nSample Weights (Head):")
    print(weights.head())
    
    low_weight_count = len(weights[weights < 1.0])
    print(f"\nSamples with weight < 1.0: {low_weight_count} (Should be many if overlapping)")

if __name__ == "__main__":
    main()
