def get_scoped_memory(memory: list, task_type: str, agent_role: str) -> list:
    """
    Filter memory items based on task type and agent role.

    Args:
        memory (list): All available memory entries.
        task_type (str): Current task type (e.g. 'generation', 'evaluation').
        agent_role (str): Role of requesting agent (e.g. 'navigator', 'scribe').

    Returns:
        list: Filtered memory relevant to the current task and role.
    """
    return [
        item for item in memory
        if task_type in item.get("tags", []) or agent_role in item.get("visibility", [])
    ]
