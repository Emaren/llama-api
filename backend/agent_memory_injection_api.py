# backend/agent_memory_injection_api.py
# API for external memory injection into agents.

from fastapi import APIRouter, Query
from backend.agent_memory_injection import AgentMemoryInjection

router = APIRouter()
injector = AgentMemoryInjection()

@router.post("/memory_inject/{agent_id}")
def inject_memory(agent_id: str, content: str = Query(...), source: str = "external"):
    return injector.inject(agent_id, content, source)
