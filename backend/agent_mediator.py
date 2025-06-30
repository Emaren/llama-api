class AgentMediator:
    def __init__(self, agents):
        self.agents = agents

    def mediate(self, issue):
        # Simple round-robin to collect opinions
        opinions = {}
        for name, agent in self.agents.items():
            opinions[name] = agent.opine(issue)
        # Aggregate or pick consensus
        consensus = self.aggregate_opinions(opinions)
        return consensus

    def aggregate_opinions(self, opinions):
        # Basic majority or weighted logic placeholder
        return max(set(opinions.values()), key=list(opinions.values()).count)
