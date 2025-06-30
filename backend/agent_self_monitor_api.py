# backend/agent_self_monitor_api.py
# API endpoints for self-monitoring agent status and health.

from fastapi import APIRouter, Query
from backend.agent_self_monitor import AgentSelfMonitor

router = APIRouter()
monitor = AgentSelfMonitor()

@router.post("/self_monitor/log/{agent_id}")
def log_status(agent_id: str, status: str = Query(...)):
    monitor.log_status(agent_id, status)
    return {"status": "logged"}

@router.get("/self_monitor/logs/{agent_id}")
def get_status_logs(agent_id: str):
    return monitor.get_status_logs(agent_id)
