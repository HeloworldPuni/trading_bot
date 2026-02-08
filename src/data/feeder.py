
import logging
import datetime
import math
from typing import List, Dict, Any, Optional
from src.core.definitions import MarketState, MarketRegime, VolatilityLevel, TrendStrength
from src.exchange.connector import BinanceConnector
from src.data.quality import validate_ohlcv
from src.config import Config

logger = logging.getLogger(__name__)

class DataFeeder:
    def __init__(self, connector: Optional[BinanceConnector]):
        self.connector = connector

    def get_current_state(self, symbol: str, open_positions: int = 0) -> MarketState:
        """
        Fetches data and constructs the MarketState.
        """
        if not self.connector:
             return self._create_safe_state(symbol, open_positions)

        limit = max(50, Config.LTF_LOOKBACK)
        ohlcv = self.connector.fetch_ohlcv(symbol, Config.SCAN_TIMEFRAME, limit=limit)
        
        if not ohlcv or len(ohlcv) < 50:
             # Fallback to Safe State if data missing
             logger.warning(f"Insufficient data for {symbol}, returning SAFE state.")
             return self._create_safe_state(symbol, open_positions)
        
        ok, issues = validate_ohlcv(ohlcv, min_len=50)
        if not ok:
            issue = issues[0] if issues else "unknown"
            logger.warning(f"Invalid OHLCV for {symbol}: {issue}. Returning SAFE state.")
            return self._create_safe_state(symbol, open_positions)

        # Fetch funding rate for anticipatory regime detection
        funding_rate = self.connector.fetch_funding_rate(symbol)
        
        return self._calculate_state_from_ohlcv(ohlcv, symbol, open_positions, funding_rate)

    def _calculate_state_from_ohlcv(self, ohlcv: List[Any], symbol: str = "BTC/USDT", open_positions: int = 0, funding_rate: float = 0.0) -> MarketState:
        # Parse basic data (close prices)
        closes = [float(x[4]) for x in ohlcv]
        last_close = closes[-1]
        raw_ts = ohlcv[-1][0] # Timestamp in ms
        
        # --- Indicators ---
        sma_20 = sum(closes[-20:]) / 20
        sma_50 = sum(closes[-50:]) / 50
        trend_spread = ((sma_20 - sma_50) / sma_50) * 100
        
        rsi = self._calculate_rsi(closes)
        
        # Phase 31: Advanced Indicators
        macd, macd_sig, macd_hist = self._calculate_macd(closes)
        bb_upper, bb_mid, bb_lower = self._calculate_bollinger_bands(closes)
        atr = self._calculate_atr(ohlcv)
        
        # Execution-aware features (last candle)
        last = ohlcv[-1]
        last_open = float(last[1])
        last_high = float(last[2])
        last_low = float(last[3])
        last_close = float(last[4])
        prev_close = float(ohlcv[-2][4]) if len(ohlcv) > 1 else last_close
        spread_pct = ((last_high - last_low) / last_close) * 100 if last_close > 0 else 0.0
        body_pct = (abs(last_close - last_open) / last_close) * 100 if last_close > 0 else 0.0
        gap_pct = ((last_open - prev_close) / prev_close) * 100 if prev_close > 0 else 0.0
        volumes = [float(x[5]) for x in ohlcv]
        vol_mean = sum(volumes) / len(volumes) if volumes else 0.0
        vol_var = sum((v - vol_mean) ** 2 for v in volumes) / len(volumes) if volumes else 0.0
        vol_std = math.sqrt(vol_var) if vol_var > 0 else 0.0
        volume_zscore = ((volumes[-1] - vol_mean) / vol_std) if vol_std > 0 else 0.0
        liquidity_proxy = (volumes[-1] / atr) if atr > 0 else 0.0
        
        high_50 = max([float(x[2]) for x in ohlcv[-50:]])
        low_50 = min([float(x[3]) for x in ohlcv[-50:]])
        dist_to_high = ((high_50 - last_close) / last_close) * 100
        dist_to_low = ((last_close - low_50) / last_close) * 100

        # Volatility (ATR-based categorization) - must come BEFORE regime assignment
        vol_level = VolatilityLevel.NORMAL
        if atr < (last_close * 0.005): # < 0.5% movement
            vol_level = VolatilityLevel.LOW
        elif atr > (last_close * 0.02): # > 2% movement
            vol_level = VolatilityLevel.HIGH

        # Regime Detection - uses volatility to pick correct sideways variant
        if last_close > sma_20 > sma_50:
            regime = MarketRegime.BULL_TREND
        elif last_close < sma_20 < sma_50:
            regime = MarketRegime.BEAR_TREND
        elif vol_level == VolatilityLevel.HIGH:
            regime = MarketRegime.SIDEWAYS_HIGH_VOL
        else:
            regime = MarketRegime.SIDEWAYS_LOW_VOL
            
        # Session & Context (UTC)
        dt = datetime.datetime.fromtimestamp(raw_ts / 1000, tz=datetime.timezone.utc)
        hour = dt.hour
        session = "OTHER"
        if 0 <= hour < 8: session = "ASIA"
        elif 8 <= hour < 13: session = "LONDON"
        elif 13 <= hour < 16: session = "OVERLAP"
        elif 16 <= hour < 21: session = "NY"
        
        day_type = "WEEKEND" if dt.weekday() >= 5 else "WEEKDAY"
        # Trend Strength based on spread
        strength = TrendStrength.WEAK
        if abs(trend_spread) > 2.0: strength = TrendStrength.STRONG
        elif abs(trend_spread) > 0.5: strength = TrendStrength.MODERATE

        # Phase C: Anticipatory Regime Detection
        # Regime Confidence: How clear is the current regime signal?
        regime_confidence = self._calculate_regime_confidence(closes, sma_20, sma_50, macd_hist)
        
        # Momentum Shift Score: -1 (strong bearish shift) to +1 (strong bullish shift)
        momentum_shift_score = self._calculate_momentum_shift(closes, macd_hist, rsi)
        
        # Regime Stable: False if strong counter-momentum detected
        regime_stable = abs(momentum_shift_score) < 0.5
        
        # Higher timeframe features (resampled from LTF)
        htf_trend_spread = 0.0
        htf_rsi = 50.0
        htf_atr = 0.0
        ltf_minutes = self._timeframe_to_minutes(Config.SCAN_TIMEFRAME)
        htf_minutes = self._timeframe_to_minutes(Config.HTF_TIMEFRAME)
        if ltf_minutes and htf_minutes and htf_minutes > ltf_minutes:
            htf_ohlcv = self._resample_ohlcv(ohlcv, ltf_minutes, htf_minutes)
            if len(htf_ohlcv) >= Config.HTF_LOOKBACK:
                htf_closes = [float(x[4]) for x in htf_ohlcv]
                htf_sma_20 = sum(htf_closes[-20:]) / 20
                htf_sma_50 = sum(htf_closes[-50:]) / 50
                htf_trend_spread = ((htf_sma_20 - htf_sma_50) / htf_sma_50) * 100 if htf_sma_50 > 0 else 0.0
                htf_rsi = self._calculate_rsi(htf_closes)
                htf_atr = self._calculate_atr(htf_ohlcv)

        return MarketState(
            symbol=symbol,
            market_regime=regime,
            volatility_level=vol_level,
            trend_strength=strength,
            time_of_day=str(hour),
            trading_session=session,
            day_type=day_type,
            week_phase="MID", 
            time_remaining_days=30.0,
            distance_to_key_levels=dist_to_high, 
            rsi=rsi,
            trend_spread=trend_spread,
            dist_to_high=dist_to_high,
            dist_to_low=dist_to_low,
            macd=macd,
            macd_signal=macd_sig,
            macd_hist=macd_hist,
            bb_upper=bb_upper,
            bb_mid=bb_mid,
            bb_lower=bb_lower,
            atr=atr,
            volume_delta=0.0,
            spread_pct=spread_pct,
            body_pct=body_pct,
            gap_pct=gap_pct,
            volume_zscore=volume_zscore,
            liquidity_proxy=liquidity_proxy,
            funding_rate=funding_rate,
            funding_extreme=abs(funding_rate) > 0.1,  # Extreme if > 0.1%
            raw_timestamp=dt.isoformat(),
            current_risk_state="SAFE",
            current_drawdown_percent=0.0,
            current_open_positions=open_positions,
            # Phase C: Anticipatory Regime Detection
            regime_confidence=regime_confidence,
            regime_stable=regime_stable,
            momentum_shift_score=momentum_shift_score,
            htf_trend_spread=htf_trend_spread,
            htf_rsi=htf_rsi,
            htf_atr=htf_atr
        )

    def _calculate_rsi(self, prices: List[float], period: int = 14) -> float:
        if len(prices) < period + 1:
            return 50.0
        
        deltas = []
        for i in range(1, len(prices)):
            deltas.append(prices[i] - prices[i-1])
            
        gains = [d if d > 0 else 0 for d in deltas[-period:]]
        losses = [-d if d < 0 else 0 for d in deltas[-period:]]
        
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        if avg_loss == 0:
            return 100.0
        
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    def _timeframe_to_minutes(self, tf: str) -> int:
        if not tf:
            return 0
        tf = tf.strip().lower()
        if tf.endswith("m"):
            return int(tf[:-1])
        if tf.endswith("h"):
            return int(tf[:-1]) * 60
        if tf.endswith("d"):
            return int(tf[:-1]) * 60 * 24
        return 0

    def _resample_ohlcv(self, ohlcv: List[Any], ltf_minutes: int, htf_minutes: int) -> List[List[float]]:
        if not ohlcv or ltf_minutes <= 0 or htf_minutes <= 0:
            return []
        htf_ms = htf_minutes * 60 * 1000
        ratio = htf_minutes // ltf_minutes if ltf_minutes and htf_minutes % ltf_minutes == 0 else None

        buckets = {}
        for row in ohlcv:
            ts = int(row[0])
            bucket = (ts // htf_ms) * htf_ms
            buckets.setdefault(bucket, []).append(row)

        aggregated = []
        for bucket_ts in sorted(buckets.keys()):
            rows = buckets[bucket_ts]
            if ratio and len(rows) < ratio:
                continue
            op = float(rows[0][1])
            hi = max(float(r[2]) for r in rows)
            lo = min(float(r[3]) for r in rows)
            cl = float(rows[-1][4])
            vol = sum(float(r[5]) for r in rows)
            aggregated.append([bucket_ts, op, hi, lo, cl, vol])
        return aggregated

    def _calculate_ema(self, prices: List[float], period: int) -> float:
        if len(prices) < period:
            return sum(prices) / len(prices) if prices else 0.0
        alpha = 2 / (period + 1)
        ema = prices[0]
        for p in prices[1:]:
            ema = (p * alpha) + (ema * (1 - alpha))
        return ema

    def _calculate_macd(self, prices: List[float], slow=26, fast=12, signal=9) -> tuple:
        """
        Calculate MACD using single-pass O(n) incremental EMAs.
        Much more efficient than the previous O(n²) slice-based approach.
        """
        if len(prices) < slow + signal:
            return 0.0, 0.0, 0.0
        
        # Incremental EMA calculation
        alpha_fast = 2 / (fast + 1)
        alpha_slow = 2 / (slow + 1)
        alpha_signal = 2 / (signal + 1)
        
        # Initialize EMAs with first value
        ema_fast = prices[0]
        ema_slow = prices[0]
        
        # Single-pass through prices to build MACD series
        macd_series = []
        for i, price in enumerate(prices):
            ema_fast = (price * alpha_fast) + (ema_fast * (1 - alpha_fast))
            ema_slow = (price * alpha_slow) + (ema_slow * (1 - alpha_slow))
            
            # Start recording MACD values after slow period stabilizes
            if i >= slow - 1:
                macd_series.append(ema_fast - ema_slow)
        
        if not macd_series:
            return 0.0, 0.0, 0.0
            
        # Calculate signal line (EMA of MACD series)
        ema_signal = macd_series[0]
        for macd_val in macd_series:
            ema_signal = (macd_val * alpha_signal) + (ema_signal * (1 - alpha_signal))
        
        macd_line = macd_series[-1]
        macd_hist = macd_line - ema_signal
        
        return macd_line, ema_signal, macd_hist

    def _calculate_bollinger_bands(self, prices: List[float], period=20, std_dev=2) -> tuple:
        if len(prices) < period:
            return 0.0, 0.0, 0.0
        
        slice = prices[-period:]
        sma = sum(slice) / period
        variance = sum([(x - sma)**2 for x in slice]) / period
        stdev = variance**0.5
        
        upper = sma + (std_dev * stdev)
        lower = sma - (std_dev * stdev)
        return upper, sma, lower

    def _calculate_atr(self, ohlcv: List[Any], period=14) -> float:
        if len(ohlcv) < period + 1:
            return 0.0
        
        tr_list = []
        for i in range(len(ohlcv)-period, len(ohlcv)):
            h, l, c_prev = float(ohlcv[i][2]), float(ohlcv[i][3]), float(ohlcv[i-1][4])
            tr = max(h - l, abs(h - c_prev), abs(l - c_prev))
            tr_list.append(tr)
            
        return sum(tr_list) / period

    def _calculate_regime_confidence(self, closes: List[float], sma_20: float, sma_50: float, macd_hist: float) -> float:
        """
        Phase C: Calculate how confident we are in the current regime.
        Returns 0-1 score (higher = more confident regime signal).
        """
        if len(closes) < 2:
            return 0.5
            
        last_close = closes[-1]
        
        # Factor 1: Price distance from SMAs (further = stronger regime)
        dist_from_20 = abs(last_close - sma_20) / sma_20 if sma_20 > 0 else 0
        dist_from_50 = abs(last_close - sma_50) / sma_50 if sma_50 > 0 else 0
        distance_score = min((dist_from_20 + dist_from_50) * 10, 1.0)
        
        # Factor 2: SMA alignment (20 and 50 in same direction = confident)
        sma_aligned = 1.0 if (sma_20 > sma_50 and last_close > sma_20) or (sma_20 < sma_50 and last_close < sma_20) else 0.5
        
        # Factor 3: MACD histogram strength
        macd_strength = min(abs(macd_hist) / 100, 1.0) if macd_hist != 0 else 0.5
        
        # Weighted average
        confidence = (distance_score * 0.3 + sma_aligned * 0.4 + macd_strength * 0.3)
        return round(confidence, 3)
    
    def _calculate_momentum_shift(self, closes: List[float], macd_hist: float, rsi: float) -> float:
        """
        Phase C: Detect momentum shifts that could precede regime changes.
        Returns -1 to +1 (negative = bearish shift, positive = bullish shift).
        """
        if len(closes) < 10:
            return 0.0
            
        # Factor 1: Short-term vs long-term momentum
        short_momentum = (closes[-1] - closes[-5]) / closes[-5] if closes[-5] > 0 else 0
        long_momentum = (closes[-1] - closes[-10]) / closes[-10] if closes[-10] > 0 else 0
        
        # Divergence: Short-term reversing against long-term = potential shift
        momentum_divergence = 0.0
        if long_momentum > 0 and short_momentum < 0:
            momentum_divergence = -0.5  # Bullish slowing, potential bear shift
        elif long_momentum < 0 and short_momentum > 0:
            momentum_divergence = 0.5   # Bearish slowing, potential bull shift
            
        # Factor 2: RSI extremes
        rsi_signal = 0.0
        if rsi > 70:
            rsi_signal = -0.3  # Overbought, potential reversal down
        elif rsi < 30:
            rsi_signal = 0.3   # Oversold, potential reversal up
            
        # Factor 3: MACD histogram direction
        macd_signal = 0.0
        if macd_hist > 50:
            macd_signal = 0.2
        elif macd_hist < -50:
            macd_signal = -0.2
            
        shift_score = momentum_divergence + rsi_signal + macd_signal
        return round(max(-1.0, min(1.0, shift_score)), 3)

    def _create_safe_state(self, symbol: str = "BTC/USDT", open_positions: int = 0) -> MarketState:
        return MarketState(
            symbol=symbol,
            market_regime=MarketRegime.SIDEWAYS_LOW_VOL,
            volatility_level=VolatilityLevel.NORMAL,
            trend_strength=TrendStrength.WEAK,
            time_of_day="DEAD_ZONE",
            trading_session="ASIA",
            day_type="WEEKDAY",
            week_phase="MID",
            time_remaining_days=0.0,
            distance_to_key_levels=0.0,
            funding_extreme=False,
            current_risk_state="DANGER", # Force safety
            current_drawdown_percent=0.0,
            current_open_positions=open_positions
        )
