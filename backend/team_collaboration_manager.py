class TeamCollaborationManager:
    def __init__(self):
        self.collaborations = {}

    def start_collaboration(self, collaboration_id, agents):
        self.collaborations[collaboration_id] = {
            "agents": agents,
            "status": "active"
        }

    def end_collaboration(self, collaboration_id):
        if collaboration_id in self.collaborations:
            self.collaborations[collaboration_id]["status"] = "ended"

    def get_collaboration(self, collaboration_id):
        return self.collaborations.get(collaboration_id)
