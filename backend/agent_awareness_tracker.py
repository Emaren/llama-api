# backend/agent_awareness_tracker.py
# Tracks changes in agent self-awareness state for audit and debugging.

from collections import deque
from datetime import datetime

class AgentAwarenessTracker:
    def __init__(self, max_history=10):
        self.history = {}  # {agent_id: deque([awareness_state])}
        self.max_history = max_history

    def record_awareness(self, agent_id, state):
        if agent_id not in self.history:
            self.history[agent_id] = deque(maxlen=self.max_history)
        self.history[agent_id].append({
            "timestamp": datetime.utcnow().isoformat(),
            "state": state
        })

    def get_history(self, agent_id):
        return list(self.history.get(agent_id, []))

    def detect_conflict(self, agent_id):
        entries = self.get_history(agent_id)
        if len(entries) < 2:
            return False
        recent = entries[-1]["state"]
        prev = entries[-2]["state"]
        return recent["role"] != prev["role"] or recent["context"] != prev["context"]
