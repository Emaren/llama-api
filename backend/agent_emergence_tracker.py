# backend/agent_emergence_tracker.py
# Observes emergent behaviors and unexpected high-order patterns in agents.

from datetime import datetime

class AgentEmergenceTracker:
    def __init__(self):
        self.events = {}  # {agent_id: [ {pattern, context, timestamp} ]}

    def record_emergence(self, agent_id, pattern: str, context: str = ""):
        if agent_id not in self.events:
            self.events[agent_id] = []
        entry = {
            "pattern": pattern,
            "context": context,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.events[agent_id].append(entry)
        return entry

    def get_emergence_events(self, agent_id):
        return self.events.get(agent_id, [])
