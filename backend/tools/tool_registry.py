registered_tools = {
    "summarizer": "tools.summarize",
    "translator": "tools.translate",
    "planner": "tools.plan_steps",
    "searcher": "tools.search_query"
}


def get_tool_path(tool_name: str) -> str:
    """
    Retrieve the module path for a given tool.

    Args:
        tool_name (str): Name of the tool.

    Returns:
        str: Python module path to tool.
    """
    return registered_tools.get(tool_name, "tools.default_fallback")
