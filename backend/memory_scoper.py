"""
memory_scoper.py – Scopes relevant memory traces based on query intent
"""

from shared.memory_types import MemoryTrace


class MemoryScoper:
    def scope(self, traces: list[MemoryTrace], query: str) -> list[MemoryTrace]:
        query_lower = query.lower()

        # 🔍 Hard-coded identity check
        if any(p in query_lower for p in ["what's my name", "who am i", "do you remember me"]):
            return [
                t for t in traces
                if any(k in t.content.lower() for k in ["my name is", "i am", "remember my name"])
            ]

        # 🧠 Fallback: return last 10 traces
        return traces[-10:]

