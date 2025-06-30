# backend/agent_drive_controller.py
# Controls and tracks primary drives and instincts in agents.

from datetime import datetime

class AgentDriveController:
    def __init__(self):
        self.drive_log = {}  # {agent_id: [ {drive, level, satisfied, timestamp} ]}

    def log_drive(self, agent_id, drive: str, level: float, satisfied: bool):
        if agent_id not in self.drive_log:
            self.drive_log[agent_id] = []
        self.drive_log[agent_id].append({
            "drive": drive,
            "level": max(0.0, min(level, 1.0)),
            "satisfied": bool(satisfied),
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_latest(self, agent_id):
        return self.drive_log.get(agent_id, [])[-1] if self.drive_log.get(agent_id) else None

    def get_history(self, agent_id):
        return self.drive_log.get(agent_id, [])
