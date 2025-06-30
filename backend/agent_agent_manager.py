# backend/team_agent_manager.py
# Manages individual agents within a team context

class TeamAgentManager:
    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def get_agent(self, agent_id):
        for agent in self.agents:
            if agent.id == agent_id:
                return agent
        return None

    def remove_agent(self, agent_id):
        self.agents = [a for a in self.agents if a.id != agent_id]

