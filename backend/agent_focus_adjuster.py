# backend/agent_focus_adjuster.py
# Dynamically nudges agent focus back on track when drift or distraction is detected.

from backend.agent_focus_tracker import AgentFocusTracker
from backend.agent_task_focus import AgentTaskFocus
from backend.project_health_tracker import ProjectHealthTracker

class AgentFocusAdjuster:
    def __init__(self):
        self.focus_tracker = AgentFocusTracker()
        self.task_focus = AgentTaskFocus()
        self.project_health = ProjectHealthTracker()

    def adjust_focus_if_needed(self, agent_id, context):
        drift_detected = self.focus_tracker.detect_drift(agent_id)
        if drift_detected:
            new_focus = self.task_focus.determine_focus(agent_id, context)
            self.focus_tracker.record_focus(agent_id, new_focus)
            self._log_adjustment(agent_id, new_focus)
            return new_focus
        return None

    def _log_adjustment(self, agent_id, new_focus):
        print(f"[FOCUS-ADJUST] Agent {agent_id} nudged to new focus: {list(new_focus.keys())[:3]}")
