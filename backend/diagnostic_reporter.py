\"\"\"
diagnostic_reporter.py – Aggregates system health, usage stats, and module status
into a structured report for UI or logs.
\"\"\"

from backend.health_checker import HealthChecker
from backend.memory_metrics import MemoryMetrics
from backend.feedback_tracker import FeedbackTracker
import datetime

class DiagnosticReporter:
    def __init__(self):
        self.health_checker = HealthChecker()
        self.memory_metrics = MemoryMetrics()
        self.feedback_tracker = FeedbackTracker()

    def generate_report(self) -> dict:
        timestamp = datetime.datetime.now().isoformat()
        print(f"[Diagnostics] Generating report @ {timestamp}")
        return {
            "timestamp": timestamp,
            "system_health": self.health_checker.check_system(),
            "memory_metrics": self.memory_metrics.get_summary(),
            "feedback_summary": self.feedback_tracker.get_summary()
        }
