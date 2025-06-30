# backend/agent_mind_map_api.py
# API endpoints for agent mind map manipulation.

from fastapi import APIRouter, Query
from backend.agent_mind_map import AgentMindMap

router = APIRouter()
mind_map = AgentMindMap()

@router.post("/mind_map/add_node/{agent_id}")
def add_node(agent_id: str, node_id: str = Query(...), concept: str = Query(...)):
    mind_map.add_node(agent_id, node_id, concept)
    return {"status": "node added"}

@router.post("/mind_map/add_link/{agent_id}")
def add_link(agent_id: str, from_node: str = Query(...), to_node: str = Query(...)):
    mind_map.add_link(agent_id, from_node, to_node)
    return {"status": "link added"}

@router.get("/mind_map/get/{agent_id}")
def get_map(agent_id: str):
    return mind_map.get_map(agent_id)
