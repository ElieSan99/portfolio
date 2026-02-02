from typing import Annotated, TypedDict, List, Dict, Any
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # Messages for conversation history
    messages: Annotated[List[Dict[str, Any]], add_messages]
    # Market data context
    market_data: Dict[str, Any]
    # Risk parameters
    risk_params: Dict[str, Any]
    # Execution details
    execution_result: Dict[str, Any]
    # Critique feedback
    critique: str
    # Current step in the flow
    next_step: str

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self, state: AgentState) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement run()")
