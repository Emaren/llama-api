# backend/agent_knowledge_drift.py
# Monitors and analyzes drift in agent knowledge and internal consistency.

from datetime import datetime

class AgentKnowledgeDrift:
    def __init__(self):
        self.knowledge_snapshots = {}  # {agent_id: [ {timestamp, snapshot_hash} ]}

    def record_snapshot(self, agent_id, snapshot_hash):
        from datetime import datetime
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "snapshot_hash": snapshot_hash
        }
        if agent_id not in self.knowledge_snapshots:
            self.knowledge_snapshots[agent_id] = []
        self.knowledge_snapshots[agent_id].append(entry)

    def calculate_drift(self, agent_id):
        snapshots = self.knowledge_snapshots.get(agent_id, [])
        if len(snapshots) < 2:
            return 0.0  # Not enough data to calculate drift

        # Placeholder: drift calculated as ratio of unique snapshots over total
        hashes = [entry["snapshot_hash"] for entry in snapshots]
        unique_hashes = len(set(hashes))
        drift_ratio = 1 - (unique_hashes / len(hashes))
        return round(drift_ratio, 3)
