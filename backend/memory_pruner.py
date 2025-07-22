"""
memory_pruner.py – Removes outdated, low-priority, or decayed memory entries
to free up space and maintain memory health.
"""

from backend.shared.memory_types import MemoryTrace
from backend.shared.memory_decay import should_prune
from typing import List

class MemoryPruner:
    def __init__(self):
        self.total_pruned = 0

    def prune(self, memory_traces: List[MemoryTrace]) -> List[MemoryTrace]:
        pruned = []
        for trace in memory_traces:
            if not should_prune(trace):
                pruned.append(trace)
            else:
                self.total_pruned += 1
        return pruned

    def report(self):
        return {
            "total_pruned": self.total_pruned
        }
