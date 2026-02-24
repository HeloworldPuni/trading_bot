from src.core.allocator import BanditAllocator, StrategyPerformanceTracker


def test_strategy_performance_tracker_roundtrip(tmp_path):
    path = tmp_path / "perf.json"

    tracker = StrategyPerformanceTracker(window=8)
    tracker.record("MOMENTUM|BULL_TREND", 1.5)
    tracker.record("MOMENTUM|BULL_TREND", -0.7)
    tracker.record("BREAKOUT|TRANSITION", -1.2)
    tracker.save(str(path))

    loaded = StrategyPerformanceTracker(window=1)
    assert loaded.load(str(path)) is True

    assert loaded.window == 8
    assert list(loaded.history["MOMENTUM|BULL_TREND"]) == [1.5, -0.7]
    assert list(loaded.history["BREAKOUT|TRANSITION"]) == [-1.2]


def test_bandit_allocator_roundtrip(tmp_path):
    path = tmp_path / "bandit.json"

    bandit = BanditAllocator()
    bandit.record("MOMENTUM|BULL_TREND", 1.0)
    bandit.record("MOMENTUM|BULL_TREND", -0.2)
    bandit.record("SCALP|SIDEWAYS_LOW_VOL", 0.4)
    bandit.save(str(path))

    loaded = BanditAllocator()
    assert loaded.load(str(path)) is True

    assert loaded.total == 3
    assert loaded.counts["MOMENTUM|BULL_TREND"] == 2
    assert loaded.counts["SCALP|SIDEWAYS_LOW_VOL"] == 1
    assert abs(loaded.values["MOMENTUM|BULL_TREND"] - 0.4) < 1e-9
