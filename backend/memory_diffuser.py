\"\"\"
memory_diffuser.py – Spreads key memory attributes (themes, sentiment, tags)
to related traces to enhance memory network cohesion.
\"\"\"

from shared.memory_types import MemoryTrace
from shared.vector_math import cosine_similarity

class MemoryDiffuser:
    def diffuse(self, memory_bank: list[MemoryTrace], core_memory: MemoryTrace) -> list[MemoryTrace]:
        print(f"[MemoryDiffuser] Diffusing traits from: {core_memory.id}")
        for trace in memory_bank:
            sim = cosine_similarity(core_memory.embedding, trace.embedding)
            if sim > 0.85:
                trace.tags.update(core_memory.tags)
                trace.annotations.append(f"Enriched via {core_memory.id}")
        return memory_bank
