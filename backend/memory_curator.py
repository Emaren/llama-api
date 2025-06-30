\"\"\"
memory_curator.py – Selects and preserves high-value memory traces that
contribute to identity, learning, or long-term planning.
\"\"\"

from backend.memory_scorer import MemoryScorer
from backend.memory_pruner import MemoryPruner
from shared.memory_types import MemoryTrace

class MemoryCurator:
    def __init__(self):
        self.scorer = MemoryScorer()
        self.pruner = MemoryPruner()

    def curate(self, memory_bank: list[MemoryTrace]) -> list[MemoryTrace]:
        print("[MemoryCurator] Scoring memories for curation...")
        scores = self.scorer.score(memory_bank)
        curated = [
            trace for trace, score in scores.items()
            if score >= 0.75  # Threshold for high-value
        ]
        print(f"[MemoryCurator] Curated {len(curated)} high-value memories.")
        return curated
