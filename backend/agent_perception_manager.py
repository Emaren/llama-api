# backend/agent_perception_manager.py
# Synthesizes sensory, memory, and system cues into agent perception state.

from backend.context_engine import ContextEngine
from backend.memory_engine import MemoryEngine
from backend.system_monitor import SystemMonitor

class AgentPerceptionManager:
    def __init__(self):
        self.context_engine = ContextEngine()
        self.memory_engine = MemoryEngine()
        self.system_monitor = SystemMonitor()

    def generate_perception(self, agent_id, external_context):
        context_state = self.context_engine.analyze(external_context)
        memory_state = self.memory_engine.query_recent(agent_id)
        system_state = self.system_monitor.get_status()

        return {
            "agent_id": agent_id,
            "context": context_state,
            "memory": memory_state,
            "system": system_state,
            "timestamp": self._now()
        }

    def _now(self):
        from datetime import datetime
        return datetime.utcnow().isoformat()
