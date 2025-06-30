# backend/agent_state_api.py
# API route to serve agent state summaries to the frontend.

from fastapi import APIRouter
from backend.agent_state_dashboard import AgentStateDashboard

router = APIRouter()
dashboard = AgentStateDashboard()

@router.get("/agent_state/{agent_id}")
def get_agent_state(agent_id: str):
    return dashboard.get_agent_state_summary(agent_id)

@router.post("/agent_states")
def get_bulk_agent_states(agent_ids: list[str]):
    return dashboard.get_bulk_state_summary(agent_ids)
