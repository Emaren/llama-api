def route_task(task_type: str, context: dict) -> str:
    """
    Determine the responsible agent module for a given task type.

    Args:
        task_type (str): e.g., 'generation', 'evaluation'
        context (dict): Additional task context (user, priority, memory)

    Returns:
        str: Target agent module name
    """
    routing_table = {
        "generation": "agent_generator",
        "evaluation": "agent_critic",
        "retrieval": "agent_searcher",
        "planning": "agent_planner"
    }
    return routing_table.get(task_type, "agent_fallback")
