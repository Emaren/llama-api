# backend/team_adaptation_manager.py
# Handles adaptive behavior for teams based on context and performance

class TeamAdaptationManager:
    def __init__(self):
        self.adaptations = {}

    def add_adaptation(self, team_id, adaptation):
        self.adaptations[team_id] = adaptation

    def get_adaptation(self, team_id):
        return self.adaptations.get(team_id, None)

    def remove_adaptation(self, team_id):
        if team_id in self.adaptations:
            del self.adaptations[team_id]

