# backend/agent_resilience_dashboard_api.py
# API to serve resilience dashboard data to the frontend.

from fastapi import APIRouter
from backend.agent_resilience_dashboard import AgentResilienceDashboard

router = APIRouter()
dashboard = AgentResilienceDashboard()

@router.get("/resilience_dashboard/{agent_id}")
def get_resilience_dashboard(agent_id: str):
    return dashboard.get_dashboard_data(agent_id)
