# backend/agent_perception_tracker.py
# Tracks evolution of an agent's perception for diagnostics and adaptation.

from collections import deque
from datetime import datetime

class AgentPerceptionTracker:
    def __init__(self, max_history=20):
        self.perception_log = {}  # {agent_id: deque([perception_state])}
        self.max_history = max_history

    def record_perception(self, agent_id, perception_state):
        if agent_id not in self.perception_log:
            self.perception_log[agent_id] = deque(maxlen=self.max_history)
        self.perception_log[agent_id].append({
            "timestamp": datetime.utcnow().isoformat(),
            "state": perception_state
        })

    def get_recent_perceptions(self, agent_id):
        return list(self.perception_log.get(agent_id, []))

    def detect_anomaly(self, agent_id):
        history = self.perception_log.get(agent_id, [])
        if len(history) < 2:
            return False
        latest = history[-1]["state"]
        previous = history[-2]["state"]
        return self._significant_shift(latest, previous)

    def _significant_shift(self, latest, previous):
        # Placeholder logic for now
        return latest.get("context") != previous.get("context")
