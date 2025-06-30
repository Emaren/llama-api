class TeamCoordinator:
    def __init__(self, agents):
        self.agents = agents  # dict of agent_name -> agent_instance

    def delegate_task(self, task):
        """
        Distribute subtasks to specialized agents and aggregate results.
        """
        results = {}
        for agent_name, agent in self.agents.items():
            if agent.can_handle(task):
                results[agent_name] = agent.handle(task)
        return results

    def run_team_cycle(self, tasks):
        """
        Run a full cycle of team tasks with collaboration.
        """
        aggregated = {}
        for task in tasks:
            partials = self.delegate_task(task)
            aggregated[task['id']] = partials
        return aggregated
