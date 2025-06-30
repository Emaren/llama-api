# backend/agent_alignment_summary.py
# Combines alignment, bias, and perception for a holistic agent integrity score.

from backend.agent_alignment_auditor import AgentAlignmentAuditor
from backend.agent_bias_monitor import AgentBiasMonitor
from backend.agent_awareness_tracker import AgentAwarenessTracker
from backend.agent_perception_tracker import AgentPerceptionTracker

class AgentAlignmentSummary:
    def __init__(self):
        self.alignment_auditor = AgentAlignmentAuditor()
        self.bias_monitor = AgentBiasMonitor()
        self.awareness_tracker = AgentAwarenessTracker()
        self.perception_tracker = AgentPerceptionTracker()

    def summarize(self, agent_id):
        alignment = self.alignment_auditor.audit_agent(agent_id)
        bias_data = self.bias_monitor.bias_log.get(agent_id, [])
        awareness = self.awareness_tracker.get_history(agent_id)
        perception = self.perception_tracker.get_recent_perceptions(agent_id)

        summary = {
            "agent_id": agent_id,
            "violations": alignment["violation_count"],
            "frequent_issues": alignment["frequent_issues"],
            "bias_trend": bias_data[-1] if bias_data else {},
            "awareness_stability": len(set(a['state']['role'] for a in awareness)) <= 1,
            "perception_entries": len(perception),
            "last_perception": perception[-1]["state"] if perception else {}
        }

        return summary
