# backend/agent_drive_controller_api.py
# API for agent drive and instinct tracking.

from fastapi import APIRouter, Query
from backend.agent_drive_controller import AgentDriveController

router = APIRouter()
drive_controller = AgentDriveController()

@router.post("/drive/log/{agent_id}")
def log_drive(agent_id: str, drive: str = Query(...), level: float = Query(...), satisfied: bool = Query(...)):
    drive_controller.log_drive(agent_id, drive, level, satisfied)
    return {"status": "drive logged"}

@router.get("/drive/latest/{agent_id}")
def get_latest(agent_id: str):
    return drive_controller.get_latest(agent_id)

@router.get("/drive/history/{agent_id}")
def get_history(agent_id: str):
    return drive_controller.get_history(agent_id)
