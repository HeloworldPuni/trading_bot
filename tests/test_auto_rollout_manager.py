from src.agent.rollout_manager import AutoRolloutManager


def _history(n: int, loss_category: str = "REGIME_SHIFT"):
    items = []
    for i in range(n):
        pnl = -1.2 if i % 2 == 0 else 0.8
        entry = {
            "realized_pnl_pct": pnl,
            "strategy": "MOMENTUM" if i % 2 == 0 else "SHORT_MOMENTUM",
            "entry_regime": "BULL_TREND" if i % 2 == 0 else "BEAR_TREND",
        }
        if pnl < 0:
            entry["loss_category"] = loss_category
        items.append(entry)
    return items


def test_auto_rollout_creates_candidate(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        stages=[{"name": "PROBE", "fraction": 0.5, "min_trades": 2}],
    )

    event = manager.maybe_create_candidate(_history(10, loss_category="REGIME_SHIFT"))
    snap = manager.snapshot()

    assert event is not None
    assert snap["candidate_version"] is not None


def test_auto_rollout_rollback_on_stage_drawdown(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        max_stage_dd_pct=1.0,
        stages=[{"name": "PROBE", "fraction": 0.5, "min_trades": 3}],
    )
    manager.maybe_create_candidate(_history(10, loss_category="REGIME_SHIFT"))

    assert manager.snapshot()["candidate_version"] is not None
    assert manager.record_trade_result(-1.0, 1000.0) is None
    event = manager.record_trade_result(-1.0, 980.0)

    assert event is not None
    assert "rolled back" in event.lower()
    assert manager.snapshot()["candidate_version"] is None


def test_auto_rollout_promotes_candidate_after_stage_passes(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        max_stage_dd_pct=5.0,
        stages=[
            {"name": "PROBE", "fraction": 0.5, "min_trades": 1},
            {"name": "FULL", "fraction": 1.0, "min_trades": 1},
        ],
        min_win_rate_delta=-1.0,
        min_sharpe_delta=-10.0,
        max_dd_increase=10.0,
    )

    manager.maybe_create_candidate(_history(10, loss_category="REGIME_SHIFT"))
    candidate_before = manager.snapshot()["candidate_version"]
    champion_before = manager.snapshot()["champion_version"]

    event_stage = manager.record_trade_result(1.8, 1000.0)
    event_promote = manager.record_trade_result(1.5, 1010.0)
    snap = manager.snapshot()

    assert candidate_before is not None
    assert champion_before is not None
    assert event_stage is not None
    assert event_promote is not None
    assert snap["candidate_version"] is None
    assert snap["champion_version"] != champion_before


def test_auto_rollout_rolls_back_after_risk_veto_streak(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        max_risk_veto_streak=2,
        stages=[{"name": "PROBE", "fraction": 0.5, "min_trades": 3}],
    )
    manager.maybe_create_candidate(_history(10, loss_category="REGIME_SHIFT"))
    assert manager.snapshot()["candidate_version"] is not None

    event = manager.record_governance_signal(risk_veto=True, reason="exposure cap reached")
    assert event is None
    event = manager.record_governance_signal(risk_veto=True, reason="exposure cap reached")

    assert event is not None
    assert "rolled back" in event.lower()
    assert manager.snapshot()["candidate_version"] is None


def test_auto_rollout_memory_blocks_same_policy_during_cooldown(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        policy_cooldown_trades=999,
        stages=[{"name": "PROBE", "fraction": 0.5, "min_trades": 3}],
    )

    history = _history(10, loss_category="REGIME_SHIFT")
    event_create = manager.maybe_create_candidate(history)
    assert event_create is not None
    assert manager.snapshot()["candidate_version"] is not None

    # Force rollback to store the candidate policy in reject-memory.
    event_rollback = manager.record_governance_signal(canary_failed=True, reason="canary halt")
    assert event_rollback is not None
    assert manager.snapshot()["candidate_version"] is None

    # With the same history and long cooldown, identical candidate should be skipped.
    event_second = manager.maybe_create_candidate(_history(16, loss_category="REGIME_SHIFT"))
    assert event_second is not None
    assert "cooldown" in event_second.lower()
    assert manager.snapshot()["candidate_version"] is None


def test_auto_rollout_shadow_mode_does_not_promote_or_rollback(tmp_path):
    manager = AutoRolloutManager(
        state_file=str(tmp_path / "rollout_state.json"),
        trigger_trades=6,
        window_trades=10,
        stages=[{"name": "PROBE", "fraction": 0.5, "min_trades": 1}],
        min_win_rate_delta=-1.0,
        min_sharpe_delta=-10.0,
        max_dd_increase=10.0,
    )
    manager.maybe_create_candidate(_history(10, loss_category="REGIME_SHIFT"))
    snap_before = manager.snapshot()

    event = manager.record_trade_result(2.0, 1000.0, active_mode=False)
    snap_after = manager.snapshot()

    assert event is None
    assert snap_before["candidate_version"] is not None
    assert snap_after["candidate_version"] == snap_before["candidate_version"]
    assert snap_after["champion_version"] == snap_before["champion_version"]
