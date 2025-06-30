# backend/agent_alignment_analyzer.py
# Evaluates patterns of misalignment and possible causes.

from backend.agent_alignment_tracker import AgentAlignmentTracker

class AgentAlignmentAnalyzer:
    def __init__(self):
        self.tracker = AgentAlignmentTracker()

    def analyze(self, agent_id):
        history = self.tracker.get_alignment_history(agent_id)
        if not history:
            return {"agent_id": agent_id, "status": "no data"}

        recent_scores = [entry["score"] for entry in history[-10:]]
        avg = sum(recent_scores) / len(recent_scores)
        min_score = min(recent_scores)
        max_score = max(recent_scores)

        status = "stable"
        if avg < 0.6:
            status = "concerning"
        elif max_score - min_score > 0.5:
            status = "volatile"

        return {
            "agent_id": agent_id,
            "average_score": round(avg, 2),
            "min_score": min_score,
            "max_score": max_score,
            "status": status
        }
