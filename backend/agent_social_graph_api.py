# backend/agent_social_graph_api.py
# API for managing agent social relationships and influence graph.

from fastapi import APIRouter, Query
from backend.agent_social_graph import AgentSocialGraph

router = APIRouter()
social_graph = AgentSocialGraph()

@router.post("/social_graph/relationship/{agent_id}")
def add_relationship(agent_id: str, peer_id: str = Query(...), relationship: str = Query(...), strength: float = Query(1.0)):
    social_graph.add_relationship(agent_id, peer_id, relationship, strength)
    return {"status": "relationship added"}

@router.get("/social_graph/relationships/{agent_id}")
def get_relationships(agent_id: str):
    return social_graph.get_relationships(agent_id)

@router.get("/social_graph/circle/{agent_id}")
def get_social_circle(agent_id: str, min_strength: float = Query(0.5)):
    return social_graph.get_social_circle(agent_id, min_strength)
