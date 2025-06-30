# backend/agent_emergent_planning.py
# Supports emergent strategy detection and planning across agent collectives.

class AgentEmergentPlanning:
    def __init__(self):
        self.plans = []  # [ {plan_id, group_id, strategy, timestamp} ]

    def log_plan(self, plan_id: str, group_id: str, strategy: str):
        from datetime import datetime
        entry = {
            "plan_id": plan_id,
            "group_id": group_id,
            "strategy": strategy,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.plans.append(entry)
        return entry

    def get_plans(self, group_id: str = None):
        if group_id:
            return [p for p in self.plans if p["group_id"] == group_id]
        return self.plans
