# backend/agent_meta_goal_evaluator.py
# Evaluates agent progress and achievement of meta-goals.

class AgentMetaGoalEvaluator:
    def __init__(self):
        self.meta_goals = {}  # {agent_id: [ {goal, achieved, timestamp} ]}

    def log_goal(self, agent_id, goal: str, achieved: bool):
        from datetime import datetime
        entry = {
            "goal": goal,
            "achieved": bool(achieved),
            "timestamp": datetime.utcnow().isoformat()
        }
        if agent_id not in self.meta_goals:
            self.meta_goals[agent_id] = []
        self.meta_goals[agent_id].append(entry)
        return entry

    def get_goals(self, agent_id):
        return self.meta_goals.get(agent_id, [])
