# backend/agent_self_repair.py
# Provides routines for autonomous error correction and self-repair.

class AgentSelfRepair:
    def __init__(self):
        self.repair_log = {}  # {agent_id: [ {timestamp, issue, action} ]}

    def log_repair(self, agent_id, issue: str, action: str):
        from datetime import datetime
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "issue": issue,
            "action": action
        }
        if agent_id not in self.repair_log:
            self.repair_log[agent_id] = []
        self.repair_log[agent_id].append(entry)
        return entry

    def get_repair_history(self, agent_id):
        return self.repair_log.get(agent_id, [])
