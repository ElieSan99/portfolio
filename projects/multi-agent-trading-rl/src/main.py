from typing import Dict, Any
from langgraph.graph import StateGraph, END
from .agents.flux_analyzer import FluxAnalyzer
from .agents.risk_strategist import RiskStrategist
from .agents.executor import Executor
from .agents.critique import Critique
from .agents.base import AgentState

def create_trading_graph():
    # Initialize agents
    analyzer = FluxAnalyzer()
    risk_strategist = RiskStrategist()
    executor = Executor()
    critique = Critique()

    # Define the graph
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("flux_analyzer", analyzer.run)
    workflow.add_node("risk_strategist", risk_strategist.run)
    workflow.add_node("executor", executor.run)
    workflow.add_node("critique", critique.run)

    # Define edges
    workflow.set_entry_point("flux_analyzer")

    def route_after_analyzer(state: AgentState):
        return state.get("next_step", "end")

    def route_after_risk(state: AgentState):
        return state.get("next_step", "end")

    workflow.add_conditional_edges(
        "flux_analyzer",
        route_after_analyzer,
        {
            "risk_strategist": "risk_strategist",
            "end": END
        }
    )

    workflow.add_conditional_edges(
        "risk_strategist",
        route_after_risk,
        {
            "executor": "executor",
            "end": END
        }
    )

    workflow.add_edge("executor", "critique")
    workflow.add_edge("critique", END)

    return workflow.compile()

if __name__ == "__main__":
    # Example usage
    import pandas as pd
    
    graph = create_trading_graph()
    
    initial_state = {
        "messages": [],
        "market_data": {
            "history": {
                "Close": [1.1000, 1.1005, 1.1010, 1.0990, 1.0980, 1.0970, 1.0960] # Simulating oversold for RSI
            }
        },
        "risk_params": {},
        "execution_result": {},
        "critique": "",
        "next_step": ""
    }
    
    final_state = graph.invoke(initial_state)
    print("\n--- Final State ---")
    for msg in final_state['messages']:
        print(msg)
