# backend/agent_resilience_planner.py
# Designs plans to increase agent resilience and recovery capacity.

class AgentResiliencePlanner:
    def __init__(self):
        self.resilience_plans = {}  # {agent_id: [ {plan_id, description, status} ]}

    def create_plan(self, agent_id, plan_id, description):
        plan = {
            "plan_id": plan_id,
            "description": description,
            "status": "active"
        }
        if agent_id not in self.resilience_plans:
            self.resilience_plans[agent_id] = []
        self.resilience_plans[agent_id].append(plan)
        return plan

    def complete_plan(self, agent_id, plan_id):
        if agent_id in self.resilience_plans:
            for plan in self.resilience_plans[agent_id]:
                if plan["plan_id"] == plan_id:
                    plan["status"] = "completed"
                    return plan
        return None

    def get_plans(self, agent_id):
        return self.resilience_plans.get(agent_id, [])
