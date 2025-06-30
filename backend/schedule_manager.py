\"\"\"
schedule_manager.py – Coordinates timing for memory updates, reflection sessions,
and diagnostics in sync with system operation cycles.
\"\"\"

import time
from backend.memory_engine import MemoryEngine
from backend.reflection_engine import ReflectionEngine
from backend.diagnostic_reporter import DiagnosticReporter

class ScheduleManager:
    def __init__(self):
        self.memory_engine = MemoryEngine()
        self.reflection_engine = ReflectionEngine()
        self.diagnostics = DiagnosticReporter()

    def run_cycle(self, session_id: str):
        print(f"[ScheduleManager] Running update cycle for session {session_id}")
        self.memory_engine.update_memory(session_id)
        self.reflection_engine.generate_reflection(session_id)
        diagnostics = self.diagnostics.report(session_id)
        return diagnostics

    def run_periodic_updates(self, session_id: str, interval_sec: int = 300):
        while True:
            self.run_cycle(session_id)
            time.sleep(interval_sec)
