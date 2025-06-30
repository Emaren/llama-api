# backend/agent_long_term_goal_monitor.py
# Tracks long-term goal progress for agents over extended timelines.

from datetime import datetime

class AgentLongTermGoalMonitor:
    def __init__(self):
        self.goals = {}  # {agent_id: { "goal": str, "created": ts, "milestones": [], "completed": bool }}

    def set_goal(self, agent_id, goal: str):
        self.goals[agent_id] = {
            "goal": goal,
            "created": datetime.utcnow().isoformat(),
            "milestones": [],
            "completed": False
        }

    def add_milestone(self, agent_id, milestone: str):
        if agent_id in self.goals:
            self.goals[agent_id]["milestones"].append({
                "milestone": milestone,
                "timestamp": datetime.utcnow().isoformat()
            })

    def complete_goal(self, agent_id):
        if agent_id in self.goals:
            self.goals[agent_id]["completed"] = True

    def get_goal_status(self, agent_id):
        return self.goals.get(agent_id, {})
