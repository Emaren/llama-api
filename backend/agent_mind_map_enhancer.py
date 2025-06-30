# backend/agent_mind_map_enhancer.py
# Adds advanced heuristics and semantic relations to agent mind maps.

from backend.agent_mind_map import AgentMindMap

class AgentMindMapEnhancer:
    def __init__(self):
        self.mind_map = AgentMindMap()

    def enhance_node(self, agent_id, node_id, heuristics: dict, semantic_tags: list):
        mind_map = self.mind_map.get_map(agent_id)
        if node_id in mind_map:
            node = mind_map[node_id]
            node['heuristics'] = heuristics
            node['semantic_tags'] = semantic_tags
            return node
        return None

    def get_enhanced_map(self, agent_id):
        return self.mind_map.get_map(agent_id)
