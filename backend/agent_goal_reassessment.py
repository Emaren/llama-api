# backend/agent_goal_reassessment.py
# Assesses if goals need revision based on recent feedback or drift.

class AgentGoalReassessment:
    def __init__(self):
        self.reassessment_log = {}  # {agent_id: [ {timestamp, reason} ]}

    def request_reassessment(self, agent_id, reason: str):
        from datetime import datetime
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "reason": reason
        }
        if agent_id not in self.reassessment_log:
            self.reassessment_log[agent_id] = []
        self.reassessment_log[agent_id].append(entry)
        return entry

    def get_reassessments(self, agent_id):
        return self.reassessment_log.get(agent_id, [])
