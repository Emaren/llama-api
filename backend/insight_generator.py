\"\"\"
insight_generator.py – Synthesizes insights from memory clusters and reflection logs.
Useful for surfacing patterns, anomalies, and behavioral trends.
\"\"\"

from backend.memory_engine import MemoryEngine
from backend.reflection_engine import ReflectionEngine

class InsightGenerator:
    def __init__(self):
        self.memory_engine = MemoryEngine()
        self.reflection_engine = ReflectionEngine()

    def extract_patterns(self, session_id: str):
        memories = self.memory_engine.fetch_session_memories(session_id)
        return self._find_common_themes(memories)

    def generate_insight(self, session_id: str):
        reflections = self.reflection_engine.get_reflections(session_id)
        patterns = self.extract_patterns(session_id)
        return {
            "themes": patterns,
            "reflections": reflections,
            "summary": self._summarize(patterns, reflections),
        }

    def _find_common_themes(self, memories):
        keywords = [m["keywords"] for m in memories if "keywords" in m]
        flat_keywords = [kw for sublist in keywords for kw in sublist]
        return list(set(flat_keywords))

    def _summarize(self, patterns, reflections):
        return f"Key themes: {', '.join(patterns)}. Reflections captured: {len(reflections)}."
