class TeamRiskManager:
    def __init__(self):
        self.risks = []

    def log_risk(self, risk):
        self.risks.append(risk)

    def assess_risks(self):
        # Basic risk assessment placeholder
        return {risk: "low" for risk in self.risks}
