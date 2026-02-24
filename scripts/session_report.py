
import asyncio
import pandas as pd
import json
import logging
from datetime import datetime, timedelta
from src.database.storage import ExperienceDB
from src.core.notifications import NotificationManager
from src.config import Config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SessionReport")

async def generate_report():
    print("--- Session Report Generator ---")
    db = ExperienceDB()
    # Manually instantiate NotificationManager to avoid event loop issues with singleton if any
    notifier = NotificationManager()
    notifier.start()
    
    # 1. Load recent data (last 24h)
    records = db.get_recent_records(limit=1000) 
    
    if not records:
        logger.info("No records found in DB.")
        await notifier.stop()
        return

    # Filter for last 24 hours
    now = datetime.now()
    cutoff = now - timedelta(hours=24)
    
    session_trades = []
    
    for r in records:
        ts_str = r.get("timestamp")
        if ts_str:
            try:
                # Handle ISO format with Z or +00:00
                dt = datetime.fromisoformat(ts_str.replace('Z', '+00:00'))
                # Ensure timezone awareness compatibility
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=None) # simplification
                    if now.tzinfo is not None:
                         now = now.replace(tzinfo=None)
                else:
                    if now.tzinfo is None:
                        now = now.astimezone() # make aware

                if dt > cutoff:
                    session_trades.append(r)
            except ValueError:
                continue
                
    if not session_trades:
        logger.info("No trades in last 24h.")
        notifier.send("📊 **DAILY REPORT**: No trades executed in the last 24 hours.", level="INFO")
    else:
        # 2. Calculate Metrics
        # Convert to DF for easier grouping
        # Filter for non-WAIT actions to see actual trading activity
        actions = []
        for t in session_trades:
            act = t.get('action_taken', {})
            if isinstance(act, dict):
                actions.append(act.get('strategy', 'UNKNOWN'))
            else:
                actions.append(str(act))
                
        from collections import Counter
        counts = Counter(actions)
        
        total_trades = len(session_trades)
        
        # Construct Report
        report = f"📊 **SESSION REPORT (Last 24h)**\n\n"
        report += f"**Total Decisions**: {total_trades}\n"
        report += f"**Activity Breakdown**:\n"
        for strat, count in counts.items():
            report += f"- {strat}: {count}\n"
            
        # Send
        notifier.send(report, level="INFO")
        logger.info(f"Report sent with {total_trades} records.")
    
    # Allow time for async send
    await asyncio.sleep(5) 
    await notifier.stop()

def main():
    asyncio.run(generate_report())

if __name__ == "__main__":
    main()
