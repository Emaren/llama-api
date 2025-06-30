# backend/agent_adaptation_manager.py
# Handles agent adaptation strategies based on environment and user feedback

class AdaptationManager:
    def __init__(self):
        self.strategies = []

    def add_strategy(self, strategy):
        self.strategies.append(strategy)

    def apply_strategies(self, agent, context):
        for strategy in self.strategies:
            strategy.apply(agent, context)

