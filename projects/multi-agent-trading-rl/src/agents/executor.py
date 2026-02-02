import random
from .base import BaseAgent, AgentState

class Executor(BaseAgent):
    def __init__(self):
        super().__init__("Exécuteur")

    def run(self, state: AgentState) -> Dict[str, Any]:
        print(f"[{self.name}] Executing trade...")
        
        # Simulate slippage
        expected_price = state['market_data']['analysis'].get('price', 1.1000)
        slippage = random.uniform(-0.0002, 0.0002)
        actual_price = expected_price + slippage
        
        return {
            "messages": [f"{self.name}: Trade executed at {actual_price:.5f} (Slippage: {slippage:.5f})"],
            "execution_result": {
                "status": "FILLED",
                "price": actual_price,
                "slippage": slippage
            },
            "next_step": "critique"
        }
