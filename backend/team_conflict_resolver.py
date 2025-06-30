class TeamConflictResolver:
    def __init__(self):
        self.conflicts = []

    def add_conflict(self, conflict_detail):
        self.conflicts.append(conflict_detail)

    def resolve_conflict(self, conflict_detail):
        if conflict_detail in self.conflicts:
            self.conflicts.remove(conflict_detail)

    def get_conflicts(self):
        return self.conflicts
