import pandas as pd
import ta
from .base import BaseAgent, AgentState

class FluxAnalyzer(BaseAgent):
    def __init__(self):
        super().__init__("Analyseur de Flux")

    def analyze_technical(self, df: pd.DataFrame) -> Dict[str, Any]:
        # Simple technical analysis using 'ta' library
        rsi = ta.momentum.RSIIndicator(df['Close']).rsi()
        macd = ta.trend.MACD(df['Close']).macd()
        
        last_rsi = rsi.iloc[-1]
        last_macd = macd.iloc[-1]
        
        signal = "HOLD"
        if last_rsi < 30:
            signal = "BUY"
        elif last_rsi > 70:
            signal = "SELL"
            
        return {
            "rsi": last_rsi,
            "macd": last_macd,
            "signal": signal
        }

    def run(self, state: AgentState) -> Dict[str, Any]:
        print(f"[{self.name}] Analyzing market flux...")
        # In a real scenario, we'd fetch data here or use state['market_data']
        # For now, we assume market_data contains a DataFrame or similar
        df = pd.DataFrame(state['market_data']['history'])
        tech_analysis = self.analyze_technical(df)
        
        return {
            "messages": [f"{self.name}: Signal identified as {tech_analysis['signal']}"],
            "market_data": {**state['market_data'], "analysis": tech_analysis},
            "next_step": "risk_strategist" if tech_analysis['signal'] != "HOLD" else "end"
        }
