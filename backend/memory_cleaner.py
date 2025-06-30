\"\"\"
memory_cleaner.py – Prunes low-utility, expired, or irrelevant memory items
to optimize memory engine performance and accuracy.
\"\"\"

from backend.memory_metrics import MemoryMetrics
from backend.memory_pruner import MemoryPruner
from shared.memory_types import MemoryTrace
from datetime import datetime, timedelta

class MemoryCleaner:
    def __init__(self):
        self.metrics = MemoryMetrics()
        self.pruner = MemoryPruner()

    def clean(self, memory_bank: list[MemoryTrace]) -> list[MemoryTrace]:
        print("[MemoryCleaner] Starting memory cleanup...")
        usage_scores = self.metrics.evaluate_usage(memory_bank)
        aged_out = [
            trace for trace in memory_bank
            if trace.timestamp < datetime.utcnow() - timedelta(days=30)
        ]
        low_score = [
            trace for trace, score in usage_scores.items()
            if score < 0.2
        ]
        to_prune = set(aged_out + low_score)
        cleaned_memory = self.pruner.prune(memory_bank, to_prune)
        print(f"[MemoryCleaner] Pruned {len(to_prune)} traces.")
        return cleaned_memory
