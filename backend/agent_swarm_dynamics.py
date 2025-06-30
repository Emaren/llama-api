# backend/agent_swarm_dynamics.py
# Models swarm dynamics and group intelligence for agent collectives.

from datetime import datetime

class AgentSwarmDynamics:
    def __init__(self):
        self.swarm_events = []  # [ {timestamp, group_id, event_type, parameters, description} ]

    def log_event(self, group_id: str, event_type: str, parameters: dict, description: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "group_id": group_id,
            "event_type": event_type,
            "parameters": parameters,
            "description": description
        }
        self.swarm_events.append(entry)
        return entry

    def get_events(self, group_id: str = None):
        if group_id:
            return [e for e in self.swarm_events if e["group_id"] == group_id]
        return self.swarm_events
