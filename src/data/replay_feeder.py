
import logging
import csv
import io
from typing import List, Any, Optional, Iterator
from src.core.definitions import MarketState
from src.data.feeder import DataFeeder
from src.config import Config
from src.data.quality import validate_ohlcv

logger = logging.getLogger(__name__)

class ReplayFeeder(DataFeeder):
    def __init__(self, csv_path: str, symbol: str = "BTC/USDT"):
        # We don't need a connector for Replay
        super().__init__(connector=None)
        self.csv_path = csv_path
        self.symbol = symbol
        self.history: List[List[Any]] = []
        self.current_index = 0
        self._last_window_size = 50
        self._last_window_end: Optional[int] = None
        self._load_data()

    def _load_data(self):
        """
        Loads OHLCV data from CSV.
        Expected Format: timestamp, open, high, low, close, volume
        """
        def _load_with_encoding(encoding: str) -> int:
            skipped = 0
            loaded = 0
            try:
                with open(self.csv_path, 'r', encoding=encoding) as f:
                    reader = csv.reader(f)
                    _ = next(reader, None)  # Skip header
                    last_ts = None
                    for row in reader:
                        if not row:
                            continue
                        try:
                            ts = int(float(row[0]))  # Timestamp
                            op = float(row[1])
                            hi = float(row[2])
                            lo = float(row[3])
                            cl = float(row[4])
                            vol = float(row[5])
                            if last_ts is not None and ts <= last_ts:
                                skipped += 1
                                continue
                            last_ts = ts
                            self.history.append([ts, op, hi, lo, cl, vol])
                            loaded += 1
                        except (ValueError, IndexError):
                            skipped += 1
                            continue
            except UnicodeError:
                return 0
            if skipped:
                logger.warning(f"Skipped {skipped} invalid rows while loading replay data.")
            return loaded

        def _load_with_null_strip() -> int:
            skipped = 0
            loaded = 0
            try:
                raw = None
                with open(self.csv_path, "rb") as f:
                    raw = f.read()
                if not raw or b"\x00" not in raw:
                    return 0
                cleaned = raw.replace(b"\x00", b"")
                text = cleaned.decode("utf-8", errors="ignore")
                reader = csv.reader(io.StringIO(text))
                _ = next(reader, None)
                last_ts = None
                for row in reader:
                    if not row:
                        continue
                    try:
                        ts = int(float(row[0]))
                        op = float(row[1])
                        hi = float(row[2])
                        lo = float(row[3])
                        cl = float(row[4])
                        vol = float(row[5])
                        if last_ts is not None and ts <= last_ts:
                            skipped += 1
                            continue
                        last_ts = ts
                        self.history.append([ts, op, hi, lo, cl, vol])
                        loaded += 1
                    except (ValueError, IndexError):
                        skipped += 1
                        continue
            except Exception:
                return 0
            if skipped:
                logger.warning(f"Skipped {skipped} invalid rows while loading replay data.")
            return loaded

        try:
            loaded = _load_with_encoding("utf-8")
            if loaded == 0:
                self.history = []
                loaded = _load_with_encoding("utf-16")
            if loaded == 0:
                self.history = []
                loaded = _load_with_null_strip()
            logger.info(f"Loaded {len(self.history)} candles for Replay.")
        except FileNotFoundError:
            logger.error(f"Replay Data File Not Found: {self.csv_path}")
            self.history = []

    def reset(self):
        self.current_index = 0

    def get_next_state(self, window_size: Optional[int] = None) -> Optional[MarketState]:
        """
        Returns the next MarketState and advances time.
        Returns None if end of data.
        """
        if window_size is None:
            window_size = Config.LTF_LOOKBACK
        while True:
            # Ensure we have enough data for a full window
            if self.current_index + window_size > len(self.history):
                return None
            
        # Slice the window ending at current_index + window_size
        # Effectively: [current_index : current_index + window_size]
        # BUT WAIT.
        # "Replay mode must simulate live trading conditions."
        # If I am at step T, I should see data up to T.
        # The window should END at the current logical "Now".
        # So we advance the pointer.
        
        # Initial: index=0. Need 50 candles. Can't start until we have 50.
        # So loop should start from index=0 (relative to available range [0..N]).
        # Window = data[current_index : current_index + window_size]
        # The "Latest" candle is the last one in this slice.
        
            ohlcv_window = self.history[self.current_index : self.current_index + window_size]
            
            ok, issues = validate_ohlcv(ohlcv_window, min_len=window_size)
            if not ok:
                issue = issues[0] if issues else "unknown"
                logger.warning(f"Invalid replay window at index {self.current_index}: {issue}. Skipping.")
                self.current_index += 1
                continue
            
            # Calculate State
            state = self._calculate_state_from_ohlcv(ohlcv_window, self.symbol)
            
            # Track window boundaries for execution simulation
            self._last_window_size = window_size
            self._last_window_end = (self.current_index + window_size - 1)

            self.current_index += 1 # Advance for next call
            
            return state

    def get_future_candle(self, offset: int = 0) -> Optional[List[float]]:
        """
        Peek ahead for EXECUTION simulation only.
        offset=0 means the immediate next candle after the current state's last candle.
        """
        # current_index was incremented in get_next_state.
        # So current_index points to the START of the NEXT window.
        # The previous window was [i : i+50].
        # The last candle of previous state was at `i+50-1`.
        # The "Future" candle is at `i+50`.
        
        # Since we did `current_index += 1` already:
        # The previous start was `current_index - 1`.
        # The end of that window was `(current_index - 1) + 50`.
        # So the index of the candle immediately following the previous state is `current_index - 1 + 50`.
        
        if self._last_window_end is None:
            return None

        idx = self._last_window_end + 1 + offset
        
        if 0 <= idx < len(self.history):
            return self.history[idx]
        return None
    def get_latest_candle(self) -> Optional[List[float]]:
        """
        Returns the most recent candle that closed in the current state (Time T).
        Strictly PAST data relative to the decision point.
        """
        # current_index points to the start of the NEXT window.
        # The window used for state was [current_index-1 : current_index-1+window_size]
        # The last candle in that window is at index: current_index - 1 + window_size - 1 for array slice?
        # Let's trace get_next_state carefully:
        # ohlcv_window = self.history[self.current_index : self.current_index + window_size]
        # self.current_index += 1
        #
        # So providing the state, we effectively "consumed" the candle at `current_index+window_size-1`.
        # Since current_index is now incremented, the index of that candle is `current_index - 1 + window_size - 1` = `current_index + window_size - 2`.
        
        if self._last_window_end is None:
            return None

        idx = self._last_window_end
        
        if 0 <= idx < len(self.history):
            return self.history[idx]
        return None
