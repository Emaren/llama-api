# backend/agent_mind_map.py
# Maintains agent mind maps (concept graphs or idea networks).

class AgentMindMap:
    def __init__(self):
        self.mind_maps = {}  # {agent_id: {node_id: {"concept": str, "links": [node_id]}}}

    def add_node(self, agent_id, node_id: str, concept: str):
        if agent_id not in self.mind_maps:
            self.mind_maps[agent_id] = {}
        self.mind_maps[agent_id][node_id] = {"concept": concept, "links": []}

    def add_link(self, agent_id, from_node: str, to_node: str):
        if agent_id in self.mind_maps and from_node in self.mind_maps[agent_id]:
            self.mind_maps[agent_id][from_node]["links"].append(to_node)

    def get_map(self, agent_id):
        return self.mind_maps.get(agent_id, {})
