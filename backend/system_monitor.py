"""
system_monitor.py – Monitors system resource usage and error rates
to maintain operational stability.
"""

import psutil
import datetime

class SystemMonitor:
    def __init__(self):
        self.error_log = []

    def check_resources(self) -> dict:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        timestamp = datetime.datetime.utcnow().isoformat()
        status = {
            "cpu_percent": cpu,
            "memory_percent": memory,
            "timestamp": timestamp
        }
        print(f"[SystemMonitor] Status: {status}")
        return status

    def log_error(self, error_msg: str):
        timestamp = datetime.datetime.utcnow().isoformat()
        self.error_log.append({"timestamp": timestamp, "error": error_msg})
        print(f"[SystemMonitor] Error logged: {error_msg}")

    def get_error_log(self) -> list:
        return self.error_log

# Simple callable for boot scripts
def check_system_status():
    monitor = SystemMonitor()
    return monitor.check_resources()
