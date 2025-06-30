class TeamResourceManager:
    def __init__(self):
        self.resources = {}

    def allocate(self, resource_name, agent_name):
        self.resources[resource_name] = agent_name

    def deallocate(self, resource_name):
        if resource_name in self.resources:
            del self.resources[resource_name]

    def get_allocation(self, resource_name):
        return self.resources.get(resource_name)
