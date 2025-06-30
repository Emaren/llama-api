\"\"\"
context_scope_meter.py – Measures and logs context distribution across sessions.
Used for UI graphing and tracking cognitive load.
\"\"\"

from collections import defaultdict
import datetime

class ContextScopeMeter:
    def __init__(self):
        self.scope_log = defaultdict(list)

    def log_scope(self, session_id: str, scope_distribution: dict):
        timestamp = datetime.datetime.now().isoformat()
        self.scope_log[session_id].append({
            "timestamp": timestamp,
            "distribution": scope_distribution
        })
        print(f"[ScopeMeter] Logged scope for {session_id} @ {timestamp}")

    def get_scope_history(self, session_id: str):
        return self.scope_log.get(session_id, [])
