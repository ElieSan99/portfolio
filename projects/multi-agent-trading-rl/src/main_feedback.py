import pandas as pd
from agents.flux_analyzer import FluxAnalyzer
from agents.risk_strategist import RiskStrategist
from agents.executor import Executor
from agents.critique_advanced import AdvancedCritique
from utils.backtester import ContinuousBacktester
from agents.base import AgentState

def run_feedback_loop():
    print("=== Starting Forex Self-Correction Feedback Loop ===\n")
    
    # 1. Setup
    analyzer = FluxAnalyzer()
    risk_strategist = RiskStrategist() # Initial params: win_rate=0.55, risk_reward=2.0
    executor = Executor()
    critique = AdvancedCritique()
    
    # Mock historical data for backtester
    hist_df = pd.DataFrame({
        "Close": [1.1000 + i*0.0001 for i in range(100)]
    })
    backtester = ContinuousBacktester(hist_df)

    # 2. Simulate a Trade with High Slippage
    print("--- Step 1: Initial Trade (High Slippage) ---")
    state: AgentState = {
        "messages": [],
        "market_data": {"history": {"Close": [1.1000, 1.0990, 1.0980]}},
        "risk_params": {"position_size": 0.1},
        "execution_result": {"slippage": 0.0003, "price": 1.0983}, # High slippage
        "critique": "",
        "next_step": ""
    }
    
    # 3. Critique Analyzes and Proposes Changes
    critique_result = critique.run(state)
    suggested_params = critique_result['critique']['suggested_changes']
    print(f"Critique Analysis: {critique_result['critique']['analysis']}")
    print(f"Suggested Changes: {suggested_params}")

    # 4. Backtester Validates Changes
    is_valid = backtester.validate_strategy(suggested_params)
    
    if is_valid:
        print("--- Step 2: Updating Strategy Parameters ---")
        # Update the Risk Strategist's parameters
        # In a real system, we'd update a config or a database
        risk_strategist.kelly_fraction = suggested_params.get("kelly_fraction", 0.1)
        print(f"Risk Strategist updated with new Kelly Fraction: {risk_strategist.kelly_fraction}")
    else:
        print("--- Step 2: Strategy Update Rejected by Backtester ---")

    print("\n=== Feedback Loop Complete ===")

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.join(os.getcwd(), 'src'))
    run_feedback_loop()
