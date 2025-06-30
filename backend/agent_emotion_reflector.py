# backend/agent_emotion_reflector.py
# Enables agents to introspect on their emotional dynamics.

from backend.agent_emotion_engine import AgentEmotionEngine

class AgentEmotionReflector:
    def __init__(self):
        self.emotion_engine = AgentEmotionEngine()

    def reflect(self, agent_id):
        emotions = self.emotion_engine.get_all_emotions(agent_id)
        insights = []

        if not emotions:
            insights.append("No emotions recorded.")
            return {"agent_id": agent_id, "insights": insights}

        dominant_emotion = max(emotions, key=emotions.get)
        intensity = emotions[dominant_emotion]

        insights.append(f"Dominant emotion: {dominant_emotion} (intensity: {intensity:.2f})")

        if intensity > 0.7:
            insights.append(f"High intensity of {dominant_emotion} may influence decisions.")

        return {"agent_id": agent_id, "insights": insights}
