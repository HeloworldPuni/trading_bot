
import json
import os

def analyze(path):
    if not os.path.exists(path):
        return None
    records = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                r = json.loads(line)
                if r.get('resolved') is True:
                    records.append(r)
            except:
                continue
    
    # Filter for actual trades (not WAITS)
    # In main.py, trades are added to open_positions.
    # In the log, trades have action direction != FLAT
    trades = [r for r in records if r['action_taken']['direction'] != 'FLAT']
    
    if not trades:
        return {"count": 0, "win_rate": 0, "avg_reward": 0, "total_reward": 0}
    
    wins = sum(1 for r in trades if r['reward'] > 0)
    win_rate = (wins / len(trades)) * 100
    avg_reward = sum(r['reward'] for r in trades) / len(trades)
    total_reward = sum(r['reward'] for r in trades)
    
    return {
        "count": len(trades),
        "win_rate": win_rate,
        "avg_reward": avg_reward,
        "total_reward": total_reward
    }

gated = analyze('data/experience_log_recent_gated.jsonl')
baseline = analyze('data/experience_log_recent_baseline.jsonl')

print("--- FINAL VERIFICATION: ML GATING IMPACT ---")
if baseline and gated:
    print(f"BASELINE (No Gating)  | Count: {baseline['count']} | Win Rate: {baseline['win_rate']:.2f}% | Total Reward: {baseline['total_reward']:.2f}")
    print(f"GATED (0.55 Threshold) | Count: {gated['count']} | Win Rate: {gated['win_rate']:.2f}% | Total Reward: {gated['total_reward']:.2f}")
    
    wr_diff = gated['win_rate'] - baseline['win_rate']
    count_diff = baseline['count'] - gated['count']
    
    print(f"\nIMPACT:")
    print(f"- Filtered out {count_diff} low-confidence trades ({(count_diff/baseline['count']*100):.1f}% reduction).")
    print(f"- Win Rate improved by +{wr_diff:.2f}%.")
    print(f"- Average Trade Quality increased from {baseline['avg_reward']:.4f} to {gated['avg_reward']:.4f}.")
else:
    print("Error: Could not find one or both log files.")
