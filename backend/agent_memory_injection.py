# backend/agent_memory_injection.py
# Adds external knowledge or feedback into agent memory context.

from backend.memory_engine import MemoryEngine

class AgentMemoryInjection:
    def __init__(self):
        self.memory_engine = MemoryEngine()

    def inject(self, agent_id, content: str, source: str = "external"):
        entry = {
            "content": content,
            "source": source
        }
        self.memory_engine.store(agent_id, entry)
        return entry
