from .base import BaseAgent, AgentState

class Critique(BaseAgent):
    def __init__(self):
        super().__init__("Critique")

    def run(self, state: AgentState) -> Dict[str, Any]:
        print(f"[{self.name}] Reflecting on trade performance...")
        
        exec_result = state.get('execution_result', {})
        slippage = exec_result.get('slippage', 0)
        
        reflection = ""
        if abs(slippage) > 0.0001:
            reflection = "High slippage detected. Consider adjusting execution timing or order type."
        else:
            reflection = "Execution was efficient. Strategy followed correctly."
            
        return {
            "messages": [f"{self.name}: {reflection}"],
            "critique": reflection,
            "next_step": "end"
        }
