# backend/agent_emotion_api.py
# API endpoints for managing agent emotional states.

from fastapi import APIRouter, Query
from backend.agent_emotion_engine import AgentEmotionEngine

router = APIRouter()
emotion_engine = AgentEmotionEngine()

@router.post("/emotion/set/{agent_id}")
def set_emotion(agent_id: str, emotion: str = Query(...), intensity: float = Query(...)):
    emotion_engine.set_emotion(agent_id, emotion, intensity)
    return {"status": "emotion set", "emotion": emotion, "intensity": intensity}

@router.get("/emotion/get/{agent_id}")
def get_emotion(agent_id: str, emotion: str = Query(...)):
    intensity = emotion_engine.get_emotion(agent_id, emotion)
    return {"emotion": emotion, "intensity": intensity}

@router.get("/emotion/all/{agent_id}")
def get_all_emotions(agent_id: str):
    return emotion_engine.get_all_emotions(agent_id)
