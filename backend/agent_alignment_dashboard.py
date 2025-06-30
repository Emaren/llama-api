# backend/agent_alignment_dashboard.py
# Prepares alignment summaries for visualization in the frontend.

from backend.agent_alignment_summary import AgentAlignmentSummary

class AgentAlignmentDashboard:
    def __init__(self):
        self.summarizer = AgentAlignmentSummary()

    def get_dashboard_summary(self, agent_id):
        summary = self.summarizer.summarize(agent_id)
        return {
            "agent_id": agent_id,
            "violation_count": summary["violations"],
            "top_issues": summary["frequent_issues"],
            "bias_keys": list(summary["bias_trend"].keys())[:3],
            "awareness_consistent": summary["awareness_stability"],
            "recent_perception_keys": list(summary["last_perception"].keys())[:5]
        }

    def get_bulk_summary(self, agent_ids):
        return [self.get_dashboard_summary(agent_id) for agent_id in agent_ids]
