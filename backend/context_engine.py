\"\"\"
context_engine.py – Constructs and maintains conversational context state.
Combines user input, session memory, and agent insights.
\"\"\"

from backend.memory_loader import MemoryLoader
from backend.insight_generator import InsightGenerator
from backend.context_scope_analyzer import ContextScopeAnalyzer

class ContextEngine:
    def __init__(self):
        self.memory_loader = MemoryLoader()
        self.insight_generator = InsightGenerator()
        self.scope_analyzer = ContextScopeAnalyzer()

    def build_context(self, user_input: str, session_id: str) -> dict:
        print(f"[ContextEngine] Building context for session: {session_id}")
        memory = self.memory_loader.load(session_id)
        insights = self.insight_generator.generate(memory)
        scope = self.scope_analyzer.analyze(user_input)

        return {
            "input": user_input,
            "memory": memory,
            "insights": insights,
            "scope": scope
        }
