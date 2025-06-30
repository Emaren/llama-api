\"\"\"
health_checker.py – Scans and reports health across backend modules,
including memory usage, system flags, and feedback queues.
\"\"\"

from shared.system_flags import SYSTEM_FLAGS
from backend.memory_health_monitor import MemoryHealthMonitor
from backend.feedback_auditor import FeedbackAuditor

class HealthChecker:
    def __init__(self):
        self.memory_monitor = MemoryHealthMonitor()
        self.feedback_auditor = FeedbackAuditor()

    def check_system(self):
        print("[HealthChecker] Running diagnostics...")
        memory_report = self.memory_monitor.check_health()
        feedback_report = self.feedback_auditor.audit()
        system_status = {
            "memory_health": memory_report,
            "feedback_integrity": feedback_report,
            "flags": SYSTEM_FLAGS
        }
        return system_status
