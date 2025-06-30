\"\"\"
self_reflector.py – Orchestrates the full cycle of self-reflection, triggering
generation of prompts, introspective responses, and logging via journal.
\"\"\"

from backend.reflection_generator import ReflectionGenerator
from backend.self_reflection_writer import ReflectionWriter

class SelfReflector:
    def __init__(self):
        self.generator = ReflectionGenerator()
        self.writer = ReflectionWriter()

    def reflect(self, agent_id: str):
        print(f"[SelfReflector] Initiating reflection cycle for {agent_id}...")
        self.writer.perform_reflection(agent_id)
        print(f"[SelfReflector] Reflection complete.")
