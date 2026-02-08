
import os
import sys
import logging
import pandas as pd

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.trainer import PolicyTrainer

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("TrainEnsemble")

def train_specialized_model(regime_suffix, model_type="xgboost", optimize=False):
    data_dir = "data"
    train_path = os.path.join(data_dir, f"train_{regime_suffix}.csv")
    val_path = os.path.join(data_dir, f"val_{regime_suffix}.csv")
    model_path = f"models/policy_{regime_suffix}.pkl"

    if not os.path.exists(train_path) or not os.path.exists(val_path):
        logger.warning(f"Data for {regime_suffix} missing. Skipping.")
        return None

    logger.info(f"Loading {regime_suffix} datasets...")
    train_df = pd.read_csv(train_path)
    val_df = pd.read_csv(val_path)

    trainer = PolicyTrainer(model_type=model_type)
    
    if optimize:
        logger.info(f"Optimizing Hyper-parameters for {model_type.upper()} ({regime_suffix.upper()})...")
        trainer.optimize(train_df, val_df, n_trials=30)
        
    logger.info(f"Training specialized {model_type.upper()} model for {regime_suffix.upper()}...")
    metrics = trainer.train(train_df, val_df)

    print(f"\n--- {regime_suffix.upper()} ({model_type.upper()}) REPORT ---")
    print(f"Val Accuracy: {metrics['validation_accuracy']:.4f}")
    print(f"Val ROC-AUC:  {metrics['validation_roc_auc']:.4f}")
    
    trainer.save_model(model_path)
    print(f"Saved: {model_path}")
    return metrics

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Train Ensemble Experts")
    parser.add_argument("--optimize", action="store_true", help="Run hyper-parameter optimization")
    parser.add_argument("--model-type", type=str, default="xgboost", choices=["xgboost", "lightgbm"], help="Model architecture to use")
    args = parser.parse_args()

    regimes = ["bull", "bear", "sideways"]
    ensemble_metrics = {}
    
    for r in regimes:
        m = train_specialized_model(r, model_type=args.model_type, optimize=args.optimize)
        if m:
            ensemble_metrics[r] = m
            
    if ensemble_metrics:
        print("\n" + "="*40)
        print(f"      ENSEMBLE SUMMARY ({args.model_type.upper()})")
        print("="*40)
        for r, m in ensemble_metrics.items():
            print(f"{r.upper():<10} | AUC: {m['validation_roc_auc']:.4f}")
        print("="*40)
    else:
        logger.error("No models were trained.")

if __name__ == "__main__":
    main()
