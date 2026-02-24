from src.agent.orchestrator import AgentOrchestrator
from src.core.definitions import (
    Action,
    ActionDirection,
    MarketRegime,
    MarketState,
    RiskLevel,
    StrategyType,
    TrendStrength,
    VolatilityLevel,
)


def _state(**overrides) -> MarketState:
    base = {
        "market_regime": MarketRegime.BULL_TREND,
        "volatility_level": VolatilityLevel.NORMAL,
        "trend_strength": TrendStrength.MODERATE,
        "time_of_day": "12",
        "trading_session": "NY",
        "day_type": "WEEKDAY",
        "week_phase": "MID",
        "time_remaining_days": 10.0,
        "distance_to_key_levels": 1.0,
        "current_drawdown_percent": 0.0,
        "current_open_positions": 1,
        "spread_pct": 0.1,
        "body_pct": 0.2,
        "gap_pct": 0.1,
        "regime_confidence": 0.8,
        "regime_stable": True,
        "symbol": "BTC/USDC",
    }
    base.update(overrides)
    return MarketState(**base)


def _action(strategy: StrategyType = StrategyType.MOMENTUM) -> Action:
    return Action(
        strategy=strategy,
        direction=ActionDirection.LONG,
        risk_level=RiskLevel.LOW,
        reasoning="test",
    )


def test_orchestrator_risk_veto_forces_wait(tmp_path):
    orch = AgentOrchestrator(log_path=str(tmp_path / "agent.jsonl"), min_confidence=0.55)
    state = _state(current_drawdown_percent=-6.0)

    packet = orch.orchestrate(
        symbol="BTC/USDC",
        state=state,
        proposed_action=_action(),
        model_confidence=0.82,
        context={"open_positions": 1, "max_positions": 5, "gross_exposure": 0.2, "exposure_cap": 0.6},
    )

    assert packet["risk_veto"]["vetoed"] is True
    assert packet["final_action"] == "WAIT"


def test_orchestrator_low_confidence_conflict_returns_insufficient_data(tmp_path):
    orch = AgentOrchestrator(log_path=str(tmp_path / "agent.jsonl"), min_confidence=0.55)
    state = _state(regime_stable=False, regime_confidence=0.45, spread_pct=0.9)

    packet = orch.orchestrate(
        symbol="BTC/USDC",
        state=state,
        proposed_action=_action(),
        model_confidence=0.40,
        context={"open_positions": 1, "max_positions": 5, "gross_exposure": 0.2, "exposure_cap": 0.6},
    )

    assert packet["risk_veto"]["vetoed"] is False
    assert packet["final_action"] in {"INSUFFICIENT_DATA", "WAIT"}
    assert packet["confidence"] < 0.55


def test_orchestrator_clean_case_executes(tmp_path):
    orch = AgentOrchestrator(log_path=str(tmp_path / "agent.jsonl"), min_confidence=0.55)
    state = _state()

    packet = orch.orchestrate(
        symbol="BTC/USDC",
        state=state,
        proposed_action=_action(),
        model_confidence=0.84,
        context={"open_positions": 1, "max_positions": 5, "gross_exposure": 0.2, "exposure_cap": 0.6},
    )

    assert packet["risk_veto"]["vetoed"] is False
    assert packet["final_action"] in {"EXECUTE", "EXECUTE_REDUCED"}
