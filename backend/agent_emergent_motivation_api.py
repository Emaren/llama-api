# backend/agent_emergent_motivation_api.py
# API for emergent motivation tracking in agent groups.

from fastapi import APIRouter, Query
from backend.agent_emergent_motivation import AgentEmergentMotivation

router = APIRouter()
emergent_motivation = AgentEmergentMotivation()

@router.post("/emergent_motivation/log")
def log_signal(group_id: str = Query(...), signal: str = Query(...), description: str = Query(...)):
    entry = emergent_motivation.log_signal(group_id, signal, description)
    return {"status": "signal logged", "entry": entry}

@router.get("/emergent_motivation/list")
def get_signals(group_id: str = Query(None)):
    return emergent_motivation.get_signals(group_id)
