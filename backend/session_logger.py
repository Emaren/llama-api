\"\"\"
session_logger.py – Logs session-level metadata, events, errors, and system messages.
Supports tracing issues, auditing, and performance analysis.
\"\"\"

import datetime

class SessionLogger:
    def __init__(self):
        self.logs = []

    def log_event(self, session_id: str, event: str):
        timestamp = datetime.datetime.utcnow().isoformat()
        log_entry = {"timestamp": timestamp, "session_id": session_id, "event": event}
        self.logs.append(log_entry)
        print(f"[SessionLogger] {log_entry}")

    def get_logs(self, session_id: str = None) -> list[dict]:
        if session_id:
            return [log for log in self.logs if log["session_id"] == session_id]
        return self.logs
