import logging
from typing import List

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)


class MicrostructureFeatures:
    """
    Order-book and trade-flow feature utilities.
    """

    @staticmethod
    def _ensure_datetime_index(df: pd.DataFrame) -> pd.DataFrame:
        if isinstance(df.index, pd.DatetimeIndex):
            return df
        out = df.copy()
        if "timestamp" in out.columns:
            # Supports both ms epoch and parseable timestamps.
            ts = pd.to_datetime(out["timestamp"], unit="ms", errors="coerce")
            if ts.isna().all():
                ts = pd.to_datetime(out["timestamp"], errors="coerce")
            out.index = ts
        return out

    @staticmethod
    def _get_col(df: pd.DataFrame, names: List[str], default: float = 0.0) -> pd.Series:
        for name in names:
            if name in df.columns:
                return pd.to_numeric(df[name], errors="coerce").fillna(default)
        return pd.Series(default, index=df.index, dtype=float)

    @staticmethod
    def _best_levels(orderbook_df: pd.DataFrame):
        df = MicrostructureFeatures._ensure_datetime_index(orderbook_df)
        bid_p = MicrostructureFeatures._get_col(df, ["bid1_p", "bid0_p", "bid_price_0", "bids_0_price"])
        bid_v = MicrostructureFeatures._get_col(df, ["bid1_v", "bid0_v", "bid_qty_0", "bids_0_qty"])
        ask_p = MicrostructureFeatures._get_col(df, ["ask1_p", "ask0_p", "ask_price_0", "asks_0_price"])
        ask_v = MicrostructureFeatures._get_col(df, ["ask1_v", "ask0_v", "ask_qty_0", "asks_0_qty"])
        return df, bid_p, bid_v, ask_p, ask_v

    @staticmethod
    def calc_spread(orderbook_df: pd.DataFrame) -> pd.DataFrame:
        """
        Returns spread metrics:
        - spread_abs: ask-bid
        - spread_rel: percentage spread vs mid
        - mid_price
        """
        if orderbook_df is None or orderbook_df.empty:
            return pd.DataFrame(columns=["spread_abs", "spread_rel", "mid_price"])

        _, bid_p, _, ask_p, _ = MicrostructureFeatures._best_levels(orderbook_df)
        mid = (bid_p + ask_p) / 2.0
        spread_abs = (ask_p - bid_p).clip(lower=0.0)
        spread_rel = np.where(mid > 0, (spread_abs / mid) * 100.0, 0.0)

        out = pd.DataFrame(
            {
                "spread_abs": spread_abs.astype(float),
                "spread_rel": pd.Series(spread_rel, index=spread_abs.index, dtype=float),
                "mid_price": mid.astype(float),
            },
            index=spread_abs.index,
        )
        return out

    @staticmethod
    def calc_ofi(orderbook_df: pd.DataFrame) -> pd.Series:
        """
        Best-level Order Flow Imbalance (OFI) approximation.
        """
        if orderbook_df is None or orderbook_df.empty:
            return pd.Series(dtype=float)

        _, bid_p, bid_v, ask_p, ask_v = MicrostructureFeatures._best_levels(orderbook_df)

        bid_p_prev = bid_p.shift(1)
        ask_p_prev = ask_p.shift(1)
        bid_v_prev = bid_v.shift(1).fillna(0.0)
        ask_v_prev = ask_v.shift(1).fillna(0.0)

        bid_term = np.where(bid_p >= bid_p_prev, bid_v, -bid_v_prev)
        ask_term = np.where(ask_p <= ask_p_prev, ask_v, -ask_v_prev)

        ofi = pd.Series(bid_term - ask_term, index=bid_p.index, dtype=float).fillna(0.0)
        ofi.name = "ofi"
        return ofi

    @staticmethod
    def calc_tfi(bars_df: pd.DataFrame) -> pd.Series:
        """
        Trade Flow Imbalance proxy from bar data.
        """
        if bars_df is None or bars_df.empty:
            return pd.Series(dtype=float)

        df = bars_df.copy()
        if "buy_volume" in df.columns and "sell_volume" in df.columns:
            buy = pd.to_numeric(df["buy_volume"], errors="coerce").fillna(0.0)
            sell = pd.to_numeric(df["sell_volume"], errors="coerce").fillna(0.0)
            denom = (buy + sell).replace(0, np.nan)
            tfi = ((buy - sell) / denom).fillna(0.0)
        else:
            close = pd.to_numeric(df.get("close"), errors="coerce").fillna(method="ffill").fillna(0.0)
            open_ = pd.to_numeric(df.get("open"), errors="coerce").fillna(close)
            vol = pd.to_numeric(df.get("volume"), errors="coerce").fillna(0.0)
            sign = np.sign(close - open_)
            denom = vol.replace(0, np.nan)
            tfi = ((sign * vol) / denom).fillna(0.0)

        tfi.name = "tfi"
        return tfi.astype(float)

    @staticmethod
    def calc_vpin(bars_df: pd.DataFrame, window: int = 50) -> pd.Series:
        """
        VPIN approximation using rolling absolute trade imbalance.
        """
        if bars_df is None or bars_df.empty:
            return pd.Series(dtype=float)

        tfi = MicrostructureFeatures.calc_tfi(bars_df)
        vol = pd.to_numeric(bars_df.get("volume"), errors="coerce").fillna(0.0)
        imbalance = (tfi.abs() * vol).rolling(window=window, min_periods=max(2, window // 5)).sum()
        volume_roll = vol.rolling(window=window, min_periods=max(2, window // 5)).sum()
        vpin = (imbalance / volume_roll.replace(0, np.nan)).fillna(0.0)
        vpin.name = "vpin"
        return vpin.astype(float)

    @staticmethod
    def calculate_obi(bids: pd.DataFrame, asks: pd.DataFrame) -> float:
        """
        Order Book Imbalance in [-1, 1].
        """
        if bids is None or asks is None or bids.empty or asks.empty:
            return 0.0

        bid_qty = pd.to_numeric(bids.get("quantity"), errors="coerce").fillna(0.0).sum()
        ask_qty = pd.to_numeric(asks.get("quantity"), errors="coerce").fillna(0.0).sum()
        denom = bid_qty + ask_qty
        if denom <= 0:
            return 0.0
        return float((bid_qty - ask_qty) / denom)

    @staticmethod
    def detect_liquidity_gaps(
        bids: pd.DataFrame, asks: pd.DataFrame, threshold_pct: float = 0.1
    ) -> List[dict]:
        """
        Detect large adjacent price jumps in ladder levels.
        threshold_pct is percentage gap between consecutive levels.
        """
        gaps: List[dict] = []
        threshold = abs(float(threshold_pct)) / 100.0

        def _scan(side_df: pd.DataFrame, side: str):
            if side_df is None or side_df.empty or "price" not in side_df.columns:
                return
            prices = pd.to_numeric(side_df["price"], errors="coerce").dropna().sort_values(ascending=(side == "ask"))
            if len(prices) < 2:
                return
            for prev, curr in zip(prices.iloc[:-1], prices.iloc[1:]):
                if prev <= 0:
                    continue
                rel_gap = abs(curr - prev) / prev
                if rel_gap >= threshold:
                    gaps.append({"side": side, "from": float(prev), "to": float(curr), "gap_pct": float(rel_gap * 100.0)})

        _scan(bids, "bid")
        _scan(asks, "ask")
        return gaps

    @staticmethod
    def calculate_micro_price(bids: pd.DataFrame, asks: pd.DataFrame) -> float:
        """
        Micro-price weighted by opposite queue size.
        """
        if bids is None or asks is None or bids.empty or asks.empty:
            return 0.0

        try:
            bid_p = float(pd.to_numeric(bids.iloc[0]["price"], errors="coerce"))
            bid_q = float(pd.to_numeric(bids.iloc[0]["quantity"], errors="coerce"))
            ask_p = float(pd.to_numeric(asks.iloc[0]["price"], errors="coerce"))
            ask_q = float(pd.to_numeric(asks.iloc[0]["quantity"], errors="coerce"))
        except Exception:
            return 0.0

        denom = bid_q + ask_q
        if denom <= 0:
            return (bid_p + ask_p) / 2.0
        return float((ask_p * bid_q + bid_p * ask_q) / denom)


class LiquidityAnalyzer:
    """
    Compatibility helper for liquidity-gap calls.
    """

    @staticmethod
    def detect_liquidity_gaps(orderbook_df: pd.DataFrame, threshold_pct: float = 0.1) -> List[dict]:
        if orderbook_df is None or orderbook_df.empty:
            return []

        bids = []
        asks = []
        row = orderbook_df.iloc[-1]
        for i in range(1, 11):
            bp = row.get(f"bid{i}_p")
            bv = row.get(f"bid{i}_v")
            ap = row.get(f"ask{i}_p")
            av = row.get(f"ask{i}_v")
            if bp is not None and bv is not None:
                bids.append({"price": bp, "quantity": bv})
            if ap is not None and av is not None:
                asks.append({"price": ap, "quantity": av})

        bids_df = pd.DataFrame(bids)
        asks_df = pd.DataFrame(asks)
        return MicrostructureFeatures.detect_liquidity_gaps(bids_df, asks_df, threshold_pct=threshold_pct)
