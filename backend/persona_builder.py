\"\"\"
persona_builder.py – Builds or updates agent personas using reflection insights,
behavior patterns, feedback, and goal alignment.
\"\"\"

from backend.reflection_engine import ReflectionEngine
from backend.feedback_tracker import FeedbackTracker
from data.persona_profile import DEFAULT_PERSONA_TEMPLATE

class PersonaBuilder:
    def __init__(self):
        self.reflection_engine = ReflectionEngine()
        self.feedback_tracker = FeedbackTracker()

    def build_persona(self, session_id: str):
        reflection = self.reflection_engine.generate(session_id)
        feedback_summary = self.feedback_tracker.summarize(session_id)
        persona = DEFAULT_PERSONA_TEMPLATE.copy()
        persona["insights"] = reflection
        persona["feedback_summary"] = feedback_summary
        return persona

    def update_persona(self, current_persona: dict, session_id: str):
        updates = self.build_persona(session_id)
        current_persona.update(updates)
        return current_persona
