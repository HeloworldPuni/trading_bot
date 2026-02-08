
import os
import sys
import logging
import pandas as pd

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ml.evaluator import PolicyEvaluator

logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("EvaluatePolicy")

def main():
    data_dir = "data"
    test_path = os.path.join(data_dir, "test.csv")
    model_path = "models/policy_model_v1.pkl"
    report_path = "reports/policy_model_v1_report.json"

    if not os.path.exists(test_path):
        logger.error(f"Test data missing: {test_path}. Run build_dataset.py first.")
        return
    if not os.path.exists(model_path):
        logger.error(f"Model missing: {model_path}. Run train_policy.py first.")
        return

    logger.info("Loading test dataset...")
    test_df = pd.read_csv(test_path)

    try:
        evaluator = PolicyEvaluator(model_path)
        logger.info("Starting Policy Model Evaluation...")
        report = evaluator.evaluate(test_df)

        # Print summary
        m = report["metrics"]
        print("\n" + "="*40)
        print("      POLICY MODEL EVALUATION REPORT")
        print("="*40)
        print(f"Test Accuracy:  {m['test_accuracy']:.4f}")
        print(f"Test ROC-AUC:   {m['test_roc_auc']:.4f}")
        print("-"*40)
        print(f"Confusion Matrix:")
        print(f"  TP: {m['confusion_matrix']['tp']}  FP: {m['confusion_matrix']['fp']}")
        print(f"  FN: {m['confusion_matrix']['fn']}  TN: {m['confusion_matrix']['tn']}")
        print("="*40)
        
        print("\nTop 5 Feature Importance (Gain):")
        for feat, imp in list(report["feature_importance"].items())[:5]:
            print(f"  - {feat}: {imp:.4f}")
        print("="*40)

        evaluator.save_report(report, report_path)
        print(f"\nSUCCESS: Evaluation report saved to {report_path}")

    except Exception as e:
        logger.error(f"Evaluation failed: {e}")

if __name__ == "__main__":
    main()
