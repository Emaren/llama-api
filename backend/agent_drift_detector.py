# backend/agent_drift_detector.py
# Detects when agents deviate from planned trajectories or tasks.

from datetime import datetime
from backend.agent_routine_planner import AgentRoutinePlanner

class AgentDriftDetector:
    def __init__(self):
        self.planner = AgentRoutinePlanner()

    def detect_drift(self, agent_id, current_task):
        routine = self.planner.get_routine(agent_id)
        if not routine:
            return {"drift": False, "reason": "No routine scheduled."}

        upcoming_tasks = [entry["task"] for entry in routine[:3]]
        if current_task not in upcoming_tasks:
            return {
                "drift": True,
                "reason": f"'{current_task}' not in upcoming routine tasks: {upcoming_tasks}"
            }

        return {"drift": False, "reason": "Aligned with routine."}
