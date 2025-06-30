\"\"\"
knowledge_auditor.py – Evaluates the factual integrity of stored knowledge.
Detects outdated, contradictory, or unsupported claims and flags them for review.
\"\"\"

from shared.vector_math import cosine_similarity
from shared.constants import KNOWLEDGE_VALIDITY_THRESHOLD

class KnowledgeAuditor:
    def __init__(self, memory_engine):
        self.memory_engine = memory_engine

    def audit_memory(self):
        memory_items = self.memory_engine.get_all_facts()
        inconsistencies = []

        for i, item in enumerate(memory_items):
            for j in range(i + 1, len(memory_items)):
                similarity = cosine_similarity(item["embedding"], memory_items[j]["embedding"])
                if similarity > 0.9 and item["content"] != memory_items[j]["content"]:
                    inconsistencies.append((item, memory_items[j]))

        return {
            "total_checked": len(memory_items),
            "inconsistencies_found": len(inconsistencies),
            "details": inconsistencies,
        }

    def flag_outdated(self, current_date):
        memory_items = self.memory_engine.get_all_facts()
        flagged = [
            item for item in memory_items
            if "timestamp" in item and (current_date - item["timestamp"]) > KNOWLEDGE_VALIDITY_THRESHOLD
        ]
        return flagged
