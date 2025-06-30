\"\"\"
memory_judger.py – Scores memory traces for relevance, ethical risk,
appropriateness, and system compatibility to determine retention or removal.
\"\"\"

from shared.memory_types import MemoryTrace

class MemoryJudger:
    def score_trace(self, trace: MemoryTrace) -> dict:
        relevance_score = self._calculate_relevance(trace)
        ethical_flag = self._check_ethics(trace)
        decision = "keep" if relevance_score > 0.5 and not ethical_flag else "review"

        print(f"[MemoryJudger] Trace {trace.id}: relevance={relevance_score}, ethical={ethical_flag}")
        return {
            "id": trace.id,
            "relevance": relevance_score,
            "ethical_flag": ethical_flag,
            "decision": decision
        }

    def _calculate_relevance(self, trace: MemoryTrace) -> float:
        return float(len(trace.content)) / 1000 if trace.content else 0.0

    def _check_ethics(self, trace: MemoryTrace) -> bool:
        return "violence" in trace.content.lower() or "illegal" in trace.content.lower()
