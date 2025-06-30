import datetime

tool_log = []


def log_tool_usage(tool_name: str, agent_id: str, params: dict):
    """
    Record a tool usage event.

    Args:
        tool_name (str): The name of the tool used.
        agent_id (str): The ID of the agent invoking the tool.
        params (dict): Input parameters used with the tool.
    """
    event = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "tool": tool_name,
        "agent": agent_id,
        "params": params
    }
    tool_log.append(event)
