def enforce_sandbox_constraints(action: str, context: dict) -> bool:
    """
    Determine if an action is permitted under sandbox constraints.

    Args:
        action (str): Requested action (e.g., 'write_file', 'api_call').
        context (dict): Execution context with flags like 'sandbox_enabled'.

    Returns:
        bool: True if allowed, False if sandbox blocks the action.
    """
    blocked_actions = {"write_file", "external_api", "modify_memory"}

    if context.get("sandbox_enabled", False) and action in blocked_actions:
        return False
    return True
