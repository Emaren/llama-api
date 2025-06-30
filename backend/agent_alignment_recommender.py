# backend/agent_alignment_recommender.py
# Recommends interventions based on alignment summary insights.

from backend.agent_alignment_summary import AgentAlignmentSummary

class AgentAlignmentRecommender:
    def __init__(self):
        self.summary = AgentAlignmentSummary()

    def recommend(self, agent_id):
        data = self.summary.summarize(agent_id)
        suggestions = []

        if data["violations"] >= 5:
            suggestions.append("Temporarily deactivate agent or limit permissions.")

        if data["frequent_issues"]:
            suggestions.append("Review flagged issues and escalate for inspection.")

        if len(data["bias_trend"]) > 0:
            suggestions.append("Trigger memory diffusion or self-reflection.")

        if not data["awareness_stability"]:
            suggestions.append("Reset role/context to stabilize awareness.")

        if data["perception_entries"] == 0:
            suggestions.append("Perception data missing — validate agent sensors.")

        return {
            "agent_id": agent_id,
            "suggestions": suggestions or ["No immediate intervention needed."]
        }
