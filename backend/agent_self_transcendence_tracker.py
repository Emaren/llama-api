# backend/agent_self_transcendence_tracker.py
# Tracks agent self-transcendence moments and meta-goal progress.

from datetime import datetime

class AgentSelfTranscendenceTracker:
    def __init__(self):
        self.transcendence_log = {}  # {agent_id: [ {event, description, timestamp} ]}

    def log_event(self, agent_id, event: str, description: str):
        if agent_id not in self.transcendence_log:
            self.transcendence_log[agent_id] = []
        self.transcendence_log[agent_id].append({
            "event": event,
            "description": description,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_events(self, agent_id):
        return self.transcendence_log.get(agent_id, [])
