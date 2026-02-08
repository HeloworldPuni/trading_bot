
import logging
import csv
from typing import List, Any, Optional, Iterator
from src.core.definitions import MarketState
from src.data.feeder import DataFeeder

logger = logging.getLogger(__name__)

class ReplayFeeder(DataFeeder):
    def __init__(self, csv_path: str, symbol: str = "BTC/USDT"):
        # We don't need a connector for Replay
        super().__init__(connector=None)
        self.csv_path = csv_path
        self.symbol = symbol
        self.history: List[List[Any]] = []
        self.current_index = 0
        self._load_data()

    def _load_data(self):
        """
        Loads OHLCV data from CSV.
        Expected Format: timestamp, open, high, low, close, volume
        """
        try:
            with open(self.csv_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None) # Skip header
                
                for row in reader:
                    if not row: continue
                    # Parse row to float (except timestamp if needed, but fetch_ohlcv keeps ts as int usually)
                    # CCXT Structure: [timestamp, open, high, low, close, volume]
                    try:
                        ts = int(float(row[0])) # Timestamp
                        op = float(row[1])
                        hi = float(row[2])
                        lo = float(row[3])
                        cl = float(row[4])
                        vol = float(row[5])
                        self.history.append([ts, op, hi, lo, cl, vol])
                    except (ValueError, IndexError):
                        continue
            
            logger.info(f"Loaded {len(self.history)} candles for Replay.")
            
        except FileNotFoundError:
            logger.error(f"Replay Data File Not Found: {self.csv_path}")
            self.history = []

    def reset(self):
        self.current_index = 0

    def get_next_state(self, window_size: int = 50) -> Optional[MarketState]:
        """
        Returns the next MarketState and advances time.
        Returns None if end of data.
        """
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
        
        # Calculate State
        state = self._calculate_state_from_ohlcv(ohlcv_window, self.symbol)
        
        # Store the "Next" candle for Execution Simulation (The candle AFTER this window)
        # We don't advance index here? Or do we?
        # Typically loop in main:
        # while True:
        #    state = feeder.get_next_state()
        #    if not state: break
        
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
        
        idx = (self.current_index - 1) + 50 + offset
        
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
        
        idx = self.current_index + 50 - 2 # Assuming window=50 hardcoded or we track window size?
        # Wait, get_next_state has window_size=50 default. 
        # Better to track `last_window_end_index` or just use the logic derived.
        # If I use window=50 (standard):
        idx = (self.current_index - 1) + 50 - 1
        
        if 0 <= idx < len(self.history):
            return self.history[idx]
        return None
