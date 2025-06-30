# backend/agent_motivation_engine.py
# Models intrinsic and extrinsic motivation signals for agents.

from datetime import datetime

class AgentMotivationEngine:
    def __init__(self):
        self.motivation_log = {}  # {agent_id: [ {type, intensity, reason, timestamp} ]}

    def log_motivation(self, agent_id, type: str, intensity: float, reason: str):
        if agent_id not in self.motivation_log:
            self.motivation_log[agent_id] = []
        self.motivation_log[agent_id].append({
            "type": type,
            "intensity": max(0.0, min(intensity, 1.0)),
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_latest(self, agent_id):
        return self.motivation_log.get(agent_id, [])[-1] if self.motivation_log.get(agent_id) else None

    def get_history(self, agent_id):
        return self.motivation_log.get(agent_id, [])
