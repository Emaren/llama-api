class TeamCollaborationTracker:
    def __init__(self):
        self.collaborations = []

    def add_collaboration(self, collaboration):
        self.collaborations.append(collaboration)

    def get_collaborations(self):
        return self.collaborations
