# backend/agent_emergent_intelligence.py
# Monitors and analyzes signals of emergent intelligence among agents.

from datetime import datetime

class AgentEmergentIntelligence:
    def __init__(self):
        self.events = []  # [ {timestamp, description, involved_agents, metric} ]

    def log_event(self, description: str, involved_agents: list, metric: float):
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "description": description,
            "involved_agents": involved_agents,
            "metric": metric
        }
        self.events.append(event)
        return event

    def get_events(self):
        return self.events

    def get_events_by_agent(self, agent_id):
        return [e for e in self.events if agent_id in e["involved_agents"]]
