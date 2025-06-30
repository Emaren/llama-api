class TeamCollaborationTools:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, tool):
        self.tools[name] = tool

    def use_tool(self, name, *args, **kwargs):
        tool = self.tools.get(name)
        if tool:
            return tool(*args, **kwargs)
        else:
            raise ValueError(f"Tool {name} not found")
