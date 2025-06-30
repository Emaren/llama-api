\"\"\"
query_classifier.py – Classifies incoming queries into predefined types such as
reflection, diagnostic, meta, or general chat to route appropriately.
\"\"\"

from shared.query_types import QUERY_TYPES

class QueryClassifier:
    def __init__(self):
        self.types = QUERY_TYPES

    def classify(self, user_input: str) -> str:
        input_lower = user_input.lower()
        for qtype, keywords in self.types.items():
            if any(keyword in input_lower for keyword in keywords):
                return qtype
        return "general"
