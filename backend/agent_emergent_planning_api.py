# backend/agent_emergent_planning_api.py
# API for emergent planning and group strategies in agent collectives.

from fastapi import APIRouter, Query
from backend.agent_emergent_planning import AgentEmergentPlanning

router = APIRouter()
emergent_planning = AgentEmergentPlanning()

@router.post("/emergent_plan/log")
def log_plan(plan_id: str = Query(...), group_id: str = Query(...), strategy: str = Query(...)):
    entry = emergent_planning.log_plan(plan_id, group_id, strategy)
    return {"status": "plan logged", "entry": entry}

@router.get("/emergent_plan/list")
def get_plans(group_id: str = Query(None)):
    return emergent_planning.get_plans(group_id)
