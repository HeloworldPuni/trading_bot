"""
Autonomous Learning Scheduler - Phase A
Runs automated retraining on a schedule to close the learning loop.
"""
import os
import sys
import time
import logging
import threading
from datetime import datetime, timedelta

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.pipeline import AdaptivePipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("LearningScheduler")

class LearningScheduler:
    """
    Automated retraining scheduler that runs the adaptive pipeline
    at configurable intervals to ensure continuous learning.
    """
    
    def __init__(self, interval_hours: int = 24, min_trades: int = 50):
        self.interval_hours = interval_hours
        self.min_trades = min_trades
        self.pipeline = AdaptivePipeline(threshold=min_trades)
        self.last_run = None
        self.running = False
        self._thread = None
        
    def _check_and_retrain(self):
        """Execute a single retraining check."""
        logger.info(f"🔄 Learning Check triggered at {datetime.now().isoformat()}")
        
        try:
            result = self.pipeline.run_check()
            if result:
                logger.info("✅ Model updated successfully!")
            else:
                logger.info("ℹ️ No update needed (threshold not met or new model didn't outperform)")
            
            self.last_run = datetime.now()
        except Exception as e:
            logger.error(f"❌ Retraining failed: {e}")
    
    def _scheduler_loop(self):
        """Background loop that runs retraining at intervals."""
        logger.info(f"🚀 Learning Scheduler started. Interval: {self.interval_hours}h, Min trades: {self.min_trades}")
        
        while self.running:
            # Check if it's time to retrain
            if self.last_run is None or datetime.now() - self.last_run > timedelta(hours=self.interval_hours):
                self._check_and_retrain()
            
            # Sleep for 1 hour between checks
            time.sleep(3600)
    
    def start_background(self):
        """Start the scheduler in a background thread."""
        if self.running:
            logger.warning("Scheduler already running")
            return
            
        self.running = True
        self._thread = threading.Thread(target=self._scheduler_loop, daemon=True)
        self._thread.start()
        logger.info("🧠 Background learning scheduler activated")
        
    def stop(self):
        """Stop the scheduler."""
        self.running = False
        if self._thread:
            self._thread.join(timeout=5)
        logger.info("⏹️ Learning scheduler stopped")
        
    def run_now(self):
        """Manually trigger a retraining check."""
        self._check_and_retrain()


def main():
    """Standalone execution for manual or cron-triggered runs."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Autonomous Learning Scheduler")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--interval", type=int, default=24, help="Hours between retraining checks")
    parser.add_argument("--min-trades", type=int, default=50, help="Minimum new trades before retraining")
    
    args = parser.parse_args()
    
    scheduler = LearningScheduler(interval_hours=args.interval, min_trades=args.min_trades)
    
    if args.once:
        scheduler.run_now()
    else:
        scheduler.start_background()
        try:
            # Keep main thread alive
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            scheduler.stop()


if __name__ == "__main__":
    main()
