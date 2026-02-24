from src.agent.analyzer import ObserverAnalyzer
from src.agent.planner import AdaptivePlanner
from src.agent.experiment_manager import ExperimentManager, ExperimentCriteria
from src.agent.governor import DeploymentGovernor


def test_observer_analyzer_builds_diagnostics():
    analyzer = ObserverAnalyzer()
    diagnostics = analyzer.build_diagnostics(
        [
            {"strategy": "MOMENTUM", "entry_regime": "BULL_TREND", "realized_pnl_pct": -1.2, "loss_category": "REGIME_SHIFT"},
            {"strategy": "MOMENTUM", "entry_regime": "BULL_TREND", "realized_pnl_pct": 1.5},
            {"strategy": "SHORT_MOMENTUM", "entry_regime": "BEAR_TREND", "realized_pnl_pct": 0.8},
        ]
    )

    assert diagnostics["total_trades"] == 3
    assert diagnostics["top_issue"] == "REGIME_SHIFT"
    assert "MOMENTUM" in diagnostics["by_strategy"]


def test_planner_generates_bounded_actions():
    planner = AdaptivePlanner()
    actions = planner.propose_actions({"top_issue": "REGIME_SHIFT", "win_rate": 0.4})
    assert len(actions) >= 1
    for action in actions:
        assert action["action_type"] in planner.ALLOWED_ACTION_TYPES


def test_experiment_manager_and_governor_flow():
    manager = ExperimentManager()
    result = manager.evaluate(
        candidate={"trades": 50, "win_rate": 0.54, "sharpe": 1.1, "max_drawdown": 4.8},
        champion={"trades": 50, "win_rate": 0.50, "sharpe": 1.0, "max_drawdown": 5.0},
        criteria=ExperimentCriteria(min_trades=30, min_win_rate_delta=0.0, min_sharpe_delta=0.0, max_drawdown_increase=0.0),
    )
    governor = DeploymentGovernor()
    decision = governor.decide(result, risk_veto=False, canary_failed=False)

    assert result["approved"] is True
    assert decision["promote"] is True
    assert decision["mode"] == "canary"
