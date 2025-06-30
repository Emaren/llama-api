# backend/agent_course_correction.py
# Synthesizes signals from drift, alignment, and goals to steer agents.

from backend.agent_drift_detector import AgentDriftDetector
from backend.agent_alignment_tracker import AgentAlignmentTracker
from backend.agent_nudging_engine import AgentNudgingEngine

class AgentCourseCorrection:
    def __init__(self):
        self.drift = AgentDriftDetector()
        self.alignment = AgentAlignmentTracker()
        self.nudger = AgentNudgingEngine()

    def evaluate_and_correct(self, agent_id, current_task):
        drift_result = self.drift.detect_drift(agent_id, current_task)
        avg_align = self.alignment.average_alignment(agent_id)

        if drift_result["drift"]:
            msg = f"⚠️ Detected drift: {drift_result['reason']}"
            self.nudger.send_nudge(agent_id, msg)

        if avg_align < 0.6:
            msg = f"⚠️ Low alignment score ({avg_align}) — re-evaluate priorities."
            self.nudger.send_nudge(agent_id, msg)

        return {
            "drift_check": drift_result,
            "alignment_score": avg_align,
            "nudges_sent": self.nudger.get_nudges(agent_id)[-2:]
        }
