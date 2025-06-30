# backend/agent_mind_map_enhancer_api.py
# API endpoints for mind map node enhancement.

from fastapi import APIRouter, Query
from backend.agent_mind_map_enhancer import AgentMindMapEnhancer

router = APIRouter()
enhancer = AgentMindMapEnhancer()

@router.post("/mind_map/enhance_node/{agent_id}")
def enhance_node(agent_id: str, node_id: str = Query(...), heuristics: str = Query(...), semantic_tags: str = Query(...)):
    import json
    heuristics_dict = json.loads(heuristics)
    semantic_tags_list = json.loads(semantic_tags)
    node = enhancer.enhance_node(agent_id, node_id, heuristics_dict, semantic_tags_list)
    return {"status": "node enhanced", "node": node}

@router.get("/mind_map/enhanced/{agent_id}")
def get_enhanced_map(agent_id: str):
    return enhancer.get_enhanced_map(agent_id)
