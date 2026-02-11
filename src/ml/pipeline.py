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
        logger.info("Pipeline: Threshold met. Starting Adaptive Ensemble Update...")
        
        # 1. Rebuild Dataset Splits
        data_dir = "data"
        full_csv = os.path.join(data_dir, "ml_dataset.csv")
        rows = self.builder.build_from_log(self.data_log_path, full_csv)
        if not rows:
            logger.error("Pipeline: Failed to build dataset.")
            return False
            
        self.builder.build_splits(rows, full_csv, data_dir)
        self.builder.build_regime_splits(full_csv, data_dir)
        
        # 2. Retrain Experts
        regimes = ["bull", "bear", "sideways"]
        next_ver = self.registry.get_next_version()
        new_experts = {}
        any_improvement = False
        
        active_experts = self.registry.get_active_experts() or {}
        
        for r in regimes:
            train_path = os.path.join(data_dir, f"train_{r}.csv")
            val_path = os.path.join(data_dir, f"val_{r}.csv")
            
            if not os.path.exists(train_path) or not os.path.exists(val_path):
                logger.warning(f"Pipeline: Missing data for expert '{r}'. Skipping.")
                # Copy active expert if it exists
                if r in active_experts:
                    new_experts[r] = active_experts[r]
                continue
                
            try:
                train_df = pd.read_csv(train_path)
                val_df = pd.read_csv(val_path)
                
                if len(train_df) < 20 or len(val_df) < 10:
                    logger.warning(f"Pipeline: Insufficient data for expert '{r}'.")
                    if r in active_experts: new_experts[r] = active_experts[r]
                    continue
                    
                trainer = PolicyTrainer()
                # Run lightweight optimization if data is large enough
                metrics = trainer.optimize(train_df, val_df, n_trials=10) if len(train_df) > 1000 else trainer.train(train_df, val_df)
                if len(train_df) > 1000: metrics = trainer.train(train_df, val_df) # Final train with best params
                
                model_path = os.path.join(self.models_dir, f"policy_{r}_{next_ver}.pkl")
                trainer.save_model(model_path)
                
                # Check for improvement (handle both 'auc' and 'validation_roc_auc' keys)
                new_auc = metrics.get("validation_roc_auc", metrics.get("auc", 0.0))
                active_info = active_experts.get(r, {})
                active_metrics = active_info.get("metrics", {})
                current_auc = active_metrics.get("validation_roc_auc", active_metrics.get("auc", 0.0))
                
                logger.info(f"Pipeline: Expert '{r}' New AUC: {new_auc:.4f} vs Current AUC: {current_auc:.4f}")
                
                if new_auc > current_auc:
                    logger.info(f"Pipeline: Expert '{r}' improved!")
                    any_improvement = True
                    new_experts[r] = {
                        "path": model_path,
                        "metrics": metrics
                    }
                else:
                    # Keep old expert in new version to maintain stability
                    if r in active_experts:
                        new_experts[r] = active_experts[r]
                    else:
                        # If first time, use new one
                        new_experts[r] = {"path": model_path, "metrics": metrics}
                        any_improvement = True
            except Exception as e:
                logger.error(f"Pipeline: Failed to retrain expert '{r}': {e}")
                if r in active_experts: new_experts[r] = active_experts[r]

        if any_improvement:
            logger.info(f"Pipeline: PROMOTION GRANTED for Ensemble {next_ver}.")
            # Register and Promote
            self.registry.register_ensemble(next_ver, new_experts, total_records)
            self.registry.promote_model(next_ver, total_records)
            return True
        else:
            logger.info("Pipeline: PROMOTION REJECTED. No expert outperformed its benchmark.")
            return False
