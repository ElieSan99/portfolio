import time
from typing import Dict, Any

class CircuitBreaker:
    def __init__(self, max_drawdown_percent: float = 0.05, window_seconds: int = 3600):
        """
        :param max_drawdown_percent: Maximum allowed loss (e.g., 0.05 for 5%)
        :param window_seconds: Time window for the drawdown calculation
        """
        self.max_drawdown_percent = max_drawdown_percent
        self.window_seconds = window_seconds
        self.is_active = True
        self.initial_equity = None
        self.start_time = time.time()

    def check(self, current_equity: float) -> bool:
        """
        Checks if the circuit breaker should trigger.
        Returns True if the system is SAFE, False if it should SHUT DOWN.
        """
        if not self.is_active:
            return False

        if self.initial_equity is None:
            self.initial_equity = current_equity
            return True

        # Reset window if time elapsed
        if time.time() - self.start_time > self.window_seconds:
            print("[CircuitBreaker] Window reset.")
            self.initial_equity = current_equity
            self.start_time = time.time()

        drawdown = (self.initial_equity - current_equity) / self.initial_equity
        
        if drawdown >= self.max_drawdown_percent:
            print(f"!!! CIRCUIT BREAKER TRIGGERED !!! Drawdown: {drawdown:.2%}")
            self.trigger_kill_switch()
            return False

        return True

    def trigger_kill_switch(self):
        """
        Emergency shutdown logic.
        """
        self.is_active = False
        print("[CircuitBreaker] EMERGENCY SHUTDOWN: Closing all API connections...")
        # In a real system:
        # 1. Close all open positions via Broker API
        # 2. Revoke API tokens
        # 3. Send Telegram/Slack alert
        # 4. Set system state to 'MANUAL_ONLY'
