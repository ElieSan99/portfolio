import sys
import os
import pandas as pd

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from main import create_trading_graph

def run_verification():
    print("=== Starting Forex Multi-Agent System Verification ===\n")
    
    graph = create_trading_graph()
    
    # Test Case: Oversold Market (RSI < 30)
    print("--- Test Case: Oversold Market ---")
    initial_state = {
        "messages": [],
        "market_data": {
            "history": {
                "Close": [1.1000, 1.1005, 1.1010, 1.0990, 1.0980, 1.0970, 1.0960] 
            },
            "pair": "EUR_USD"
        },
        "risk_params": {},
        "execution_result": {},
        "critique": "",
        "next_step": ""
    }
    
    final_state = graph.invoke(initial_state)
    
    print("\nExecution Flow Messages:")
    for msg in final_state['messages']:
        print(f"  - {msg}")
        
    print(f"\nFinal Decision: {final_state.get('next_step', 'N/A')}")
    print(f"Execution Status: {final_state.get('execution_result', {}).get('status', 'NOT_EXECUTED')}")
    print(f"Critique: {final_state.get('critique', 'None')}")
    
    print("\n=== Verification Complete ===")

if __name__ == "__main__":
    run_verification()
