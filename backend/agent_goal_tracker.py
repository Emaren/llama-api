# backend/agent_goal_tracker.py
# Tracks progress of agent goals and updates status dynamically.

from datetime import datetime

class AgentGoalTracker:
    def __init__(self):
        self.agent_goals = {}  # {agent_id: [{goal, status, timestamp}]}

    def update_goal_status(self, agent_id, goal, status):
        if agent_id not in self.agent_goals:
            self.agent_goals[agent_id] = []
        self.agent_goals[agent_id].append({
            "goal": goal,
            "status": status,
            "updated_at": self._now()
        })

    def get_goal_status(self, agent_id):
        return self.agent_goals.get(agent_id, [])

    def detect_stalled_goals(self, agent_id, threshold_minutes=30):
        now = datetime.utcnow()
        stalled = []
        for entry in self.agent_goals.get(agent_id, []):
            delta = now - entry["updated_at"]
            if entry["status"] != "completed" and delta.total_seconds() > threshold_minutes * 60:
                stalled.append(entry["goal"])
        return stalled

    def _now(self):
        return datetime.utcnow()
