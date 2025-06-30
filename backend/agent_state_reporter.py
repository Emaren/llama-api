# backend/agent_state_reporter.py
# Generates human-readable summaries of logged agent states.

import json
from collections import Counter
from backend.agent_state_logger import AgentStateLogger

class AgentStateReporter:
    def __init__(self, log_path="data/agent_state_log.jsonl"):
        self.logger = AgentStateLogger(log_path=log_path)

    def summarize_recent_states(self, agent_id, limit=5):
        entries = [e for e in self.logger.tail_log(n=50) if e["agent_id"] == agent_id][-limit:]
        if not entries:
            return f"No recent state logs for agent {agent_id}."

        report = [f"📊 Agent State Summary (last {len(entries)} entries):"]
        roles = Counter()
        statuses = Counter()

        for e in entries:
            awareness = e["state"].get("awareness", {})
            roles[awareness.get("role", "unknown")] += 1
            statuses[awareness.get("status", "unknown")] += 1
            report.append(f"- {e['timestamp']} | Role: {awareness.get('role')} | Status: {awareness.get('status')}")

        report.append(f"\n🔁 Role Distribution: {dict(roles)}")
        report.append(f"🔎 Status Distribution: {dict(statuses)}")
        return "\n".join(report)
