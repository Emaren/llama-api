\"\"\"
memory_engine.py – Central engine for memory access, persistence, lookup, and injection
across conversational sessions and memory modules.
\"\"\"

from shared.memory_types import MemoryTrace
from backend.memory_scoper import MemoryScoper
from backend.memory_loader import MemoryLoader
from backend.memory_pruner import MemoryPruner

class MemoryEngine:
    def __init__(self):
        self.loader = MemoryLoader()
        self.pruner = MemoryPruner()
        self.scoper = MemoryScoper()
        self.memory_store = {}

    def store_trace(self, session_id: str, trace: MemoryTrace):
        if session_id not in self.memory_store:
            self.memory_store[session_id] = []
        self.memory_store[session_id].append(trace)
        print(f"[MemoryEngine] Stored trace in session {session_id}: {trace.content}")

    def retrieve_scope(self, session_id: str, query: str):
        traces = self.memory_store.get(session_id, [])
        scoped = self.scoper.scope(traces, query)
        print(f"[MemoryEngine] Retrieved {len(scoped)} scoped traces for session {session_id}")
        return scoped

    def prune_memory(self, session_id: str):
        traces = self.memory_store.get(session_id, [])
        self.memory_store[session_id] = self.pruner.prune(traces)
        print(f"[MemoryEngine] Pruned memory for session {session_id}")
