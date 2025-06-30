# backend/agent_emergent_behavior_analyzer.py
# Identifies and logs emergent behaviors in agent collectives.

from datetime import datetime

class AgentEmergentBehaviorAnalyzer:
    def __init__(self):
        self.behavior_log = []  # [ {timestamp, behavior, group_id, description} ]

    def log_behavior(self, behavior: str, group_id: str, description: str):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "behavior": behavior,
            "group_id": group_id,
            "description": description
        }
        self.behavior_log.append(entry)
        return entry

    def get_behaviors(self, group_id: str = None):
        if group_id:
            return [b for b in self.behavior_log if b["group_id"] == group_id]
        return self.behavior_log
