# backend/agent_influence_propagator.py
# Simulates propagation of influence across agent social networks.

class AgentInfluencePropagator:
    def __init__(self):
        self.influence = {}  # {agent_id: {peer_id: float}}

    def propagate(self, agent_id, strength: float = 1.0):
        # Placeholder: increase influence to all direct peers by strength
        influenced = {}
        for peer_id in self.influence.get(agent_id, {}):
            self.influence[agent_id][peer_id] += strength
            influenced[peer_id] = self.influence[agent_id][peer_id]
        return influenced

    def set_influence(self, agent_id, peer_id, strength: float):
        if agent_id not in self.influence:
            self.influence[agent_id] = {}
        self.influence[agent_id][peer_id] = strength

    def get_influence(self, agent_id):
        return self.influence.get(agent_id, {})
