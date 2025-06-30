# backend/agent_temporal_context.py
# Tracks and manages temporal context and event sequencing.

from datetime import datetime, timedelta

class AgentTemporalContext:
    def __init__(self):
        self.context_windows = {}  # {agent_id: [ {start, end, context_data} ]}

    def add_context_window(self, agent_id, start: datetime, end: datetime, context_data):
        if agent_id not in self.context_windows:
            self.context_windows[agent_id] = []
        self.context_windows[agent_id].append({
            "start": start.isoformat(),
            "end": end.isoformat(),
            "context_data": context_data
        })

    def get_context_for_time(self, agent_id, timestamp: datetime):
        windows = self.context_windows.get(agent_id, [])
        for window in windows:
            start = datetime.fromisoformat(window["start"])
            end = datetime.fromisoformat(window["end"])
            if start <= timestamp <= end:
                return window["context_data"]
        return None
