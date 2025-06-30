# backend/agent_philosophy_module.py
# Defines internal philosophy and principles to shape agent decisions.

class AgentPhilosophyModule:
    def __init__(self):
        self.philosophies = {}  # {agent_id: [principles]}

    def set_philosophy(self, agent_id: str, principles: list):
        self.philosophies[agent_id] = principles

    def get_philosophy(self, agent_id: str):
        return self.philosophies.get(agent_id, [])

    def apply_ethics_filter(self, agent_id: str, action: str):
        philosophy = self.philosophies.get(agent_id, [])
        violations = [p for p in philosophy if p.lower() in action.lower()]
        return {
            "approved": len(violations) == 0,
            "violations": violations
        }
