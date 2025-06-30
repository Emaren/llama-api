# backend/agent_innovation_tracker.py
# Observes and logs innovative behaviors and experimental actions.

from datetime import datetime

class AgentInnovationTracker:
    def __init__(self):
        self.innovations = {}  # {agent_id: [ {idea, context, timestamp} ]}

    def log_innovation(self, agent_id, idea: str, context: str = ""):
        if agent_id not in self.innovations:
            self.innovations[agent_id] = []
        entry = {
            "idea": idea,
            "context": context,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.innovations[agent_id].append(entry)
        return entry

    def get_innovation_history(self, agent_id):
        return self.innovations.get(agent_id, [])
