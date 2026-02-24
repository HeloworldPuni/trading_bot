import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.volatility import VolatilityEstimator
from src.features.labeler import TripleBarrierLabeler

def main():
    symbol = "BTC/USDT"
    print(f"Testing Triple Barrier Labeling for {symbol}...")
    
    store = FeatureStore(symbol)
    
    # 1. Load Data
    full_trades = store.load_trades()
    if full_trades.empty:
        print("No trade data found. Exiting.")
        return

    # 2. Resample to 1-minute bars
    bars = store.resample_trades(full_trades, rule='1min')
    close_prices = bars['close']
    print(f"Loaded {len(bars)} 1-min bars.")
    
    if len(bars) < 20:
        print("Not enough bars for volatility estimation.")
        return

    # 3. Volatility Estimation
    # Using a fast span for this short test data
    vol = VolatilityEstimator.get_daily_vol(close_prices, span=20)
    print("\nVolatility (First 5):")
    print(vol.head())
    print("\nVolatility (Last 5):")
    print(vol.tail())
    
    # 4. Triple Barrier Labeling
    # Set barriers: PT=1.0*vol, SL=1.0*vol
    # Vertical Barrier: 10 mins
    
    t_events = close_prices.index
    vertical_barriers = t_events + pd.Timedelta(minutes=10)
    
    print("\nRunning Labeler...")
    labels = TripleBarrierLabeler.get_events(
        close_prices=close_prices,
        t_events=t_events,
        pt_sl=[1.0, 1.0],
        target=vol,
        min_ret=0.00001, # very small minimum for testing
        vertical_barrier_times=pd.Series(vertical_barriers, index=t_events)
    )
    
    print("\nLabels Generated:")
    print(labels.describe())
    print(labels['label'].value_counts())
    
    # Show a few examples
    print("\nSample Events:")
    print(labels.head(10))

if __name__ == "__main__":
    main()
