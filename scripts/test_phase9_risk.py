import os
import sys

import numpy as np
import pandas as pd

sys.path.append(os.getcwd())

from src.risk.guardian import RiskGuardian
from src.risk.metrics import RiskMetrics


def test_metrics():
    print("\n[TEST] Risk Metrics (VaR / ES / Kelly)")

    np.random.seed(42)
    returns = pd.Series(np.random.normal(0, 0.02, 1000))

    var_hist = RiskMetrics.calculate_var_historical(returns, 0.95)
    print(f"Historical VaR (95%): {var_hist:.4f}")

    var_param = RiskMetrics.calculate_parametric_var(returns, 0.95)
    print(f"Parametric VaR (95%): {var_param:.4f}")
    if 0.030 <= var_param <= 0.036:
        print("[PASS] Parametric VaR within expected range")
    else:
        print(f"[FAIL] Parametric VaR {var_param:.4f} out of expected range")

    es = RiskMetrics.calculate_expected_shortfall(returns, 0.95)
    print(f"Expected Shortfall (95%): {es:.4f}")
    if es > var_hist:
        print("[PASS] ES > VaR (tail risk captured)")
    else:
        print("[FAIL] ES <= VaR")

    kelly = RiskMetrics.calculate_kelly(win_rate=0.55, avg_win=0.02, avg_loss=0.01)
    print(f"Kelly Fraction: {kelly:.4f}")
    if 0.32 <= kelly <= 0.33:
        print("[PASS] Kelly calculation correct")
    else:
        print(f"[FAIL] Kelly {kelly:.4f}")


def test_guardian():
    print("\n[TEST] Risk Guardian (Kill Switch)")

    guardian = RiskGuardian(daily_stop_loss_pct=-0.03, max_drawdown_pct=-0.10)

    guardian.update_state(100000.0)
    guardian.update_state(101000.0)
    guardian.update_state(99000.0)

    if guardian.check_system_health():
        print("[PASS] System healthy under normal conditions")
    else:
        print("[FAIL] False positive kill switch")

    print("Simulating -3.5% daily loss...")
    guardian.update_state(96500.0)

    if not guardian.check_system_health():
        print(f"[PASS] Daily stop triggered. Reason: {guardian.state.kill_reason}")
    else:
        print("[FAIL] Daily stop failed to trigger")

    print("Resetting guardian for drawdown test...")
    guardian = RiskGuardian(daily_stop_loss_pct=-0.03, max_drawdown_pct=-0.10)
    guardian.update_state(100000.0)
    guardian.update_state(120000.0)

    print("Simulating -11% drawdown from HWM...")
    guardian.update_state(106000.0)

    if not guardian.check_system_health():
        print(f"[PASS] Max drawdown triggered. Reason: {guardian.state.kill_reason}")
    else:
        print(f"[FAIL] Drawdown failed to trigger (DD={guardian.state.current_drawdown_pct:.2%})")


if __name__ == "__main__":
    test_metrics()
    test_guardian()
