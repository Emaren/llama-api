"""
memory_scorer.py – Calculates importance or retrieval priority score for memory traces
using a weighted combination of relevance, recency, and user engagement.
"""

import time
from shared.memory_types import MemoryTrace


class MemoryScorer:
    def __init__(self, weights=None):
        # Default weights for scoring dimensions
        self.weights = weights or {
            "relevance": 0.5,
            "recency": 0.3,
            "engagement": 0.2,
        }

    def score(self, trace: MemoryTrace, current_time: float = None) -> float:
        current_time = current_time or time.time()

        relevance = trace.metadata.get("relevance", 0)
        engagement = trace.metadata.get("engagement", 0)

        # Convert datetime to epoch timestamp if necessary
        if hasattr(trace, "timestamp") and hasattr(trace.timestamp, "timestamp"):
            age_seconds = current_time - trace.timestamp.timestamp()
        else:
            age_seconds = 0

        recency = max(0.0, 1.0 - age_seconds / (60 * 60 * 24))  # 1-day linear decay

        score = (
            relevance * self.weights["relevance"] +
            recency * self.weights["recency"] +
            engagement * self.weights["engagement"]
        )

        trace.score = score
        return score


def score_memory(content: str) -> float:
    """
    Quick stateless scoring for new memory content before deeper trace context is available.
    Boosts memory for name declarations or explicit memory cues.
    """
    content_lower = content.lower()

    if "my name is" in content_lower:
        return 10.0  # 🚀 Force high retention for names

    if any(kw in content_lower for kw in ["remember", "remind me", "don't forget"]):
        return 5.0  # Boost for memory-related intent

    return 1.0 if len(content.split()) > 3 else 0.5  # Default fallback
