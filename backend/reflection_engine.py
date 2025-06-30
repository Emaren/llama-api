\"\"\"
reflection_engine.py – Generates introspective responses, manages reflection chains,
and triggers deep learning based on past interactions.
\"\"\"

from backend.reflection_generator import ReflectionGenerator
from backend.reflection_scheduler import ReflectionScheduler
from backend.self_reflection_writer import SelfReflectionWriter
from backend.memory_loader import MemoryLoader
from shared.constants import REFLECTION_DEPTH_LIMIT

class ReflectionEngine:
    def __init__(self):
        self.generator = ReflectionGenerator()
        self.scheduler = ReflectionScheduler()
        self.writer = SelfReflectionWriter()
        self.loader = MemoryLoader()

    def generate(self, trigger_input: str):
        reflections = []
        relevant_memories = self.loader.load_related(trigger_input)

        for depth in range(REFLECTION_DEPTH_LIMIT):
            scheduled = self.scheduler.schedule(reflections, relevant_memories)
            new_reflection = self.generator.generate(scheduled)
            if not new_reflection:
                break
            reflections.append(new_reflection)
            self.writer.write(new_reflection)

        return reflections[-1] if reflections else None
