\"\"\"
self_reflection_generator.py – Generates tailored introspective prompts
based on agent state, feedback, and prior memory interactions.
\"\"\"

from shared.reflection_templates import get_reflection_templates
from backend.memory_engine import MemoryEngine

class ReflectionGenerator:
    def __init__(self):
        self.memory = MemoryEngine()
        self.templates = get_reflection_templates()

    def generate(self, agent_id: str) -> list[str]:
        recent_insights = self.memory.fetch_recent_insights(agent_id)
        questions = []

        for template in self.templates:
            q = template.format(insight=recent_insights.pop(0) if recent_insights else "N/A")
            questions.append(q)

        return questions
