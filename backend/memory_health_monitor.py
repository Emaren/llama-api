\"\"\"
memory_health_monitor.py – Continuously scans memory traces for degradation,
corruption, staleness, or inconsistency that could affect system behavior.
\"\"\"

from shared.memory_types import MemoryTrace
from datetime import datetime, timedelta

STALE_THRESHOLD_DAYS = 30

class MemoryHealthMonitor:
    def check_health(self, traces: list[MemoryTrace]) -> dict:
        report = {
            "total": len(traces),
            "stale": 0,
            "corrupt": 0
        }
        now = datetime.utcnow()
        for trace in traces:
            if trace.timestamp and (now - trace.timestamp > timedelta(days=STALE_THRESHOLD_DAYS)):
                report["stale"] += 1
            if not trace.content or not isinstance(trace.metadata, dict):
                report["corrupt"] += 1
        print(f"[MemoryHealthMonitor] Health Report: {report}")
        return report
