"""
Startup Checks - Runs all safety validations before bot starts.
Integrates Solutions #1, #2, #3.
"""
import sys
import logging

logger = logging.getLogger(__name__)


def run_startup_checks() -> bool:
    """
    Run all startup validations.
    Returns True if safe to proceed, False if critical issues found.
    """
    print("\n" + "="*60)
    print("🔍 RUNNING STARTUP CHECKS")
    print("="*60 + "\n")
    
    issues_found = False
    
    # 1. Config Validation
    print("📋 Config Validation:")
    from src.core.config_validator import validate_config
    config_issues = validate_config()
    if any("DANGER" in issue for issue in config_issues):
        issues_found = True
    print()
    
    # 2. Model Staleness Check
    print("🧠 Model Staleness Check:")
    from src.ml.staleness import check_model_staleness
    needs_retrain = check_model_staleness()
    if needs_retrain:
        print("   ➡️ Consider running: python scripts/train_policy.py")
    print()
    
    # 3. Decision Audit Setup
    print("📝 Decision Audit:")
    from src.monitoring.decision_audit import get_auditor
    auditor = get_auditor()
    print(f"   ✅ Decision audit logging to: {auditor.log_path}")
    print()
    
    print("="*60)
    if issues_found:
        print("⚠️ CRITICAL ISSUES FOUND - Review before proceeding")
    else:
        print("✅ ALL CHECKS PASSED - Safe to start")
    print("="*60 + "\n")
    
    return not issues_found


if __name__ == "__main__":
    success = run_startup_checks()
    sys.exit(0 if success else 1)
