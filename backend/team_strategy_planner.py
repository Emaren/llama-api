class TeamStrategyPlanner:
    def __init__(self):
        self.strategies = {}

    def add_strategy(self, strategy_name, details):
        self.strategies[strategy_name] = details

    def get_strategy(self, strategy_name):
        return self.strategies.get(strategy_name)

    def remove_strategy(self, strategy_name):
        if strategy_name in self.strategies:
            del self.strategies[strategy_name]
