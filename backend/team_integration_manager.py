class TeamIntegrationManager:
    def __init__(self):
        self.integrations = {}

    def add_integration(self, name, details):
        self.integrations[name] = details

    def get_integration(self, name):
        return self.integrations.get(name)

    def remove_integration(self, name):
        if name in self.integrations:
            del self.integrations[name]
