# backend/agent_goal_planner.py
# Assigns, adapts, and schedules goals for individual agents.

from backend.project_planner import ProjectPlanner
from backend.goal_state_evaluator import GoalStateEvaluator
from backend.context_engine import ContextEngine

class AgentGoalPlanner:
    def __init__(self):
        self.project_planner = ProjectPlanner()
        self.goal_evaluator = GoalStateEvaluator()
        self.context_engine = ContextEngine()

    def plan_goals_for_agent(self, agent_id, context):
        context_state = self.context_engine.analyze(context)
        goals = self.project_planner.generate_goals(context_state)
        prioritized = self.goal_evaluator.rank_goals(goals)
        return self._assign_goals(agent_id, prioritized)

    def _assign_goals(self, agent_id, goals):
        return {
            "agent_id": agent_id,
            "goals": goals[:3],  # Top 3 actionable goals
            "timestamp": self._current_timestamp()
        }

    def _current_timestamp(self):
        from datetime import datetime
        return datetime.utcnow().isoformat()
