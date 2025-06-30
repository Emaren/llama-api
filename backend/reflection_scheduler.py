\"\"\"
reflection_scheduler.py – Schedules and prioritizes reflection tasks based on
session context, memory salience, and engagement patterns.
\"\"\"

from backend.memory_metrics import MemoryMetrics
from backend.engagement_predictor import EngagementPredictor

class ReflectionScheduler:
    def __init__(self):
        self.metrics = MemoryMetrics()
        self.predictor = EngagementPredictor()

    def schedule(self, session_id: str, memory_set: list) -> list:
        scored = self.metrics.score_memories(memory_set)
        sorted_memories = sorted(scored, key=lambda x: x["importance"], reverse=True)

        high_engagement = self.predictor.predict(session_id) > 0.75
        count = 5 if high_engagement else 2

        return sorted_memories[:count]
