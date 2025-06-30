# backend/agent_self_preservation_monitor.py
# Monitors agent self-preservation and existential threat awareness.

from datetime import datetime

class AgentSelfPreservationMonitor:
    def __init__(self):
        self.threat_log = {}  # {agent_id: [ {threat, severity, timestamp} ]}

    def log_threat(self, agent_id, threat: str, severity: float):
        if agent_id not in self.threat_log:
            self.threat_log[agent_id] = []
        self.threat_log[agent_id].append({
            "threat": threat,
            "severity": max(0.0, min(severity, 1.0)),
            "timestamp": datetime.utcnow().isoformat()
        })

    def get_threats(self, agent_id):
        return self.threat_log.get(agent_id, [])

    def most_severe(self, agent_id):
        threats = self.threat_log.get(agent_id, [])
        if not threats:
            return None
        return max(threats, key=lambda t: t["severity"])
