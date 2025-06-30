# backend/agent_multi_modal_processor_api.py
# API endpoints for multi-modal input/output management.

from fastapi import APIRouter, Query
from datetime import datetime
from backend.agent_multi_modal_processor import AgentMultiModalProcessor

router = APIRouter()
mm_processor = AgentMultiModalProcessor()

@router.post("/multi_modal/log/{agent_id}")
def log_input(agent_id: str, modality: str = Query(...), content: str = Query(...)):
    timestamp = datetime.utcnow().isoformat()
    mm_processor.log_input(agent_id, modality, content, timestamp)
    return {"status": "input logged"}

@router.get("/multi_modal/history/{agent_id}")
def get_history(agent_id: str):
    return mm_processor.get_history(agent_id)

@router.get("/multi_modal/latest/{agent_id}")
def get_latest_by_modality(agent_id: str, modality: str = Query(...)):
    return mm_processor.get_latest_by_modality(agent_id, modality)
