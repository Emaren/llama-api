# backend/agent_state_synthesizer.py
# Synthesizes multiple agent subsystems into a coherent state snapshot.

from backend.agent_awareness_model import AgentAwarenessModel
from backend.agent_focus_tracker import AgentFocusTracker
from backend.agent_perception_tracker import AgentPerceptionTracker
from backend.memory_engine import MemoryEngine

class AgentStateSynthesizer:
    def __init__(self):
        self.awareness_model = AgentAwarenessModel()
        self.focus_tracker = AgentFocusTracker()
        self.perception_tracker = AgentPerceptionTracker()
        self.memory_engine = MemoryEngine()

    def synthesize_state(self, agent_id):
        awareness = self.awareness_model.get_awareness(agent_id)
        focus = self.focus_tracker.get_focus_history(agent_id, limit=1)
        perception = self.perception_tracker.get_recent_perceptions(agent_id)[-1]["state"]             if self.perception_tracker.get_recent_perceptions(agent_id) else {}
        memory = self.memory_engine.query_recent(agent_id)

        return {
            "agent_id": agent_id,
            "awareness": awareness,
            "focus": focus[0] if focus else {},
            "perception": perception,
            "memory": memory
        }
