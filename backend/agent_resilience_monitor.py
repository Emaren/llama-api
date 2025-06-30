# backend/agent_resilience_monitor.py
# Tracks agent recovery patterns to assess resilience and adaptive strength.

from datetime import datetime, timedelta

class AgentResilienceMonitor:
    def __init__(self):
        self.failure_events = {}  # {agent_id: [timestamp]}
        self.recovery_events = {}  # {agent_id: [timestamp]}

    def log_failure(self, agent_id):
        self._log_event(self.failure_events, agent_id)

    def log_recovery(self, agent_id):
        self._log_event(self.recovery_events, agent_id)

    def calculate_resilience_score(self, agent_id, window_minutes=60):
        failures = self._recent_events(self.failure_events.get(agent_id, []), window_minutes)
        recoveries = self._recent_events(self.recovery_events.get(agent_id, []), window_minutes)
        if not failures:
            return 1.0
        return min(1.0, len(recoveries) / len(failures))

    def _log_event(self, store, agent_id):
        if agent_id not in store:
            store[agent_id] = []
        store[agent_id].append(datetime.utcnow())

    def _recent_events(self, events, window_minutes):
        cutoff = datetime.utcnow() - timedelta(minutes=window_minutes)
        return [e for e in events if e >= cutoff]
