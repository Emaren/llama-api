# backend/agent_emotion_engine_api.py
# API endpoints for agent emotion logging and querying.

from fastapi import APIRouter, Query
from backend.agent_emotion_engine import AgentEmotionEngine

router = APIRouter()
emotion_engine = AgentEmotionEngine()

@router.post("/emotion/log/{agent_id}")
def log_emotion(agent_id: str, emotion: str = Query(...), intensity: float = Query(...)):
    emotion_engine.log_emotion(agent_id, emotion, intensity)
    return {"status": "emotion logged"}

@router.get("/emotion/latest/{agent_id}")
def get_latest(agent_id: str):
    return emotion_engine.get_latest(agent_id)

@router.get("/emotion/history/{agent_id}")
def get_history(agent_id: str):
    return emotion_engine.get_history(agent_id)

@router.get("/emotion/aggregate/{agent_id}")
def get_all_emotions(agent_id: str):
    return emotion_engine.get_all_emotions(agent_id)
