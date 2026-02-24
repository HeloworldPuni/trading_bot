from src.execution.pov import POVOrder

def test_pov():
    print("\n[TEST] POV Execution (Phase 8)")
    # Order: Buy 1000. Rate: 10%
    pov = POVOrder(total_qty=1000.0, participation_rate=0.1)
    
    # Interval 1: Market Vol = 5000
    # Target = 5000 * 0.1 = 500
    # We should trade 500
    qty1 = pov.update_market_volume(5000.0)
    print(f"Interval 1 (Vol=5000): Trade {qty1:.2f}")
    
    if qty1 == 500.0:
        print("✅ PASSED: Correct initial participation")
    else:
        print(f"❌ FAILED: Expected 500, got {qty1}")
        
    pov.fill(qty1)
    
    # Interval 2: Market Vol = 2000
    # Target Total = (5000 + 2000) * 0.1 = 700
    # Filled so far = 500
    # Need = 200
    qty2 = pov.update_market_volume(2000.0)
    print(f"Interval 2 (Vol=2000): Trade {qty2:.2f}")
    
    if qty2 == 200.0:
        print("✅ PASSED: Correct accumulated participation")
    else:
        print(f"❌ FAILED: Expected 200, got {qty2}")

if __name__ == "__main__":
    test_pov()
