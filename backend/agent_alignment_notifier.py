# backend/agent_alignment_notifier.py
# Triggers alerts when agents violate alignment thresholds.

from backend.agent_alignment_auditor import AgentAlignmentAuditor

class AgentAlignmentNotifier:
    def __init__(self, violation_threshold=3):
        self.auditor = AgentAlignmentAuditor()
        self.threshold = violation_threshold

    def check_and_notify(self, agent_id):
        audit = self.auditor.audit_agent(agent_id)
        if audit["violation_count"] >= self.threshold:
            self._send_alert(agent_id, audit)

    def _send_alert(self, agent_id, audit):
        print(f"[🚨 ALIGNMENT NOTIFIER] Agent {agent_id} has {audit['violation_count']} violations!")
        for issue, count in audit["frequent_issues"]:
            print(f"  - {issue}: {count} times")
