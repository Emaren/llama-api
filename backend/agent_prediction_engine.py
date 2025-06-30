# backend/agent_prediction_engine.py
# Forecasts possible agent futures for planning, risk detection, and opportunity spotting.

from backend.memory_engine import MemoryEngine
from backend.context_engine import ContextEngine
from backend.project_tracker import ProjectTracker

class AgentPredictionEngine:
    def __init__(self):
        self.memory_engine = MemoryEngine()
        self.context_engine = ContextEngine()
        self.project_tracker = ProjectTracker()

    def predict_future(self, agent_id, horizon=3):
        memory = self.memory_engine.query_recent(agent_id)
        context = self.context_engine.analyze(memory)
        trajectory = self.project_tracker.project_trajectory(agent_id, context)

        predictions = {
            "agent_id": agent_id,
            "expected_tasks": trajectory.get("next_tasks", [])[:horizon],
            "risk_level": trajectory.get("risk_score", 0.0),
            "confidence": trajectory.get("confidence_score", 0.0)
        }

        return predictions
