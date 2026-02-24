from pathlib import Path

from src.core.meta_learner import MetaLearner


def _new_meta(tmp_path: Path) -> MetaLearner:
    return MetaLearner(history_window=20, state_file=str(tmp_path / "meta_state.json"))


def test_policy_not_applied_with_insufficient_samples(tmp_path):
    meta = _new_meta(tmp_path)

    for _ in range(5):
        meta.record_trade_result(
            won=False,
            loss_category="BAD_TIMING",
            strategy="MOMENTUM",
            entry_regime="BULL_TREND",
        )

    adj = meta.get_policy_adjustments("MOMENTUM", "BULL_TREND", regime_stable=True)
    assert adj["applied"] is False
    assert adj["sample_size"] == 5


def test_policy_applies_when_loss_pattern_is_dominant(tmp_path):
    meta = _new_meta(tmp_path)

    for _ in range(14):
        meta.record_trade_result(
            won=False,
            loss_category="BAD_TIMING",
            strategy="MOMENTUM",
            entry_regime="BULL_TREND",
        )
    for _ in range(4):
        meta.record_trade_result(
            won=True,
            strategy="MOMENTUM",
            entry_regime="BULL_TREND",
        )

    adj = meta.get_policy_adjustments("MOMENTUM", "BULL_TREND", regime_stable=True)
    assert adj["applied"] is True
    assert adj["dominant_loss_category"] == "BAD_TIMING"
    assert adj["score_multiplier"] < 1.0
    assert adj["confidence_buffer"] > 0.0
    assert adj["size_multiplier"] < 1.0


def test_sync_from_history_populates_context_policy(tmp_path):
    meta = _new_meta(tmp_path)

    history = []
    for _ in range(12):
        history.append(
            {
                "strategy": "BREAKOUT",
                "entry_regime": "TRANSITION",
                "realized_pnl_usd": -5.0,
                "loss_category": "REGIME_SHIFT",
            }
        )
    for _ in range(4):
        history.append(
            {
                "strategy": "BREAKOUT",
                "entry_regime": "TRANSITION",
                "realized_pnl_usd": 4.0,
                "loss_category": None,
            }
        )

    meta.sync_from_history(history)
    adj = meta.get_policy_adjustments("BREAKOUT", "TRANSITION", regime_stable=False)
    assert adj["applied"] is True
    assert adj["dominant_loss_category"] == "REGIME_SHIFT"
    assert adj["score_multiplier"] < 1.0
