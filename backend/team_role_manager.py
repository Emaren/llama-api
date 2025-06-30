class TeamRoleManager:
    def __init__(self):
        self.roles = {}

    def assign_role(self, agent_name, role):
        self.roles[agent_name] = role

    def get_role(self, agent_name):
        return self.roles.get(agent_name)

    def remove_role(self, agent_name):
        if agent_name in self.roles:
            del self.roles[agent_name]
