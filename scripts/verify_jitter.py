import sys
import os
import json
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("VerifyEnhancedReplay")

def verify_enhanced_replay(log_path):
    if not os.path.exists(log_path):
        logger.error(f"Log file not found: {log_path}")
        return False
        
    jitter_detected = 0
    total_trades = 0
    durations = set()
    
    with open(log_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                record = json.loads(line)
                # Check for specific period
                metadata = record.get("metadata", {})
                if metadata.get("market_period_id") != "ETH_ENHANCED":
                    continue
                    
                # Look for finalized trades
                if record.get("resolved") and record.get("outcome"):
                    total_trades += 1
                    entry_price = record["outcome"].get("entry_price")
                    duration = record["outcome"].get("holding_period")
                    
                    if duration:
                        durations.add(duration)
                    
                    # Dummy data has opens like 29000.0, 29200.0 (Round numbers).
                    # Jitter creates non-round numbers.
                    if entry_price != round(entry_price, 1):
                         jitter_detected += 1
                         
            except Exception:
                continue
                
    logger.info(f"Total Trades: {total_trades}")
    logger.info(f"Jittery Entries: {jitter_detected}")
    logger.info(f"Unique Durations: {durations}")
    
    if jitter_detected > 0 and len(durations) > 1:
        logger.info("SUCCESS: Jitter and Variable Duration Detected.")
        return True
    else:
        logger.error("FAILURE: Missing Jitter or Variable Duration variance.")
        return False

if __name__ == "__main__":
    verify_enhanced_replay("data/experience_log.jsonl")
