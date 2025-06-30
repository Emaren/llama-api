# backend/agent_alignment_interface.py
# Unified interface for managing agent alignment lifecycle.

from backend.agent_alignment_manager import AgentAlignmentManager
from backend.agent_alignment_reporter import AgentAlignmentReporter
from backend.agent_alignment_notifier import AgentAlignmentNotifier
from backend.agent_alignment_resolver import AgentAlignmentResolver

class AgentAlignmentInterface:
    def __init__(self):
        self.manager = AgentAlignmentManager()
        self.reporter = AgentAlignmentReporter()
        self.notifier = AgentAlignmentNotifier()
        self.resolver = AgentAlignmentResolver()

    def full_alignment_check(self, agent_id, output):
        result = self.manager.evaluate_alignment(agent_id, output)
        if not result["aligned"]:
            self.notifier.check_and_notify(agent_id)
            resolution = self.resolver.resolve_violations(agent_id)
            return {
                "aligned": False,
                "report": self.reporter.generate_report(agent_id),
                "resolution": resolution
            }
        return {"aligned": True, "message": "No violations detected."}
