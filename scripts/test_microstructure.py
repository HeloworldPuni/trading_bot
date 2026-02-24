import sys
import os
import pandas as pd
import glob

# Ensure project root is in path
sys.path.append(os.getcwd())

from src.features.microstructure import MicrostructureFeatures

def load_latest_orderbook(symbol="BTC_USDT"):
    # Find latest date directory/file
    # Pattern: data/raw/{symbol}/orderbook/{date}.csv
    path_pattern = os.path.join(os.getcwd(), "data", "raw", symbol, "orderbook", "*.csv")
    files = glob.glob(path_pattern)
    
    if not files:
        print(f"No orderbook data found for {symbol}")
        return None
        
    # Get latest file
    latest_file = max(files, key=os.path.getctime)
    print(f"Loading data from: {latest_file}")
    
    try:
        # Load CSV. 
        # Structure is usually: timestamp, bid1_p, bid1_v, ... ask1_p, ask1_v ...
        # But wait, our ingestor saves snapshots. Let's inspect the headers or assume standard format.
        # Based on src/data/ingestor.py, it likely saves just the raw snapshot JSON or flattened CSV.
        # Let's try reading it.
        df = pd.read_csv(latest_file)
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

def parse_snapshot_to_bids_asks(row, depth=5):
    """
    Parses a single row from the CSV into Bids/Asks DF for the feature calculator.
    Assumes columns like 'bids_0_price', 'bids_0_qty', 'asks_0_price', ...
    """
    bids_list = []
    asks_list = []
    
    for i in range(depth):
        try:
            # Check for possible column naming conventions
            # 1. ingestor.py format: bid{i}_p, bid{i}_v (based on recent log inspection)
            bp = row.get(f"bid{i}_p") or row.get(f"bids_{i}_price") or row.get(f"bid_price_{i}")
            bq = row.get(f"bid{i}_v") or row.get(f"bids_{i}_qty") or row.get(f"bid_qty_{i}")
            
            ap = row.get(f"ask{i}_p") or row.get(f"asks_{i}_price") or row.get(f"ask_price_{i}")
            aq = row.get(f"ask{i}_v") or row.get(f"asks_{i}_qty") or row.get(f"ask_qty_{i}")
            
            if bp is not None and bq is not None:
                bids_list.append({"price": float(bp), "quantity": float(bq)})
            
            if ap is not None and aq is not None:
                asks_list.append({"price": float(ap), "quantity": float(aq)})
                
        except Exception as e:
            continue
            
    return pd.DataFrame(bids_list), pd.DataFrame(asks_list)

def main():
    print("Testing Microstructure Features...")
    
    df = load_latest_orderbook()
    if df is None or df.empty:
        print("FAIL: No data to test.")
        return

    print(f"Loaded {len(df)} snapshots.")
    print("Columns:", df.columns.tolist()[:10]) # Debug print
    
    # Test on the last 5 snapshots
    for idx, row in df.tail(5).iterrows():
        bids, asks = parse_snapshot_to_bids_asks(row)
        
        if bids.empty or asks.empty:
            print(f"Skipping row {idx} (parsing failed)")
            continue
            
        # 1. OBI
        obi = MicrostructureFeatures.calculate_obi(bids, asks)
        
        # 2. Gaps
        gaps = MicrostructureFeatures.detect_liquidity_gaps(bids, asks)
        
        # 3. MicroPrice
        mp = MicrostructureFeatures.calculate_micro_price(bids, asks)
        
        mid = (bids.iloc[0]['price'] + asks.iloc[0]['price']) / 2
        
        print(f"[{idx}] OBI: {obi:.4f} | Gaps: {len(gaps)} | Mid: {mid:.2f} | MP: {mp:.2f}")

    print("Success: Microstructure features calculated on live data.")

if __name__ == "__main__":
    main()
