import os
import sys
import logging

import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.trainer import PolicyTrainer

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("WalkForward")


def _train_val_split(df: pd.DataFrame, val_ratio: float = 0.2):
    split = int(len(df) * (1 - val_ratio))
    return df.iloc[:split], df.iloc[split:]


def walk_forward(
    df: pd.DataFrame,
    train_window: int,
    test_window: int,
    purge_window: int,
    embargo_window: int
):
    results = []
    start = 0
    total = len(df)

    while start + train_window + purge_window + test_window <= total:
        train_slice = df.iloc[start : start + train_window]
        test_start = start + train_window + purge_window
        test_slice = df.iloc[test_start : test_start + test_window]

        train_df, val_df = _train_val_split(train_slice)

        trainer = PolicyTrainer()
        train_metrics = trainer.train(train_df, val_df)

        X_test = test_slice[trainer.feature_cols]
        y_test = test_slice[trainer.target_col]
        preds = trainer.model.predict(X_test)
        probs = trainer.model.predict_proba(X_test)[:, 1]

        result = {
            "start": start,
            "train_rows": len(train_slice),
            "test_rows": len(test_slice),
            "train_accuracy": float(train_metrics["train_accuracy"]),
            "val_accuracy": float(train_metrics["validation_accuracy"]),
            "val_auc": float(train_metrics["validation_roc_auc"]),
            "test_accuracy": float(accuracy_score(y_test, preds)),
            "test_auc": float(roc_auc_score(y_test, probs)),
        }
        results.append(result)

        start += test_window + embargo_window

    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Walk-forward evaluation with purge/embargo.")
    parser.add_argument("--data", default="data/ml_dataset.csv", help="Path to dataset CSV (time-ordered)")
    parser.add_argument("--train-window", type=int, default=30000)
    parser.add_argument("--test-window", type=int, default=5000)
    parser.add_argument("--purge-window", type=int, default=200)
    parser.add_argument("--embargo-window", type=int, default=200)
    args = parser.parse_args()

    if not os.path.exists(args.data):
        logger.error(f"Dataset not found: {args.data}")
        return

    df = pd.read_csv(args.data)
    results = walk_forward(
        df,
        train_window=args.train_window,
        test_window=args.test_window,
        purge_window=args.purge_window,
        embargo_window=args.embargo_window
    )

    if not results:
        logger.error("No walk-forward splits were evaluated. Check window sizes.")
        return

    avg_test_auc = sum(r["test_auc"] for r in results) / len(results)
    avg_test_acc = sum(r["test_accuracy"] for r in results) / len(results)

    print("\n" + "=" * 40)
    print("WALK-FORWARD SUMMARY")
    print("=" * 40)
    print(f"Splits:          {len(results)}")
    print(f"Avg Test AUC:    {avg_test_auc:.4f}")
    print(f"Avg Test Acc:    {avg_test_acc:.4f}")
    print("=" * 40)


if __name__ == "__main__":
    main()
