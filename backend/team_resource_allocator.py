class TeamResourceAllocator:
    def __init__(self):
        self.resources = {}

    def allocate_resource(self, resource_name, agent_name):
        self.resources[resource_name] = agent_name

    def get_allocation(self, resource_name):
        return self.resources.get(resource_name)

    def release_resource(self, resource_name):
        if resource_name in self.resources:
            del self.resources[resource_name]
