# backend/agent_task_efficiency_api.py
# API endpoints to log task performance and retrieve efficiency.

from fastapi import APIRouter, Query
from backend.agent_task_efficiency_monitor import AgentTaskEfficiencyMonitor

router = APIRouter()
efficiency_monitor = AgentTaskEfficiencyMonitor()

@router.post("/task_efficiency/log/{agent_id}")
def log_task(agent_id: str, task_id: str = Query(...), duration_sec: float = Query(...), resources_used: float = Query(...)):
    efficiency_monitor.log_task(agent_id, task_id, duration_sec, resources_used)
    return {"status": "task logged"}

@router.get("/task_efficiency/calc/{agent_id}")
def calculate_efficiency(agent_id: str):
    return efficiency_monitor.calculate_efficiency(agent_id)
