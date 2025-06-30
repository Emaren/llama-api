\"\"\"
reflection_generator.py – Generates reflective responses based on memory input
and introspective cues, guiding learning and self-improvement.
\"\"\"

from shared.reflection_templates import TEMPLATES
from shared.utils import summarize

class ReflectionGenerator:
    def __init__(self):
        self.templates = TEMPLATES

    def generate(self, context: dict) -> str:
        if not context:
            return None

        template = self.select_template(context)
        memory_summary = summarize(context.get("memories", []))
        reflection = template.format(summary=memory_summary)
        return reflection

    def select_template(self, context: dict) -> str:
        # Pick template based on emotional tone, topic, or system phase
        return self.templates.get("default", "Reflecting on: {summary}")
