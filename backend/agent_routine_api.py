# backend/agent_routine_api.py
# API for managing agent routines and schedules.

from fastapi import APIRouter, Query
from backend.agent_routine_planner import AgentRoutinePlanner

router = APIRouter()
planner = AgentRoutinePlanner()

@router.post("/routine/plan/{agent_id}")
def plan_routine(agent_id: str, tasks: list[str] = Query(...)):
    return planner.plan_daily_routine(agent_id, tasks)

@router.get("/routine/{agent_id}")
def get_routine(agent_id: str):
    return planner.get_routine(agent_id)

@router.delete("/routine/{agent_id}")
def clear_routine(agent_id: str):
    planner.clear_routine(agent_id)
    return {"status": "cleared"}
