\"\"\"
context_scope_analyzer.py – Analyzes user input and assigns contextual scope
(e.g., memory recall, planning, reflection, scoring).
\"\"\"

import re
import random
from shared.query_types import QUERY_TYPES

class ContextScopeAnalyzer:
    def __init__(self):
        self.types = QUERY_TYPES

    def analyze(self, user_input: str) -> dict:
        print(f"[ScopeAnalyzer] Analyzing: '{user_input}'")
        scores = {}
        lowered = user_input.lower()

        for scope, patterns in self.types.items():
            scores[scope] = sum(bool(re.search(p, lowered)) for p in patterns)

        # Normalize scores
        total = sum(scores.values()) or 1
        for scope in scores:
            scores[scope] = round(scores[scope] / total, 3)

        return scores
