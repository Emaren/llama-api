# backend/agent_alignment_reporter.py
# Summarizes agent alignment history and highlights potential issues.

from backend.agent_alignment_manager import AgentAlignmentManager

class AgentAlignmentReporter:
    def __init__(self):
        self.manager = AgentAlignmentManager()

    def generate_report(self, agent_id):
        flags = self.manager.get_flags(agent_id)
        if not flags:
            return f"✅ Agent {agent_id} has no recorded alignment violations."

        report_lines = [f"⚠️ Alignment Report for Agent {agent_id}:"]
        for entry in flags:
            issues = ", ".join(entry["issues"])
            report_lines.append(f"- {entry['timestamp']}: {issues}")
        return "\n".join(report_lines)

    def summarize_violations(self, agent_ids):
        summary = {}
        for agent_id in agent_ids:
            flags = self.manager.get_flags(agent_id)
            if flags:
                summary[agent_id] = len(flags)
        return summary
