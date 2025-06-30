# backend/agent_conflict_detector.py
# Identifies conflicts in goals, plans, or knowledge for resolution.

class AgentConflictDetector:
    def __init__(self):
        self.conflicts = {}  # {agent_id: [ {conflict_type, details} ]}

    def add_conflict(self, agent_id, conflict_type: str, details: str):
        if agent_id not in self.conflicts:
            self.conflicts[agent_id] = []
        self.conflicts[agent_id].append({
            "conflict_type": conflict_type,
            "details": details
        })

    def get_conflicts(self, agent_id):
        return self.conflicts.get(agent_id, [])
