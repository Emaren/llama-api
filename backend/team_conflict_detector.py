class TeamConflictDetector:
    def __init__(self):
        self.conflicts = []

    def detect_conflict(self, conflict):
        self.conflicts.append(conflict)

    def get_conflicts(self):
        return self.conflicts

    def clear_conflicts(self):
        self.conflicts.clear()
