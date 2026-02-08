import json
import os

LOG_FILE = 'data/experience_log.jsonl'

if not os.path.exists(LOG_FILE):
    print("Log file not found.")
    exit(1)

with open(LOG_FILE, 'r') as f:
    lines = f.readlines()
    if not lines:
        print("Log file empty.")
        exit(1)
        
    print(f"Total Records: {len(lines)}")
    for line in lines[-5:]:
        try:
            record = json.loads(line)
            symbol = record['market_state'].get('symbol', 'UNKNOWN')
            period = record['metadata'].get('market_period_id', 'UNKNOWN')
            print(f"ID: {record.get('id')} | Symbol: {symbol} | Period: {period}")
        except:
            print("Error parsing line")

    # Check last one specifically for success condition
    last_record = json.loads(lines[-1])
    symbol = last_record['market_state'].get('symbol', 'UNKNOWN')
    period = last_record['metadata'].get('market_period_id', 'UNKNOWN')
    
    if symbol == "ETH/USDT" and period == "ETH_TEST":
        print("VERIFICATION SUCCESS")
    else:
        print("VERIFICATION FAILED")
