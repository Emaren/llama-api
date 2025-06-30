# backend/agent_emergent_motivation.py
# Detects and tracks emergent motivational signals across agent groups.

from datetime import datetime

class AgentEmergentMotivation:
    def __init__(self):
        self.motivation_log = []  # [ {group_id, signal, description, timestamp} ]

    def log_signal(self, group_id: str, signal: str, description: str):
        entry = {
            "group_id": group_id,
            "signal": signal,
            "description": description,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.motivation_log.append(entry)
        return entry

    def get_signals(self, group_id: str = None):
        if group_id:
            return [m for m in self.motivation_log if m["group_id"] == group_id]
        return self.motivation_log
