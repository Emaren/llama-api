# backend/agent_emotion_engine.py
# Models and manages emotions for agents.

from datetime import datetime

class AgentEmotionEngine:
    def __init__(self):
        self.emotion_log = {}  # {agent_id: [ {emotion, intensity, timestamp} ]}

    def log_emotion(self, agent_id, emotion: str, intensity: float):
        if agent_id not in self.emotion_log:
            self.emotion_log[agent_id] = []
        self.emotion_log[agent_id].append({
            "emotion": emotion,
            "intensity": max(0.0, min(intensity, 1.0)),
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_latest(self, agent_id):
        return self.emotion_log.get(agent_id, [])[-1] if self.emotion_log.get(agent_id) else None

    def get_history(self, agent_id):
        return self.emotion_log.get(agent_id, [])

    def get_all_emotions(self, agent_id):
        # Returns dict {emotion: avg_intensity}
        history = self.emotion_log.get(agent_id, [])
        if not history:
            return {}
        emotion_map = {}
        counts = {}
        for entry in history:
            emo = entry["emotion"]
            val = entry["intensity"]
            if emo not in emotion_map:
                emotion_map[emo] = 0.0
                counts[emo] = 0
            emotion_map[emo] += val
            counts[emo] += 1
        return {emo: emotion_map[emo] / counts[emo] for emo in emotion_map}
