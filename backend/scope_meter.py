\"\"\"
scope_meter.py – Quantifies usage of conversational scope, measuring how much
of the context budget is currently consumed or remaining.
\"\"\"

from shared.constants import MAX_CONTEXT_TOKENS

class ScopeMeter:
    def __init__(self):
        self.current_usage = 0

    def update_usage(self, token_count: int):
        self.current_usage = token_count
        print(f"[ScopeMeter] Updated context usage to {self.current_usage} tokens")

    def get_remaining_budget(self) -> int:
        remaining = MAX_CONTEXT_TOKENS - self.current_usage
        print(f"[ScopeMeter] Remaining budget: {remaining} tokens")
        return max(0, remaining)

    def is_near_limit(self, threshold: float = 0.9) -> bool:
        near_limit = self.current_usage >= MAX_CONTEXT_TOKENS * threshold
        print(f"[ScopeMeter] Near limit: {near_limit}")
        return near_limit
