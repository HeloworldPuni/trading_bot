import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.volatility import VolatilityEstimator
from src.features.labeler import TripleBarrierLabeler
from src.features.meta_labeling import MetaLabeler

def main():
    symbol = "BTC/USDT"
    print(f"Testing Phase 3: Full Labeling Pipeline for {symbol}...")
    
    store = FeatureStore(symbol)
    full_trades = store.load_trades()
    if full_trades.empty:
        print("No trades found.")
        return
        
    # 1. Resample
    bars = store.resample_trades(full_trades, rule='1min')
    close_prices = bars['close']
    print(f"Loaded {len(bars)} bars.")
    
    if len(bars) < 50:
        print("Not enough data.")
        return

    # 2. Volatility
    vol = VolatilityEstimator.get_daily_vol(close_prices, span=20)
    
    # 3. Triple Barrier
    t_events = close_prices.index
    vertical_barriers = t_events + pd.Timedelta(minutes=10)
    
    # Hypothsis: We are a trend following strategy always betting LONG
    # So we want to know: "If we go LONG here, do we win?"
    
    print("\nRunning Labeler...")
    labels = TripleBarrierLabeler.get_events(
        close_prices=close_prices,
        t_events=t_events,
        pt_sl=[1.0, 1.0],
        target=vol,
        min_ret=0.00001,
        vertical_barrier_times=pd.Series(vertical_barriers, index=t_events)
    )
    
    print("Events found:", len(labels))
    
    # 4. Meta-Labeling
    # Adding a 'side' column to simulate primary model
    # Let's say we are betting Long (1)
    labels['side'] = 1
    
    print("\nApplying Meta-Labeling...")
    meta_labels = MetaLabeler.get_meta_labels(labels, close_prices)
    
    print("\nMeta-Labels (First 10):")
    print(meta_labels.head(10))
    
    print("\nValue Counts:")
    print(meta_labels['bin'].value_counts())
    
    print("\nAvg realized return for bin=1:", meta_labels[meta_labels['bin']==1]['ret'].mean())
    print("Avg realized return for bin=0:", meta_labels[meta_labels['bin']==0]['ret'].mean())

if __name__ == "__main__":
    main()
