def should_delegate(task: dict) -> bool:
    """
    Decide whether to delegate a task based on complexity or scope.

    Args:
        task (dict): Task metadata including type, difficulty, and required expertise.

    Returns:
        bool: True if delegation is recommended.
    """
    return task.get("complexity", 0) > 0.7 or task.get("requires_specialist", False)


def delegate_to(agent_name: str, task: dict) -> dict:
    """
    Simulate handing off the task to another agent.

    Args:
        agent_name (str): The name of the target agent.
        task (dict): Task data to transfer.

    Returns:
        dict: Simulated result from delegated agent.
    """
    return {
        "agent": agent_name,
        "status": "delegated",
        "result": f"{agent_name} accepted task: {task.get('type')}"
    }
