
import os
import sys
import logging

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.dataset_builder import DatasetBuilder

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("BuildDataset")

def main():
    data_dir = "data"
    master_log = os.path.join(data_dir, "experience_log.jsonl")
    output_csv = os.path.join(data_dir, "ml_dataset.csv")

    # Check if master_log exists. If not, try to merge suffixes.
    if not os.path.exists(master_log):
        logger.info("Master log not found. Attempting to merge suffix-based logs (btc, eth, sol)...")
        log_files = [f for f in os.listdir(data_dir) if f.startswith("experience_log_") and f.endswith(".jsonl")]
        if not log_files:
            logger.error("No experience logs found in data/ directory.")
            return
        
        with open(master_log, "w", encoding="utf-8") as outfile:
            for fname in log_files:
                fpath = os.path.join(data_dir, fname)
                logger.info(f"Merging {fname}...")
                with open(fpath, "r", encoding="utf-8") as infile:
                    outfile.write(infile.read())
        logger.info(f"Created master log: {master_log}")

    builder = DatasetBuilder()
    logger.info("Starting dataset transformation...")
    count = builder.build_from_log(master_log, output_csv)
    
    if count > 0:
        logger.info(f"Building time-based splits for {count} rows...")
        builder.build_splits(count, output_csv, data_dir)
        
        logger.info("Building regime-specific ensemble splits...")
        builder.build_regime_splits(output_csv, data_dir)
        
        logger.info("SUCCESS: ML-Ready dataset and splits created at data/")
    else:
        logger.error("FAILED: No valid records found.")

if __name__ == "__main__":
    main()
