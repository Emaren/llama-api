class TeamDecisionMaker:
    def __init__(self):
        self.decisions = []

    def make_decision(self, decision):
        self.decisions.append(decision)

    def get_decisions(self):
        return self.decisions
