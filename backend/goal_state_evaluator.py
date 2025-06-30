\"\"\"
goal_state_evaluator.py – Evaluates project or agent goals for progress,
completion, or stalling, and suggests interventions if needed.
\"\"\"

from data.project_goals import GOALS_DB

class GoalStateEvaluator:
    def __init__(self):
        self.goals = GOALS_DB

    def evaluate(self, agent_id: str):
        agent_goals = self.goals.get(agent_id, [])
        evaluations = []

        for goal in agent_goals:
            progress = goal.get("progress", 0)
            status = "completed" if progress >= 100 else                      "on_track" if progress >= 50 else                      "at_risk" if progress > 0 else "not_started"
            evaluations.append({
                "goal": goal["name"],
                "status": status,
                "progress": progress
            })

        return evaluations

    def flag_interventions(self, evaluations):
        return [g for g in evaluations if g["status"] in ("at_risk", "not_started")]
