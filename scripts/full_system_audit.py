import sys
import os
import glob
import importlib
sys.path.append(os.getcwd())

def check_module(module_path, class_name):
    try:
        mod = importlib.import_module(module_path)
        cls = getattr(mod, class_name)
        return True
    except ImportError as e:
        print(f"  [FAIL] Missing Module: {module_path} ({e})")
        return False
    except AttributeError:
        print(f"  [FAIL] Missing Class: {class_name} in {module_path}")
        return False

def audit_phase_1():
    print("--- Phase 1: Market Data Foundation ---")
    # Check for raw data folders
    base = "data/raw"
    if not os.path.exists(base):
        print("  [WARN] Data directory not found (may need ingestion).")
    else:
        print("  [OK] Data directory present.")
    
    # Check Ingestors
    return check_module("src.data.ingestor", "DataIngestor") and \
           check_module("src.data.macro", "MacroProvider") and \
           check_module("src.data.context.sentiment", "SentimentIngestor") and \
           check_module("src.data.context.onchain", "WhaleIngestor")

def audit_phase_2():
    print("\n--- Phase 2: Feature Engineering ---")
    return check_module("src.features.microstructure", "MicrostructureFeatures") and \
           check_module("src.features.microstructure_advanced", "LiquidityAnalyzer")

def audit_phase_3():
    print("\n--- Phase 3: Label Engineering ---")
    return check_module("src.features.labeler", "TripleBarrierLabeler") and \
           check_module("src.features.distributions", "DistributionAnalyzer")

def audit_phase_4():
    print("\n--- Phase 4: Regime Detection ---")
    return check_module("src.features.hmm_regime", "HMMRegimeClassifier") and \
           check_module("src.features.spoofing", "SpoofingDetector")

def audit_phase_5():
    print("\n--- Phase 5: Strategy Library ---")
    return check_module("src.strategies.arbitrage", "ArbitrageStrategy") and \
           check_module("src.strategies.market_making", "InventoryStrategy")

def audit_phase_6():
    print("\n--- Phase 6: Strategy Specific Models ---")
    return check_module("src.ml.feature_selection", "FeatureSelector")

def audit_phase_7():
    print("\n--- Phase 7: Portfolio Allocation ---")
    return check_module("src.portfolio.balancer", "NetExposureBalancer")

def audit_phase_8():
    print("\n--- Phase 8: Execution Engine ---")
    return check_module("src.execution.algos", "IcebergExecutor") and \
           check_module("src.execution.algos", "POVExecutor") and \
           check_module("src.execution.algos", "VWAPExecutor") and \
           check_module("src.execution.fees", "FeeOptimizer")

def audit_phase_9():
    print("\n--- Phase 9: Risk Engine ---")
    return check_module("src.risk.guardian", "RiskGuardian") and \
           check_module("src.risk.metrics", "RiskMetrics")

def audit_phase_10():
    print("\n--- Phase 10: Monitoring ---")
    return check_module("src.monitoring.drift", "DriftDetector") and \
           check_module("src.monitoring.performance", "PerformanceMonitor") and \
           check_module("src.monitoring.latency", "LatencyMonitor")

def audit_phase_11():
    print("\n--- Phase 11: Deployment ---")
    return check_module("src.deployment.shadow", "ShadowExecutor") and \
           check_module("src.deployment.canary", "CanaryLauncher") and \
           check_module("src.deployment.safety", "SafetyLock")

def main():
    print("=======================================")
    print("   INSTITUTIONAL SYSTEM AUDIT REPORT   ")
    print("=======================================")
    
    phases = [
        (1, audit_phase_1),
        (2, audit_phase_2),
        (3, audit_phase_3),
        (4, audit_phase_4),
        (5, audit_phase_5),
        (6, audit_phase_6),
        (7, audit_phase_7),
        (8, audit_phase_8),
        (9, audit_phase_9),
        (10, audit_phase_10),
        (11, audit_phase_11)
    ]
    
    results = {}
    for num, func in phases:
        try:
            passed = func()
            results[num] = "PASS" if passed else "FAIL"
        except Exception as e:
            print(f"  [CRASH] {e}")
            results[num] = "CRASH"
            
    print("\n=======================================")
    print("           FINAL SUMMARY               ")
    print("=======================================")
    all_pass = True
    for num, status in results.items():
        print(f"Phase {num:02d}: {status}")
        if status != "PASS":
            all_pass = False
            
    if all_pass:
        print("\n[SUCCESS] All phases are implemented and loadable.")
    else:
        print("\n[FAILURE] Some phases are incomplete.")
        sys.exit(1)

if __name__ == "__main__":
    main()
