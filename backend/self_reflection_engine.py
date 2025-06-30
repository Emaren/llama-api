\"\"\"
self_reflection_engine.py – Core engine that initiates, schedules, and
executes self-reflection tasks to enhance the agent’s internal alignment.
\"\"\"

from backend.reflection_generator import ReflectionGenerator
from backend.reflection_scheduler import ReflectionScheduler
from backend.self_reflection_writer import SelfReflectionWriter
from backend.feedback_tracker import FeedbackTracker
from shared.constants import SELF_REFLECTION_INTERVAL

class SelfReflectionEngine:
    def __init__(self):
        self.generator = ReflectionGenerator()
        self.scheduler = ReflectionScheduler()
        self.writer = SelfReflectionWriter()
        self.feedback = FeedbackTracker()

    def run_reflection_cycle(self, agent_id: str, session_id: str):
        if not self.scheduler.should_reflect(agent_id, interval=SELF_REFLECTION_INTERVAL):
            return None

        questions = self.generator.generate(agent_id)
        responses = []
        for q in questions:
            r = self.writer.compose(agent_id, q)
            responses.append({"question": q, "response": r})
            self.feedback.track(session_id, {"reflection": r})

        return responses
