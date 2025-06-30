# backend/agent_emotion_reflector_api.py
# API endpoint for agent emotional self-reflection insights.

from fastapi import APIRouter
from backend.agent_emotion_reflector import AgentEmotionReflector

router = APIRouter()
reflector = AgentEmotionReflector()

@router.get("/emotion_reflect/{agent_id}")
def reflect_emotion(agent_id: str):
    return reflector.reflect(agent_id)
