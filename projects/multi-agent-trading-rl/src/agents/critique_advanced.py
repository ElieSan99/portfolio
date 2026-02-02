import json
from typing import Dict, Any, List
from .base import BaseAgent, AgentState

class AdvancedCritique(BaseAgent):
    def __init__(self, model_name="gpt-4"):
        super().__init__("Critique Avancé")
        self.model_name = model_name
        
    def get_system_prompt(self) -> str:
        return """
        Tu es un Expert Quant Trader et Analyste de Risque. 
        Ton rôle est d'analyser les logs de trading d'un agent autonome et de suggérer des ajustements d'hyperparamètres.
        
        Tu dois identifier :
        1. Les causes des pertes (ex: volatilité trop élevée, slippage excessif, signal technique faible).
        2. Les patterns de succès.
        3. Des ajustements précis pour l'agent 'Stratège de Risque'.
        
        Format de sortie attendu (JSON uniquement) :
        {
            "analysis": "Brève analyse textuelle",
            "suggested_changes": {
                "kelly_fraction": float, (0.0 à 1.0)
                "atr_multiplier": float, (ex: 1.5, 2.0)
                "risk_per_trade": float (ex: 0.01, 0.02)
            },
            "rationale": "Pourquoi ces changements ?"
        }
        """

    def format_logs(self, state: AgentState) -> str:
        logs = {
            "market_data": state.get("market_data", {}).get("analysis", {}),
            "execution": state.get("execution_result", {}),
            "risk_params": state.get("risk_params", {})
        }
        return json.dumps(logs, indent=2)

    def run(self, state: AgentState) -> Dict[str, Any]:
        print(f"[{self.name}] Analyzing logs and reflecting on strategy...")
        
        # In a real implementation, we would call the LLM here.
        # For this demonstration, we simulate the LLM response.
        
        logs_str = self.format_logs(state)
        
        # Simulated LLM Logic:
        # If slippage is high, suggest lowering exposure.
        # If ATR is high (volatility), suggest increasing ATR multiplier for stops.
        
        execution = state.get("execution_result", {})
        slippage = abs(execution.get("slippage", 0))
        
        if slippage > 0.00015:
            suggested_changes = {
                "kelly_fraction": 0.05, # Lower exposure
                "atr_multiplier": 2.5,  # Wider stops for volatility
                "risk_per_trade": 0.01
            }
            analysis = "High slippage and volatility detected in recent trades."
        else:
            suggested_changes = {
                "kelly_fraction": 0.1,
                "atr_multiplier": 2.0,
                "risk_per_trade": 0.02
            }
            analysis = "Performance is stable. Maintaining standard parameters."

        reflection = {
            "analysis": analysis,
            "suggested_changes": suggested_changes,
            "rationale": "Automated reflection based on execution logs."
        }
        
        return {
            "messages": [f"{self.name}: {reflection['analysis']}"],
            "critique": reflection,
            "next_step": "backtester"
        }
