# backend/agent_symbolic_reasoner.py
# Supports symbolic logic and deterministic reasoning for agents.

class AgentSymbolicReasoner:
    def __init__(self):
        self.knowledge_base = {}  # {agent_id: set of facts}

    def add_fact(self, agent_id, fact: str):
        if agent_id not in self.knowledge_base:
            self.knowledge_base[agent_id] = set()
        self.knowledge_base[agent_id].add(fact)

    def has_fact(self, agent_id, fact: str):
        return fact in self.knowledge_base.get(agent_id, set())

    def infer(self, agent_id, premise_a: str, premise_b: str, conclusion: str):
        kb = self.knowledge_base.get(agent_id, set())
        if premise_a in kb and premise_b in kb:
            kb.add(conclusion)
            return {"inferred": True, "conclusion": conclusion}
        return {"inferred": False, "reason": "Premises not satisfied"}
