# backend/agent_alignment_manager.py
# Evaluates and manages alignment of agent behavior to system values and rules.

from backend.validation.alignment_checker import AlignmentChecker
from backend.feedback_tracker import FeedbackTracker

class AgentAlignmentManager:
    def __init__(self):
        self.alignment_checker = AlignmentChecker()
        self.feedback_tracker = FeedbackTracker()
        self.flags = {}

    def evaluate_alignment(self, agent_id, output):
        result = self.alignment_checker.check(output)
        if not result["aligned"]:
            self._flag(agent_id, result["issues"])
        return result

    def _flag(self, agent_id, issues):
        if agent_id not in self.flags:
            self.flags[agent_id] = []
        self.flags[agent_id].append({
            "issues": issues,
            "timestamp": self._now()
        })
        print(f"[🚨 ALIGNMENT ALERT] Agent {agent_id}: {issues}")

    def get_flags(self, agent_id):
        return self.flags.get(agent_id, [])

    def _now(self):
        from datetime import datetime
        return datetime.utcnow().isoformat()
