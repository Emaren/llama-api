# backend/agent_goal_review.py
# Reviews historical goal data for insights and alignment analysis.

from backend.agent_goal_archive import AgentGoalArchive
from backend.insight_generator import InsightGenerator

class AgentGoalReviewer:
    def __init__(self):
        self.archive = AgentGoalArchive()
        self.insight_generator = InsightGenerator()

    def review_agent_goals(self, agent_id):
        archived = self.archive.get_archived_goals(agent_id)
        return self._analyze(archived)

    def _analyze(self, archived_goals):
        successes = [g for g in archived_goals if g["status"] == "completed"]
        failures = [g for g in archived_goals if g["status"] != "completed"]
        insights = self.insight_generator.generate({
            "success_rate": len(successes) / max(len(archived_goals), 1),
            "total_goals": len(archived_goals),
            "failures": failures
        })
        return insights
