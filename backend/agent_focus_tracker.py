# backend/agent_focus_tracker.py
# Logs and monitors agent focus over time for analysis and adjustment.

from datetime import datetime

class AgentFocusTracker:
    def __init__(self):
        self.focus_log = {}  # {agent_id: [ {focus, timestamp} ]}

    def record_focus(self, agent_id, focus_map):
        entry = {
            "focus": focus_map,
            "timestamp": self._now()
        }
        if agent_id not in self.focus_log:
            self.focus_log[agent_id] = []
        self.focus_log[agent_id].append(entry)

    def get_focus_history(self, agent_id, limit=10):
        return self.focus_log.get(agent_id, [])[-limit:]

    def detect_drift(self, agent_id):
        history = self.get_focus_history(agent_id, limit=5)
        if not history:
            return None
        recent_focus_keys = [list(entry["focus"].keys())[0] for entry in history if entry["focus"]]
        return len(set(recent_focus_keys)) > 3  # Arbitrary threshold

    def _now(self):
        return datetime.utcnow().isoformat()
