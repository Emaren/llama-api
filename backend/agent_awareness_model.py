# backend/agent_awareness_model.py
# Tracks the agent’s internal state of self-awareness, roles, and operational context.

from datetime import datetime

class AgentAwarenessModel:
    def __init__(self):
        self.state = {}  # {agent_id: awareness_state}

    def update_awareness(self, agent_id, role, context, status="ready"):
        self.state[agent_id] = {
            "role": role,
            "context": context,
            "status": status,
            "updated_at": self._now()
        }

    def get_awareness(self, agent_id):
        return self.state.get(agent_id, {
            "role": None,
            "context": None,
            "status": "unknown",
            "updated_at": None
        })

    def _now(self):
        return datetime.utcnow().isoformat()
