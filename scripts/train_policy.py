
import os
import sys
import logging
import pandas as pd

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.trainer import PolicyTrainer

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("TrainPolicy")

def main():
    data_dir = "data"
    train_path = os.path.join(data_dir, "train.csv")
    val_path = os.path.join(data_dir, "validation.csv")
    model_path = "models/policy_model_v1.pkl"

    if not os.path.exists(train_path) or not os.path.exists(val_path):
        logger.error(f"Training or Validation data missing in {data_dir}. Run build_dataset.py first.")
        return

    logger.info("Loading datasets...")
    train_df = pd.read_csv(train_path)
    val_df = pd.read_csv(val_path)

    trainer = PolicyTrainer()
    
    logger.info("Starting Policy Model Training (XGBoost)...")
    metrics = trainer.train(train_df, val_df)

    # Print results
    print("\n" + "="*40)
    print("      POLICY MODEL TRAINING REPORT")
    print("="*40)
    print(f"Train Accuracy:      {metrics['train_accuracy']:.4f}")
    print(f"Validation Accuracy: {metrics['validation_accuracy']:.4f}")
    print(f"Validation ROC-AUC:  {metrics['validation_roc_auc']:.4f}")
    print("="*40)

    trainer.save_model(model_path)
    print(f"\nSUCCESS: Policy model saved to {model_path}")

if __name__ == "__main__":
    main()
