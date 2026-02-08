
import os
import sys
import logging
import argparse

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.pipeline import AdaptivePipeline

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AdaptiveUpdate")

def main():
    parser = argparse.ArgumentParser(description="Adaptive Policy Retraining Pipeline")
    parser.add_argument("--threshold", type=int, default=2000, help="New record threshold to trigger retraining")
    parser.add_argument("--force", action="store_true", help="Force retraining regardless of record count")
    
    args = parser.parse_args()

    pipeline = AdaptivePipeline(threshold=args.threshold)
    
    if args.force:
        logger.info("Forcing update as requested...")
        # We simulate meeting the threshold by overriding the check logic or calling internal
        # For simplicity, we just pass the total count
        pipeline._execute_update(pipeline.registry.get_last_trained_count() + 2000)
    else:
        pipeline.run_check()

if __name__ == "__main__":
    main()
