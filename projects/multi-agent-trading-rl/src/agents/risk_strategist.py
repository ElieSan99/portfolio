import numpy as np
from .base import BaseAgent, AgentState

class RiskStrategist(BaseAgent):
    def __init__(self, win_rate=0.55, risk_reward=2.0):
        super().__init__("Stratège de Risque")
        self.win_rate = win_rate
        self.risk_reward = risk_reward

    def calculate_kelly(self) -> float:
        # Kelly Criterion: f* = (bp - q) / b
        # b = odds (risk/reward), p = win rate, q = loss rate
        b = self.risk_reward
        p = self.win_rate
        q = 1 - p
        kelly_f = (b * p - q) / b
        return max(0, kelly_f * 0.2)  # Fractional Kelly (20% of Kelly) for safety

    def run(self, state: AgentState) -> Dict[str, Any]:
        print(f"[{self.name}] Calculating risk parameters...")
        
        kelly_fraction = self.calculate_kelly()
        
        # Simple VaR simulation (placeholder)
        var_limit = 0.02 # 2% max loss per trade
        
        risk_ok = kelly_fraction > 0
        
        return {
            "messages": [f"{self.name}: Risk assessment complete. Kelly fraction: {kelly_fraction:.4f}"],
            "risk_params": {
                "position_size": kelly_fraction,
                "max_loss": var_limit,
                "risk_ok": risk_ok
            },
            "next_step": "executor" if risk_ok else "end"
        }
