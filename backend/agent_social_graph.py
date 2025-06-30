# backend/agent_social_graph.py
# Models agent relationships and social influence graph.

class AgentSocialGraph:
    def __init__(self):
        self.graph = {}  # {agent_id: {peer_id: {"relationship": str, "strength": float}}}

    def add_relationship(self, agent_id, peer_id, relationship: str, strength: float = 1.0):
        if agent_id not in self.graph:
            self.graph[agent_id] = {}
        self.graph[agent_id][peer_id] = {
            "relationship": relationship,
            "strength": max(0.0, min(strength, 1.0))
        }

    def get_relationships(self, agent_id):
        return self.graph.get(agent_id, {})

    def get_social_circle(self, agent_id, min_strength: float = 0.5):
        peers = self.graph.get(agent_id, {})
        return {peer: data for peer, data in peers.items() if data["strength"] >= min_strength}
