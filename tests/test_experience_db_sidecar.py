import json
from pathlib import Path

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
from src.database.storage import ExperienceDB, load_resolution_updates
from src.ml.dataset_builder import DatasetBuilder


def _sample_state() -> MarketState:
    return MarketState(
        symbol="BTC/USDC",
        market_regime=MarketRegime.BEAR_TREND,
        volatility_level=VolatilityLevel.NORMAL,
        trend_strength=TrendStrength.MODERATE,
        time_of_day="12",
        trading_session="NY",
        day_type="WEEKDAY",
        week_phase="MID",
        time_remaining_days=1.0,
        distance_to_key_levels=1.0,
        current_price=100.0,
        rsi=42.0,
        trend_spread=-1.2,
        dist_to_high=1.0,
        dist_to_low=1.0,
    )


def _sample_action() -> Action:
    return Action(
        strategy=StrategyType.SHORT_MOMENTUM,
        direction=ActionDirection.SHORT,
        risk_level=RiskLevel.LOW,
        base_risk=0.01,
        adjusted_risk=0.01,
        risk_multiplier=1.0,
        target_weight=0.0,
        tp=99.0,
        sl=101.0,
        reasoning="test",
    )


def test_finalize_writes_resolution_sidecar(tmp_path):
    db = ExperienceDB(filename="experience_log.jsonl", data_path=str(tmp_path))
    decision_id = db.log_decision(_sample_state(), _sample_action())
    db.finalize_record(decision_id, {"reason": "TP", "pnl_usd": 1.23}, final_reward=1.0)

    log_path = Path(db.filepath)
    sidecar_path = Path(f"{db.filepath}.resolved.jsonl")

    assert log_path.exists()
    assert sidecar_path.exists()

    # Base log entry remains immutable; resolution is stored append-only in sidecar.
    base_record = json.loads(log_path.read_text(encoding="utf-8").strip())
    assert base_record["id"] == decision_id
    assert base_record["resolved"] is False

    updates = load_resolution_updates(db.filepath)
    assert decision_id in updates
    assert updates[decision_id]["resolved"] is True
    assert updates[decision_id]["outcome"]["reason"] == "TP"


def test_dataset_builder_applies_resolution_sidecar(tmp_path):
    db = ExperienceDB(filename="experience_log.jsonl", data_path=str(tmp_path))
    decision_id = db.log_decision(_sample_state(), _sample_action())
    db.finalize_record(decision_id, {"reason": "TP", "pnl_usd": 1.23}, final_reward=1.0)

    output_csv = tmp_path / "ml_dataset.csv"
    builder = DatasetBuilder()
    builder.FEATURE_MAPS_PATH = str(tmp_path / "feature_maps.json")
    rows = builder.build_from_log(db.filepath, str(output_csv))

    assert rows == 1
    assert output_csv.exists()
