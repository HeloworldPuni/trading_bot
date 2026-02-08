
import json
import os

log_path = 'data/experience_log_recent_gated.jsonl'
if not os.path.exists(log_path):
    print("Log not found.")
    exit(1)

records = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            r = json.loads(line)
            if r.get('resolved') is True:
                records.append(r)
        except:
            continue

executed = [r for r in records if not r['metadata'].get('original_action')]
gated = [r for r in records if r['metadata'].get('original_action')]

print(f"--- Final Backtest Results ---")
print(f"Total Decisions Resolved: {len(records)}")
print(f"Trades Executed (Confirmed): {len(executed)}")
print(f"Trades Gated (Filtered): {len(gated)}")

if executed:
    exec_wins = sum(1 for r in executed if r['reward'] > 0)
    exec_wr = (exec_wins / len(executed)) * 100
    avg_exec_reward = sum(r['reward'] for r in executed) / len(executed)
    print(f"Executed Win Rate: {exec_wr:.2f}%")
    print(f"Avg Executed Reward: {avg_exec_reward:.4f}")

if gated:
    gated_wins = sum(1 for r in gated if r['reward'] > 0)
    gated_wr = (gated_wins / len(gated)) * 100
    avg_gated_reward = sum(r['reward'] for r in gated) / len(gated)
    print(f"Gated Hypothetical Win Rate: {gated_wr:.2f}%")
    print(f"Avg Gated Reward (Hypothetical): {avg_gated_reward:.4f}")
    
    improvement = exec_wr - gated_wr if executed else 0
    print(f"Win Rate Edge (Executed vs Gated): +{improvement:.2f}%")
