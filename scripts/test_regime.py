import sys
import os
import pandas as pd
import numpy as np
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.regime import RegimeDetector
from src.features.spike_detector import SpikeDetector
from src.features.hmm_regime import HMMRegimeClassifier

def main():
    symbol = "BTC/USDT"
    print(f"Testing Regime Detection for {symbol}...\n")
    
    store = FeatureStore(symbol)
    full_trades = store.load_trades()
    ob = store.load_orderbook()
    
    if full_trades.empty or ob.empty:
        print("Data missing. Exiting.")
        return

    # 1. Resample to 5-min bars for Regime Analysis
    bars = store.resample_trades(full_trades, rule='5min')
    close = bars['close']
    high = bars['high']
    low = bars['low']
    
    print(f"Loaded {len(bars)} 5-min bars.")
    
    # --- Layer 1: Statistical Regimes ---
    print("\n--- Layer 1: Statistical Rules ---")
    
    # Volatility
    vol_regime = RegimeDetector.get_volatility_regime(close)
    print("Volatility Regime Distribution:")
    print(vol_regime.value_counts(normalize=True).sort_index())
    
    # Trend
    trend_regime = RegimeDetector.get_trend_regime(high, low, close)
    print("\nTrend Regime Distribution (1=Trend, 0=Range):")
    print(trend_regime.value_counts(normalize=True).sort_index())
    
    # Liquidity (needs orderbook, might need resampling or just snapshot check)
    # checking raw orderbook for liquidity
    liq_regime = RegimeDetector.get_liquidity_regime(ob)
    print("\nLiquidity Regime Distribution (1=Liquid, 0=Illiquid):")
    print(liq_regime.value_counts(normalize=True).sort_index())
    
    # --- Layer 2: Anomalies ---
    print("\n--- Layer 2: Spikes/News ---")
    spikes = SpikeDetector.detect_spikes(close)
    num_spikes = spikes.sum()
    print(f"Detected {num_spikes} Spikes/Shocks (> 4-sigma).")
    
    # --- Layer 3: HMM / Latent States ---
    print("\n--- Layer 3: HMM / Latent States ---")
    hmm = HMMRegimeClassifier(n_components=2)
    
    # Determine returns
    rets = np.log(close / close.shift(1)).dropna()
    
    try:
        states = hmm.fit_predict(rets)
        states = pd.Series(states, index=rets.index) # Re-align
        print("HMM State Distribution:")
        print(states.value_counts(normalize=True).sort_index())
        
        # Check volatility of each state to identify which is which
        vol_0 = rets[states == 0].std()
        vol_1 = rets[states == 1].std()
        print(f"\nState 0 Volatility: {vol_0:.5f}")
        print(f"State 1 Volatility: {vol_1:.5f}")
        
    except Exception as e:
        print(f"HMM Failed: {e}")

if __name__ == "__main__":
    main()
