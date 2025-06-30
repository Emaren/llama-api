\"\"\"
feedback_auditor.py – Audits feedback handling to detect neglected issues or
mismatched resolutions based on type, urgency, and recurrence.
\"\"\"

from backend.feedback_tracker import FeedbackTracker

class FeedbackAuditor:
    def __init__(self):
        self.tracker = FeedbackTracker()

    def audit_session(self, session_id: str):
        feedback_items = self.tracker.get_feedback(session_id)
        unresolved = [item for item in feedback_items if not item.get("resolved")]
        if unresolved:
            print(f"[FeedbackAuditor] Unresolved items found in session {session_id}")
        return unresolved

    def flag_recurring_issues(self):
        recurring = self.tracker.get_recurring_issues()
        for issue in recurring:
            print(f"[FeedbackAuditor] Recurring issue flagged: {issue['description']}")
        return recurring
