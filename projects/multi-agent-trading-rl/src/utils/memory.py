import os
from pinecone import Pinecone
from typing import Dict, Any, List

class VectorMemory:
    def __init__(self, api_key: str, index_name: str):
        self.pc = Pinecone(api_key=api_key)
        self.index = self.pc.Index(index_name)

    def store_state(self, vector: List[float], metadata: Dict[str, Any]):
        """Stores a market state in Pinecone."""
        self.index.upsert(
            vectors=[
                {
                    "id": metadata.get("trade_id", "unknown"),
                    "values": vector,
                    "metadata": metadata
                }
            ],
            namespace="forex_market_states"
        )

    def query_similar_states(self, vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Queries Pinecone for similar past market states."""
        results = self.index.query(
            namespace="forex_market_states",
            vector=vector,
            top_k=top_k,
            include_metadata=True
        )
        return results.to_dict().get('matches', [])
