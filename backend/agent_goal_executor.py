# backend/agent_goal_executor.py
# Executes agent goals using internal tools or delegating to modules.

from backend.tools.tool_registry import ToolRegistry
from backend.module_dispatcher import ModuleDispatcher

class AgentGoalExecutor:
    def __init__(self):
        self.tool_registry = ToolRegistry()
        self.dispatcher = ModuleDispatcher()

    def execute_goal(self, agent_id, goal):
        tool = self.tool_registry.get_tool_for_goal(goal)
        if tool:
            return tool.run(agent_id=agent_id, goal=goal)
        else:
            return self.dispatcher.dispatch(agent_id, goal)

    def execute_batch(self, agent_id, goals):
        results = []
        for goal in goals:
            result = self.execute_goal(agent_id, goal)
            results.append({"goal": goal, "result": result})
        return results
