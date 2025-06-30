# backend/agent_alignment_tracker.py
# Tracks behavior alignment with goals, roles, and values.

from datetime import datetime

class AgentAlignmentTracker:
    def __init__(self):
        self.alignment_logs = {}  # {agent_id: [ {score, reason, timestamp} ]}

    def log_alignment(self, agent_id, score: float, reason: str = ""):
        if agent_id not in self.alignment_logs:
            self.alignment_logs[agent_id] = []
        self.alignment_logs[agent_id].append({
            "score": round(score, 2),
            "reason": reason,
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_alignment_history(self, agent_id):
        return self.alignment_logs.get(agent_id, [])

    def average_alignment(self, agent_id):
        entries = self.alignment_logs.get(agent_id, [])
        if not entries:
            return 1.0
        return round(sum(e["score"] for e in entries) / len(entries), 2)
