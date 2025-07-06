import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "shared")))
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
"""
memory_loader.py – Loads memory traces from persistent storage and prepares
them for use in active memory systems.
"""

import json
from shared.memory_types import MemoryTrace
from backend.db_models import MemoryEntry
from backend.db_session import async_session
from sqlalchemy import select

class MemoryLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_memory(self) -> list[MemoryTrace]:
        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)
            traces = [MemoryTrace(**item) for item in data]
            print(f"[MemoryLoader] Loaded {len(traces)} memory traces from {self.filepath}")
            return traces
        except Exception as e:
            print(f"[MemoryLoader] Error loading memory: {e}")
            return []

async def load_memories(user_id: str, agent_name: str, limit: int = 5):
    async with async_session() as session:
        result = await session.execute(
            select(MemoryEntry)
            .where(MemoryEntry.user_id == user_id)
            .where(MemoryEntry.agent_name == agent_name)
            .order_by(MemoryEntry.score.desc())
            .limit(limit)
        )
        memories = result.scalars().all()
        return [m.content for m in memories]
