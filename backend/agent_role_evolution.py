# backend/agent_role_evolution.py
# Manages role transitions and evolution for long-term agent development.

from datetime import datetime

class AgentRoleEvolution:
    def __init__(self):
        self.history = {}  # {agent_id: [ {role, timestamp, reason} ]}

    def record_role(self, agent_id, role, reason="manual"):
        if agent_id not in self.history:
            self.history[agent_id] = []
        self.history[agent_id].append({
            "role": role,
            "timestamp": datetime.utcnow().isoformat(),
            "reason": reason
        })

    def get_role_history(self, agent_id):
        return self.history.get(agent_id, [])

    def suggest_next_role(self, agent_id):
        roles = [entry["role"] for entry in self.history.get(agent_id, [])]
        if not roles:
            return "observer"
        if roles[-1] == "analyst":
            return "strategist"
        if roles[-1] == "helper":
            return "innovator"
        return "analyst"
