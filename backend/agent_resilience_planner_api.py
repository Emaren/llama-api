# backend/agent_resilience_planner_api.py
# API endpoints for managing resilience planning for agents.

from fastapi import APIRouter, Query
from backend.agent_resilience_planner import AgentResiliencePlanner

router = APIRouter()
resilience_planner = AgentResiliencePlanner()

@router.post("/resilience_plan/create/{agent_id}")
def create_plan(agent_id: str, plan_id: str = Query(...), description: str = Query(...)):
    plan = resilience_planner.create_plan(agent_id, plan_id, description)
    return {"status": "plan created", "plan": plan}

@router.post("/resilience_plan/complete/{agent_id}")
def complete_plan(agent_id: str, plan_id: str = Query(...)):
    plan = resilience_planner.complete_plan(agent_id, plan_id)
    if plan:
        return {"status": "plan completed", "plan": plan}
    else:
        return {"status": "plan not found"}

@router.get("/resilience_plan/list/{agent_id}")
def get_plans(agent_id: str):
    return resilience_planner.get_plans(agent_id)
