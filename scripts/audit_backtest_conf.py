
import json
import collections

log_file = "data/experience_log_v4_verify_btc_v2.jsonl"
print(f"Auditing {log_file}...")

confs = []
blocked_count = 0
trade_count = 0

with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            j = json.loads(line)
            c = j.get("ml_confidence", 0.5)
            confs.append(c)
            
            action = j.get("action_taken", {})
            strat = action.get("strategy")
            reason = action.get("reasoning", "")
            
            if "Blocked by ML Confidence" in reason:
                blocked_count += 1
            if strat in ["BREAKOUT", "MOMENTUM", "SHORT_MOMENTUM", "SCALP", "MEAN_REVERSION"]:
                trade_count += 1
        except:
            continue

if not confs:
    print("No records found.")
    sys.exit(1)

print(f"Total Records: {len(confs)}")
print(f"Trades Executed: {trade_count}")
print(f"Trades Blocked: {blocked_count}")

# Unique confidence scores (other than 0.5)
unique_confs = sorted(list(set([c for c in confs if c != 0.5])))
print(f"Unique non-0.5 confidence scores: {len(unique_confs)}")

if unique_confs:
    print("Sample non-0.5 scores:")
    for v in unique_confs[:10]:
        print(f"  {v:.4f}")
    
    print(f"Min: {min(unique_confs):.4f} | Max: {max(unique_confs):.4f}")
else:
    print("WARNING: Every single record has ml_confidence = 0.5")
