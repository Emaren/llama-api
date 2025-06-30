class TeamInitiativeManager:
    def __init__(self):
        self.initiatives = []

    def add_initiative(self, initiative):
        self.initiatives.append(initiative)

    def list_initiatives(self):
        return self.initiatives
