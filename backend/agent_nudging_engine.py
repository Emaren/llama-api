# backend/agent_nudging_engine.py
# Issues lightweight nudges to correct agent course or boost momentum.

from datetime import datetime

class AgentNudgingEngine:
    def __init__(self):
        self.nudge_log = {}  # {agent_id: [ {message, timestamp} ]}

    def send_nudge(self, agent_id, message: str):
        if agent_id not in self.nudge_log:
            self.nudge_log[agent_id] = []
        entry = {
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.nudge_log[agent_id].append(entry)
        return entry

    def get_nudges(self, agent_id):
        return self.nudge_log.get(agent_id, [])
