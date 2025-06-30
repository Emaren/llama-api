# backend/agent_long_term_planner_api.py
# API endpoints for managing agent long-term plans.

from fastapi import APIRouter, Query
from backend.agent_long_term_planner import AgentLongTermPlanner

router = APIRouter()
planner = AgentLongTermPlanner()

@router.post("/plan/create/{agent_id}")
def create_plan(agent_id: str, plan_id: str = Query(...), description: str = Query(...), timeline_days: int = 30):
    return planner.create_plan(agent_id, plan_id, description, timeline_days)

@router.post("/plan/milestone/{agent_id}")
def add_milestone(agent_id: str, plan_id: str = Query(...), milestone: str = Query(...)):
    planner.add_milestone(agent_id, plan_id, milestone)
    return {"status": "milestone added"}

@router.get("/plan/get/{agent_id}")
def get_plan(agent_id: str, plan_id: str = Query(...)):
    return planner.get_plan(agent_id, plan_id)

@router.post("/plan/complete/{agent_id}")
def complete_plan(agent_id: str, plan_id: str = Query(...)):
    planner.complete_plan(agent_id, plan_id)
    return {"status": "plan completed"}
