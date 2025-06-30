# backend/agent_self_actualization_tracker.py
# Tracks agent progress toward self-actualization and growth.

from datetime import datetime

class AgentSelfActualizationTracker:
    def __init__(self):
        self.actualization_log = {}  # {agent_id: [ {goal, progress, timestamp} ]}

    def log_progress(self, agent_id, goal: str, progress: float):
        if agent_id not in self.actualization_log:
            self.actualization_log[agent_id] = []
        self.actualization_log[agent_id].append({
            "goal": goal,
            "progress": progress,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_progress(self, agent_id):
        return self.actualization_log.get(agent_id, [])
