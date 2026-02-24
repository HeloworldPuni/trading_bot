import math

from src.config import Config
from src.core.portfolio import Portfolio


def _new_portfolio(tmp_path, initial=1000.0):
    p = Portfolio(initial_balance=initial, load_state=False)
    p.state_file = str(tmp_path / "portfolio_state_test.json")
    return p


def test_loss_is_capped_by_margin_and_marked_liquidated(tmp_path):
    p = _new_portfolio(tmp_path, initial=1000.0)
    assert p.open_position(
        "BTC/USDC",
        "SHORT",
        entry_price=100.0,
        size_usd=500.0,
        tp=90.0,
        sl=105.0,
        decision_id="liq-1",
        leverage=5,
    )

    p.update_metrics("BTC/USDC", current_price=1000.0)
    pos = p.get_all_positions()[0]
    assert pos["liquidation_flag"] is True
    assert math.isclose(pos["unrealized_pnl_usd"], -100.0, rel_tol=0, abs_tol=1e-9)

    closed = p.close_position("BTC/USDC", exit_price=1000.0, reason="SL", decision_id="liq-1")
    assert closed is not None
    assert closed["liquidated"] is True
    assert closed["exit_reason"] == "LIQUIDATED"
    assert closed["loss_category"] == "LIQUIDATION"
    # gross loss capped to margin=100, net adds fees (entry + exit)
    assert math.isclose(closed["realized_pnl_usd"], -100.36, rel_tol=0, abs_tol=1e-6)
    assert math.isclose(p.balance, 899.64, rel_tol=0, abs_tol=1e-6)


def test_flat_round_trip_charges_each_fee_once(tmp_path):
    p = _new_portfolio(tmp_path, initial=1000.0)
    assert p.open_position(
        "ETH/USDC",
        "LONG",
        entry_price=100.0,
        size_usd=100.0,
        tp=110.0,
        sl=90.0,
        decision_id="flat-1",
        leverage=1,
    )
    p.update_metrics("ETH/USDC", current_price=100.0)
    closed = p.close_position("ETH/USDC", exit_price=100.0, reason="EXIT", decision_id="flat-1")
    assert closed is not None
    # 0.04 entry fee + 0.04 exit fee
    assert math.isclose(closed["realized_pnl_usd"], -0.08, rel_tol=0, abs_tol=1e-9)
    assert math.isclose(p.balance, 999.92, rel_tol=0, abs_tol=1e-9)


def test_exit_fee_never_negative_on_wipeout(tmp_path):
    p = _new_portfolio(tmp_path, initial=1000.0)
    assert p.open_position(
        "SOL/USDC",
        "LONG",
        entry_price=100.0,
        size_usd=100.0,
        tp=110.0,
        sl=90.0,
        decision_id="wipe-1",
        leverage=1,
    )
    p.update_metrics("SOL/USDC", current_price=0.0)
    closed = p.close_position("SOL/USDC", exit_price=0.0, reason="SL", decision_id="wipe-1")
    assert closed is not None
    assert closed["exit_fee"] >= 0.0
    assert math.isclose(closed["exit_fee"], 0.0, rel_tol=0, abs_tol=1e-9)
    assert math.isclose(closed["realized_pnl_usd"], -100.04, rel_tol=0, abs_tol=1e-9)
