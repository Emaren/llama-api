\"\"\"
feedback_tracker.py – Tracks feedback from users and internal evaluations,
storing data for auditing, aggregation, and long-term trend analysis.
\"\"\"

from collections import defaultdict
from datetime import datetime

class FeedbackTracker:
    def __init__(self):
        self.feedback_log = defaultdict(list)

    def track(self, session_id: str, feedback: dict):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "feedback": feedback,
            "resolved": False
        }
        self.feedback_log[session_id].append(entry)
        print(f"[FeedbackTracker] Feedback logged for session {session_id}")

    def resolve_feedback(self, session_id: str, index: int):
        try:
            self.feedback_log[session_id][index]["resolved"] = True
            print(f"[FeedbackTracker] Resolved feedback item {index} in session {session_id}")
        except IndexError:
            print(f"[FeedbackTracker] No such feedback item at index {index}")

    def get_feedback(self, session_id: str):
        return self.feedback_log.get(session_id, [])

    def get_recurring_issues(self):
        issues = defaultdict(int)
        for session_entries in self.feedback_log.values():
            for entry in session_entries:
                desc = entry["feedback"].get("description", "")
                if desc:
                    issues[desc] += 1
        return [{"description": k, "count": v} for k, v in issues.items() if v > 1]
