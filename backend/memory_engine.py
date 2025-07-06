"""
memory_engine.py – Redis-backed memory engine for persistent scoped memory
"""

import redis
import json
from shared.memory_types import MemoryTrace
from backend.memory_scoper import MemoryScoper
from backend.memory_pruner import MemoryPruner
from backend.db_models import MemoryEntry
from backend.db_session import async_session


class MemoryEngine:
    def __init__(self):
        self.r = redis.Redis(host="localhost", port=6379, decode_responses=True)
        self.pruner = MemoryPruner()
        self.scoper = MemoryScoper()

    def store_trace(self, session_id: str, trace: MemoryTrace):
        trace_dict = trace.dict()
        self.r.rpush(session_id, json.dumps(trace_dict))
        print(f"[DEBUG] Current Redis memory for {session_id}: {self.r.lrange(session_id, 0, -1)}")
        print(f"[MemoryEngine] Stored trace in Redis for session {session_id}: {trace.content}")

    def retrieve_scope(self, session_id: str, query: str):
        raw_traces = self.r.lrange(session_id, 0, -1)
        traces = [MemoryTrace(**json.loads(t)) for t in raw_traces]
        scoped = self.scoper.scope(traces, query)
        print(f"[MemoryEngine] Retrieved {len(scoped)} scoped traces from Redis for session {session_id}")
        return scoped

    def prune_memory(self, session_id: str):
        raw_traces = self.r.lrange(session_id, 0, -1)
        traces = [MemoryTrace(**json.loads(t)) for t in raw_traces]
        pruned = self.pruner.prune(traces)
        self.r.delete(session_id)
        for trace in pruned:
            self.r.rpush(session_id, json.dumps(trace.dict()))
        print(f"[MemoryEngine] Pruned Redis memory for session {session_id}")


async def save_memory(user_id: str, agent_name: str, content: str, score: float, session_id: str = "default-session"):
    async with async_session() as session:
        memory = MemoryEntry(
            user_id=user_id,
            agent_name=agent_name,
            content=content,
            score=score,
        )
        session.add(memory)
        await session.commit()
        print(f'[Memory Saved] [{user_id}] {content[:100]}... (score: {score})')

    # Save to Redis
    trace = MemoryTrace(content=content, score=score)
    memory_engine.store_trace(session_id, trace)


# ✅ Singleton instance
memory_engine = MemoryEngine()
