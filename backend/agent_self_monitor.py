# backend/agent_self_monitor.py
# Tracks agent health and internal system status for early warning.

from datetime import datetime

class AgentSelfMonitor:
    def __init__(self):
        self.status_logs = {}  # {agent_id: [ {timestamp, status} ]}

    def log_status(self, agent_id, status: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "status": status
        }
        if agent_id not in self.status_logs:
            self.status_logs[agent_id] = []
        self.status_logs[agent_id].append(entry)

    def get_status_logs(self, agent_id):
        return self.status_logs.get(agent_id, [])
