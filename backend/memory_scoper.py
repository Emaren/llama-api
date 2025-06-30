\"\"\"
memory_scoper.py – Assigns a contextual scope to each memory (e.g., global, session-specific, topic-based)
for improved relevance targeting and memory retrieval.
\"\"\"

from shared.memory_types import MemoryTrace

class MemoryScoper:
    def __init__(self):
        pass

    def assign_scope(self, trace: MemoryTrace, context: dict) -> str:
        # Example scope logic: if topic matches current session focus
        if "topic" in context and context["topic"] in trace.tags:
            trace.scope = "topic"
        elif trace.session_id == context.get("session_id"):
            trace.scope = "session"
        else:
            trace.scope = "global"
        return trace.scope
