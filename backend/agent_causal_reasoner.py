# backend/agent_causal_reasoner.py
# Supports causal inference and reasoning for agents.

class AgentCausalReasoner:
    def __init__(self):
        self.causal_graphs = {}  # {agent_id: {cause: set(effect)}}

    def add_causal_relation(self, agent_id, cause: str, effect: str):
        if agent_id not in self.causal_graphs:
            self.causal_graphs[agent_id] = {}
        if cause not in self.causal_graphs[agent_id]:
            self.causal_graphs[agent_id][cause] = set()
        self.causal_graphs[agent_id][cause].add(effect)

    def get_effects(self, agent_id, cause: str):
        return list(self.causal_graphs.get(agent_id, {}).get(cause, set()))

    def get_causes(self, agent_id, effect: str):
        causes = []
        for cause, effects in self.causal_graphs.get(agent_id, {}).items():
            if effect in effects:
                causes.append(cause)
        return causes
