# backend/agent_behavioral_trends.py
# Detects and records behavioral patterns and shifts over time.

from datetime import datetime

class AgentBehavioralTrends:
    def __init__(self):
        self.behavior_logs = {}  # {agent_id: [ {timestamp, behavior} ]}

    def log_behavior(self, agent_id, behavior: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "behavior": behavior
        }
        if agent_id not in self.behavior_logs:
            self.behavior_logs[agent_id] = []
        self.behavior_logs[agent_id].append(entry)

    def get_behavior_trends(self, agent_id):
        return self.behavior_logs.get(agent_id, [])
