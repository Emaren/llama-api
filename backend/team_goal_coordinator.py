class TeamGoalCoordinator:
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        if goal not in self.goals:
            self.goals.append(goal)

    def remove_goal(self, goal):
        if goal in self.goals:
            self.goals.remove(goal)

    def list_goals(self):
        return self.goals
