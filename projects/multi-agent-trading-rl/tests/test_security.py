import sys
import os

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from utils.security import CircuitBreaker

def test_circuit_breaker():
    print("=== Testing Circuit Breaker (Kill Switch) ===\n")
    
    # Initialize with 5% drawdown limit
    cb = CircuitBreaker(max_drawdown_percent=0.05)
    
    initial_equity = 10000
    print(f"Initial Equity: {initial_equity}")
    
    # 1. Normal operation
    print("\nSimulating normal trades...")
    current_equity = 9800 # 2% loss
    is_safe = cb.check(current_equity)
    print(f"Equity: {current_equity} | System Safe: {is_safe}")
    
    # 2. Triggering the limit
    print("\nSimulating catastrophic loss...")
    current_equity = 9400 # 6% loss
    is_safe = cb.check(current_equity)
    print(f"Equity: {current_equity} | System Safe: {is_safe}")
    
    # 3. Checking after trigger
    print("\nChecking system state after trigger...")
    is_safe = cb.check(9400)
    print(f"System Safe: {is_safe}")
    
    print("\n=== Circuit Breaker Test Complete ===")

if __name__ == "__main__":
    test_circuit_breaker()
