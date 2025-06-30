\"\"\"
prompt_strategy_manager.py – Chooses the most effective strategy for
prompt construction based on input scope, user intent, and system goals.
\"\"\"

from shared.strategies_config import STRATEGY_MAP

class PromptStrategyManager:
    def __init__(self):
        self.strategy_map = STRATEGY_MAP

    def select_strategy(self, scope: str) -> dict:
        if scope in self.strategy_map:
            return self.strategy_map[scope]
        return self.strategy_map.get("default", {})
