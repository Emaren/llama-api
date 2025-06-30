class TeamGoalManager:
    def __init__(self):
        self.goals = {}

    def set_goal(self, goal_name, goal_details):
        self.goals[goal_name] = goal_details

    def get_goal(self, goal_name):
        return self.goals.get(goal_name)

    def remove_goal(self, goal_name):
        if goal_name in self.goals:
            del self.goals[goal_name]
