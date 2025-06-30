# backend/agent_goal_feedback.py
# Collects feedback on executed goals and informs future planning.

from backend.feedback_tracker import FeedbackTracker
from backend.goal_state_evaluator import GoalStateEvaluator

class AgentGoalFeedback:
    def __init__(self):
        self.feedback_tracker = FeedbackTracker()
        self.evaluator = GoalStateEvaluator()

    def record_feedback(self, agent_id, goal, outcome, notes=None):
        feedback = {
            "agent_id": agent_id,
            "goal": goal,
            "outcome": outcome,
            "notes": notes
        }
        self.feedback_tracker.store(feedback)

    def evaluate_execution(self, agent_id, goal_result):
        score = self.evaluator.evaluate_result(goal_result)
        return {
            "agent_id": agent_id,
            "score": score,
            "assessment": self._interpret_score(score)
        }

    def _interpret_score(self, score):
        if score >= 0.8:
            return "successful"
        elif score >= 0.5:
            return "partial success"
        else:
            return "unsuccessful"
