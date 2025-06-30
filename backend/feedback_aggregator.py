\"\"\"
feedback_aggregator.py – Collects feedback across sessions and summarizes
trends in positivity, suggestions, and critical issues.
\"\"\"

from collections import defaultdict

class FeedbackAggregator:
    def __init__(self):
        self.feedback_by_type = defaultdict(list)

    def record_feedback(self, category: str, message: str):
        self.feedback_by_type[category].append(message)
        print(f"[FeedbackAggregator] Logged feedback in category: {category}")

    def summarize(self):
        summary = {}
        for category, messages in self.feedback_by_type.items():
            summary[category] = {
                "count": len(messages),
                "sample": messages[-3:]
            }
        return summary
