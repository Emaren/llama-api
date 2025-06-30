# backend/agent_alignment_auditor.py
# Audits agent alignment over time and surfaces repeat violations or trends.

from backend.agent_alignment_manager import AgentAlignmentManager
from collections import Counter

class AgentAlignmentAuditor:
    def __init__(self):
        self.manager = AgentAlignmentManager()

    def audit_agent(self, agent_id):
        flags = self.manager.get_flags(agent_id)
        if not flags:
            return {
                "agent_id": agent_id,
                "violation_count": 0,
                "frequent_issues": []
            }

        all_issues = []
        for entry in flags:
            all_issues.extend(entry["issues"])

        issue_counts = Counter(all_issues)
        return {
            "agent_id": agent_id,
            "violation_count": len(flags),
            "frequent_issues": issue_counts.most_common(5)
        }

    def audit_multiple(self, agent_ids):
        return [self.audit_agent(agent_id) for agent_id in agent_ids]
