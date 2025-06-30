# backend/agent_conflict_resolver.py
# Implements logic to resolve or escalate agent conflicts.

class AgentConflictResolver:
    def __init__(self):
        self.resolutions = {}  # {agent_id: [ {conflict_type, resolution, timestamp} ]}

    def resolve_conflict(self, agent_id, conflict_type: str, resolution: str):
        from datetime import datetime
        entry = {
            "conflict_type": conflict_type,
            "resolution": resolution,
            "timestamp": datetime.utcnow().isoformat()
        }
        if agent_id not in self.resolutions:
            self.resolutions[agent_id] = []
        self.resolutions[agent_id].append(entry)
        return entry

    def get_resolutions(self, agent_id):
        return self.resolutions.get(agent_id, [])
