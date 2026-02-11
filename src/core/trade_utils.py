from typing import Tuple
from src.config import Config


def get_trade_mode(regime: str, trend_strength: str) -> Tuple[str, float, float]:
    """
    Determine trade mode (SCALP vs SWING) based on market conditions.
    Returns (mode, tp_pct, sl_pct).
    """
    if trend_strength in ["STRONG", "VERY_STRONG"]:
        if "BULL" in regime or "BEAR" in regime:
            return "SWING", Config.SWING_TP_PCT, Config.SWING_SL_PCT
    return "SCALP", Config.SCALP_TP_PCT, Config.SCALP_SL_PCT


def expected_value(confidence: float, tp_pct: float, sl_pct: float) -> float:
    """
    Expected value in percent terms.
    EV = p * TP - (1-p) * SL
    """
    return (confidence * tp_pct) - ((1 - confidence) * sl_pct)


def calculate_tp_sl(entry_price: float, direction: str, atr: float, regime: str, trend_strength: str) -> Tuple[str, float, float, float, float]:
    """
    Calculate TP/SL prices using ATR multipliers when enabled.
    Returns (trade_mode, tp_price, sl_price, tp_pct, sl_pct).
    """
    trade_mode, tp_pct_cfg, sl_pct_cfg = get_trade_mode(regime, trend_strength)
    tp_dist = entry_price * (tp_pct_cfg / 100)
    sl_dist = entry_price * (sl_pct_cfg / 100)

    if Config.ATR_TP_SL_ENABLED and atr > 0:
        if trade_mode == "SWING":
            tp_dist = atr * Config.ATR_TP_MULTIPLIER_SWING
            sl_dist = atr * Config.ATR_SL_MULTIPLIER_SWING
        else:
            tp_dist = atr * Config.ATR_TP_MULTIPLIER_SCALP
            sl_dist = atr * Config.ATR_SL_MULTIPLIER_SCALP
        # Ensure minimum distance based on config % to avoid ultra-tight stops
        tp_dist = max(tp_dist, entry_price * (tp_pct_cfg / 100))
        sl_dist = max(sl_dist, entry_price * (sl_pct_cfg / 100))

    if direction == "LONG":
        tp_price = entry_price + tp_dist
        sl_price = entry_price - sl_dist
    else:
        tp_price = entry_price - tp_dist
        sl_price = entry_price + sl_dist

    tp_pct = (tp_dist / entry_price) * 100 if entry_price > 0 else tp_pct_cfg
    sl_pct = (sl_dist / entry_price) * 100 if entry_price > 0 else sl_pct_cfg
    return trade_mode, tp_price, sl_price, tp_pct, sl_pct
