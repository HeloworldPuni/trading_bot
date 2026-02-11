"""
Startup checks for pre-run safety validation.
"""

import logging
import os
import sys
from pathlib import Path

logger = logging.getLogger(__name__)

# Ensure `src` imports resolve when executed as `python scripts/startup_checks.py`.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def _configure_console_encoding() -> None:
    """
    Avoid Windows cp1252 print/log crashes.
    """
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def run_startup_checks() -> bool:
    """
    Run startup validations.
    Returns True when safe to proceed.
    """
    _configure_console_encoding()

    print("\n" + "=" * 60)
    print("RUNNING STARTUP CHECKS")
    print("=" * 60 + "\n")

    issues_found = False
    from src.config import Config

    # 0) Runtime sanity check (catches broken embeddable-style installs).
    stdlib_probe = os.path.join(sys.base_prefix, "Lib", "encodings")
    if not os.path.exists(stdlib_probe):
        print("[CRITICAL] Python runtime appears incomplete (missing stdlib encodings path).")
        print(f"          Checked: {stdlib_probe}")
        issues_found = True
    else:
        print(f"Runtime Sanity: [OK] stdlib found at {stdlib_probe}")
    print()

    # 1) Config validation
    print("Config Validation:")
    from src.core.config_validator import validate_config

    config_issues = validate_config()
    if any(("DANGER" in issue) or ("CRITICAL" in issue) for issue in config_issues):
        issues_found = True
    print()

    # 2) Model staleness
    print("Model Staleness Check:")
    from src.ml.staleness import check_model_staleness

    needs_retrain = check_model_staleness()
    if needs_retrain:
        print("   -> Consider running: python scripts/train_policy.py")
        if Config.STRICT_STARTUP:
            print("   [STRICT] Treating stale/unknown model status as startup failure")
            issues_found = True
    print()

    # 3) Decision audit
    print("Decision Audit:")
    from src.monitoring.decision_audit import get_auditor

    auditor = get_auditor()
    print(f"   [OK] Decision audit logging to: {auditor.log_path}")
    print()

    print("=" * 60)
    if issues_found:
        print("[FAIL] CRITICAL ISSUES FOUND - Review before proceeding")
    else:
        print("[OK] ALL CHECKS PASSED - Safe to start")
    print("=" * 60 + "\n")

    return not issues_found


if __name__ == "__main__":
    success = run_startup_checks()
    sys.exit(0 if success else 1)
