# backend/agent_hierarchical_reflection_api.py
# API for hierarchical reflection and meta-reflection in agents.

from fastapi import APIRouter, Query
from backend.agent_hierarchical_reflection import AgentHierarchicalReflection

router = APIRouter()
hier_reflector = AgentHierarchicalReflection()

@router.post("/hierarchical_reflection/log/{agent_id}")
def log_reflection(agent_id: str, level: int = Query(...), content: str = Query(...)):
    return hier_reflector.log_reflection(agent_id, level, content)

@router.get("/hierarchical_reflection/get/{agent_id}")
def get_reflections(agent_id: str, level: int = Query(None)):
    return hier_reflector.get_reflections(agent_id, level)
