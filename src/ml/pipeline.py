import logging
import os
import json
import pandas as pd
import joblib
from typing import Optional, Dict, Any
from src.ml.registry import ModelRegistry
from src.ml.dataset_builder import DatasetBuilder
from src.ml.trainer import PolicyTrainer
from src.ml.evaluator import PolicyEvaluator

logger = logging.getLogger(__name__)

class AdaptivePipeline:
    def __init__(self, 
                 threshold: int = 100,  # Phase A: Lowered from 2000 for faster learning
                 data_log_path: str = "data/experience_log.jsonl",
                 models_dir: str = "models"):
        self.threshold = threshold
        self.data_log_path = data_log_path
        self.models_dir = models_dir
        self.registry = ModelRegistry()
        self.builder = DatasetBuilder()

    def run_check(self) -> bool:
        """
        Checks if retraining is needed based on new data.
        Returns True if update was attempted.
        """
        logger.info("Pipeline: Checking for new experience data...")
        
        # 1. Count resolved records in log
        resolved_count = 0
        if os.path.exists(self.data_log_path):
            with open(self.data_log_path, "r", encoding="utf-8") as f:
                for line in f:
                    try:
                        if json.loads(line).get("resolved") is True:
                            resolved_count += 1
                    except:
                        continue
        
        last_count = self.registry.get_last_trained_count()
        new_records = resolved_count - last_count
        
        logger.info(f"Pipeline: Detected {new_records} new resolved records (Total: {resolved_count}).")
        
        if new_records < self.threshold:
            logger.info(f"Pipeline: Below threshold ({self.threshold}). Skipping update.")
            return False
            
        return self._execute_update(resolved_count)

    def _execute_update(self, total_records: int) -> bool:
        logger.info("Pipeline: Threshold met. Starting Adaptive Update...")
        
        # 1. Rebuild Dataset Splits
        data_dir = "data"
        full_csv = os.path.join(data_dir, "ml_dataset.csv")
        rows = self.builder.build_from_log(self.data_log_path, full_csv)
        if not rows:
            logger.error("Pipeline: Failed to build dataset.")
            return False
            
        self.builder.build_splits(rows, data_dir)
        
        # 2. Train New Model Version
        next_ver = self.registry.get_next_version()
        model_filename = f"policy_model_{next_ver}.pkl"
        model_path = os.path.join(self.models_dir, model_filename)
        
        train_df = pd.read_csv(os.path.join(data_dir, "train.csv"))
        val_df = pd.read_csv(os.path.join(data_dir, "validation.csv"))
        test_df = pd.read_csv(os.path.join(data_dir, "test.csv"))
        
        import pandas as pd # Ensure pandas is available locally if needed, but it's likely global
        
        trainer = PolicyTrainer()
        trainer.train(train_df, val_df)
        trainer.save_model(model_path)
        
        # 3. Evaluate New Model
        evaluator = PolicyEvaluator(model_path)
        new_report = evaluator.evaluate(test_df)
        new_auc = new_report["metrics"]["test_roc_auc"]
        
        # 4. Promotion Gate
        active_metrics = self.registry.get_active_metrics()
        current_auc = active_metrics.get("test_roc_auc", 0.0) if active_metrics else 0.0
        
        logger.info(f"Pipeline: New Model ({next_ver}) AUC: {new_auc:.4f} vs Current AUC: {current_auc:.4f}")
        
        # Register the new model anyway (for history)
        self.registry.register_model(next_ver, model_path, new_report["metrics"], total_records)
        
        if new_auc > current_auc:
            logger.info(f"Pipeline: PROMOTION GRANTED. Updating active model to {next_ver}.")
            self.registry.promote_model(next_ver, total_records)
            return True
        else:
            logger.info("Pipeline: PROMOTION REJECTED. New model did not outperform current model.")
            return False
