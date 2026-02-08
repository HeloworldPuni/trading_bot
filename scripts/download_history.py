import sys
import os
import csv
import ccxt
import time
from datetime import datetime, timedelta

# Add parent dir to path to import Config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import Config

# Setup
EXCHANGE = ccxt.binance({
    'apiKey': Config.EXCHANGE_API_KEY,
    'secret': Config.EXCHANGE_SECRET,
    'enableRateLimit': True,
    'options': {'defaultType': 'future'}
})

TIMEFRAME = '1h'
LIMIT = 1000

def download_symbol(symbol: str, start_year: int, end_year: int):
    print(f"Starting download for {symbol} ({start_year}-{end_year})...")
    
    start_dt = datetime(start_year, 1, 1)
    end_dt = datetime(end_year, 12, 31, 23, 59, 59)
    # Ensure we don't go into future (if 2026 is future, cap at Now)
    if end_dt > datetime.now():
        end_dt = datetime.now()
        
    start_ts = int(start_dt.timestamp() * 1000)
    end_ts = int(end_dt.timestamp() * 1000)
    
    filename = f"data/{symbol.replace('/', '_')}_{start_year}_{end_year}.csv"
    os.makedirs("data", exist_ok=True)
    
    all_candles = []
    current_since = start_ts
    
    while current_since < end_ts:
        print(f"Fetching from {datetime.fromtimestamp(current_since/1000)}...")
        try:
            ohlcv = EXCHANGE.fetch_ohlcv(symbol, TIMEFRAME, since=current_since, limit=LIMIT)
            if not ohlcv:
                print("No more data received.")
                break
            
            all_candles.extend(ohlcv)
            current_since = ohlcv[-1][0] + 1 # Next ms
            
            # Rate limit politeness
            time.sleep(0.5)
            
            if current_since >= end_ts:
                break
                
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5) # Backoff
            
    # Filter by strictly within range (fetch_ohlcv might overshoot slightly)
    # Actually logic handles since.. so it just keeps going.
    
    print(f"Saving {len(all_candles)} candles to {filename}...")
    
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for candle in all_candles:
            writer.writerow(candle)
            
    print("Download Complete.")

if __name__ == "__main__":
    # Define Targets
    targets = [
        ("BTC/USDT", 2020, 2026),
        ("ETH/USDT", 2020, 2026),
        ("SOL/USDT", 2020, 2026)
    ]
    
    for sym, start, end in targets:
        download_symbol(sym, start, end)
