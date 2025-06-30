# backend/agent_long_term_planner.py
# Creates and manages long-term strategic plans for agents.

from datetime import datetime, timedelta

class AgentLongTermPlanner:
    def __init__(self):
        self.plans = {}  # {agent_id: {plan_id: {details}}}

    def create_plan(self, agent_id, plan_id, description, timeline_days=30):
        end_date = datetime.utcnow() + timedelta(days=timeline_days)
        plan = {
            "description": description,
            "created": datetime.utcnow().isoformat(),
            "end_date": end_date.isoformat(),
            "milestones": [],
            "status": "active"
        }
        if agent_id not in self.plans:
            self.plans[agent_id] = {}
        self.plans[agent_id][plan_id] = plan
        return plan

    def add_milestone(self, agent_id, plan_id, milestone):
        if agent_id in self.plans and plan_id in self.plans[agent_id]:
            self.plans[agent_id][plan_id]["milestones"].append({
                "milestone": milestone,
                "timestamp": datetime.utcnow().isoformat()
            })

    def get_plan(self, agent_id, plan_id):
        return self.plans.get(agent_id, {}).get(plan_id, {})

    def complete_plan(self, agent_id, plan_id):
        if agent_id in self.plans and plan_id in self.plans[agent_id]:
            self.plans[agent_id][plan_id]["status"] = "completed"
