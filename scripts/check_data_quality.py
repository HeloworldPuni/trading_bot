import os
import csv
import time
from datetime import datetime
from typing import List, Dict
import sys

# Add project root to path
sys.path.append(os.getcwd())

from src.config import Config
from src.data.quality import validate_orderbook

def check_data_quality():
    raw_dir = os.path.join(Config.DATA_PATH, "raw")
    if not os.path.exists(raw_dir):
        print(f"No data found in {raw_dir}")
        return

    print(f"\n{'='*60}")
    print(f"DATA QUALITY REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    symbols = [d for d in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, d))]
    
    for symbol in symbols:
        print(f"\n>>> SYMBOL: {symbol}")
        symbol_path = os.path.join(raw_dir, symbol)
        
        # Check Orderbooks
        _check_category(symbol, symbol_path, "orderbook", check_l2_integrity=True)
        
        # Check Trades
        _check_category(symbol, symbol_path, "trades")
        
        # Check Open Interest
        _check_category(symbol, symbol_path, "open_interest")

def _check_category(symbol, base_path, category, check_l2_integrity=False):
    cat_path = os.path.join(base_path, category)
    if not os.path.exists(cat_path):
        print(f"  [{category:15s}] MISSING DIRECTORY")
        return

    files = sorted([f for f in os.listdir(cat_path) if f.endswith('.csv')])
    if not files:
        print(f"  [{category:15s}] NO DATA FILES")
        return

    latest_file = os.path.join(cat_path, files[-1])
    
    # Analyze Latency & Gaps
    timestamps = []
    rows = []
    
    # Timestamp index depends on category
    ts_idx = 1 if category == "trades" else 0
    
    try:
        with open(latest_file, 'r') as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if row:
                    # Timestamp is always first column
                    timestamps.append(int(float(row[ts_idx]))) 
                    if check_l2_integrity:
                        rows.append(row)
    except Exception as e:
        print(f"  [{category:15s}] ERROR READING FILE: {e}")
        return

    if not timestamps:
        print(f"  [{category:15s}] EMPTY FILE")
        return

    count = len(timestamps)
    last_ts = timestamps[-1]
    now_ms = time.time() * 1000
    age_sec = (now_ms - last_ts) / 1000.0
    
    # Calculate intervals
    intervals = []
    for i in range(1, len(timestamps)):
        diff =(timestamps[i] - timestamps[i-1]) / 1000.0
        intervals.append(diff)
    
    avg_interval = (sum(intervals) / len(intervals)) if intervals else 0.0
    max_gap = max(intervals) if intervals else 0.0
    
    status = "OK"
    if age_sec > 60: status = "STALE"
    if max_gap > 30: status = "GAPS"
    
    print(f"  [{category:15s}] {status:5s} | Count: {count:4d} | Age: {age_sec:5.1f}s | Avg Interval: {avg_interval:4.2f}s | Max Gap: {max_gap:4.1f}s")
    
    # Deep Check for L2
    if check_l2_integrity and rows:
        issues_found = 0
        for i, row in enumerate(rows[-10:]): # Check last 10 rows
            # Parse bids/asks
            # Format: ts, b1p, b1v, a1p, a1v...
            try:
                bids = []
                asks = []
                # indices: 1,2 (bid1), 3,4 (ask1), 5,6 (bid2)...
                # Wait, my ingestor format is: ts, b1p, b1v, a1p, a1v, b2p, b2v, a2p, a2v...
                # Actually, ingestor code:
                # row.extend([bids[i][0], bids[i][1]])
                # row.extend([asks[i][0], asks[i][1]])
                # So for depth=5, we have 5 iterations.
                # headers: bid1_p, bid1_v, ask1_p, ask1_v...
                
                # Let's just check best bid vs best ask
                b1_p = float(row[1])
                a1_p = float(row[3])
                
                if b1_p >= a1_p and b1_p > 0 and a1_p > 0:
                     print(f"      [WARN] Crossed Book at row {len(timestamps)-10+i}: Bid {b1_p} >= Ask {a1_p}")
                     issues_found += 1
            except:
                pass
        
        if issues_found == 0 and check_l2_integrity:
             print(f"      [INTEGRITY] Last 10 snapshots verified (No Crossed Books).")

if __name__ == "__main__":
    check_data_quality()
