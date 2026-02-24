
import os
import sys

def reset_paper():
    files = [
        "data/portfolio_state.json",
        "data/trade_history.json",
        "data/experience_log.jsonl" # Optional: Reset learning too? Maybe keep learning.
    ]
    
    print("🧹 Cleaning Paper Trading State...")
    for f in files:
        if os.path.exists(f):
            try:
                os.remove(f)
                print(f"  [DELETED] {f}")
            except Exception as e:
                print(f"  [ERROR] Could not delete {f}: {e}")
        else:
            print(f"  [MISSING] {f} (Clean)")
            
    print("\n✅ Reset Complete. Run 'python main.py' for a fresh start.")

if __name__ == "__main__":
    reset_paper()
