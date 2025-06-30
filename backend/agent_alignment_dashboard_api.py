# backend/agent_alignment_dashboard_api.py
# API for serving alignment summaries to the frontend dashboard.

from fastapi import APIRouter, Body
from backend.agent_alignment_dashboard import AgentAlignmentDashboard

router = APIRouter()
dashboard = AgentAlignmentDashboard()

@router.get("/alignment_dashboard/{agent_id}")
def get_alignment_dashboard(agent_id: str):
    return dashboard.get_dashboard_summary(agent_id)

@router.post("/alignment_dashboard_bulk")
def get_bulk_alignment_dashboards(agent_ids: list[str] = Body(...)):
    return dashboard.get_bulk_summary(agent_ids)
