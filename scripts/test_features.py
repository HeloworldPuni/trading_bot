import sys
import os
import pandas as pd
sys.path.append(os.getcwd())

from src.features.store import FeatureStore
from src.features.microstructure import MicrostructureFeatures

def main():
    symbol = "BTC/USDT"
    print(f"Testing Feature Engineering for {symbol}...")
    
    store = FeatureStore(symbol)
    
    # 1. Load Trades
    print("\n1. Loading Trades...")
    trades_df = store.load_trades()
    print(f"Loaded {len(trades_df)} trades.")
    if not trades_df.empty:
        print(trades_df.tail())
        
        # 2. Resample
        print("\n2. Resampling to 5s bars...")
        bars = store.resample_trades(trades_df, rule='5s')
        print(f"Generated {len(bars)} bars.")
        print(bars.head())
        
        # 3. Compute TFI
        print("\n3. Computing Trade Flow Imbalance (TFI)...")
        tfi = MicrostructureFeatures.calc_tfi(bars)
        print(tfi.describe())
        
        # 4. Compute VPIN
        print("\n4. Computing VPIN...")
        vpin = MicrostructureFeatures.calc_vpin(bars, window=10)
        print(vpin.describe())
        
    else:
        print("Skipping Trade features (no data).")

    # 5. Load Orderbook (if exists)
    print("\n5. Loading Orderbook...")
    ob_df = store.load_orderbook()
    print(f"Loaded {len(ob_df)} snapshots.")
    
    # 6. Compute OFI (Requires specific columns)
    # Our ingestor saves: bid1_p, bid1_v, ask1_p, ask1_v...
    # The calc_ofi method expects these or similar.
    # Let's check columns first.
    if not ob_df.empty:
        print(f"Columns: {ob_df.columns.tolist()}")
        # We need to ensure columns match what calc_ofi expects
        # microstructure.py uses: bid1_p, bid1_v... which matches ingestor.
        
        print("\n6. Computing Order Flow Imbalance (OFI)...")
        # Since OFI needs high frequency, we might not resample yet, or resample to 100ms?
        # For now, let's run on raw snapshots.
        ofi = MicrostructureFeatures.calc_ofi(ob_df)
        print(ofi.describe())
        
        print("\n7. Computing Spread Metrics...")
        spread_df = MicrostructureFeatures.calc_spread(ob_df)
        print(spread_df.describe())
        
    else:
        print("Skipping Orderbook features (no data).")

if __name__ == "__main__":
    main()
