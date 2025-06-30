\"\"\"
memory_scorer.py – Calculates importance or retrieval priority score for memory traces
using a weighted combination of relevance, recency, and user engagement.
\"\"\"

from shared.memory_types import MemoryTrace
import time

class MemoryScorer:
    def __init__(self, weights=None):
        # Default weights: adjust as needed
        self.weights = weights or {
            "relevance": 0.5,
            "recency": 0.3,
            "engagement": 0.2,
        }

    def score(self, trace: MemoryTrace, current_time: float) -> float:
        relevance = trace.metadata.get("relevance", 0)
        recency = max(0, 1 - (current_time - trace.timestamp) / (60 * 60 * 24))  # 1 day decay
        engagement = trace.metadata.get("engagement", 0)

        score = (
            relevance * self.weights["relevance"] +
            recency * self.weights["recency"] +
            engagement * self.weights["engagement"]
        )
        trace.score = score
        return score
