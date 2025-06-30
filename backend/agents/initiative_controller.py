def evaluate_initiative_mode(user_engaged: bool, mode: str) -> bool:
    """
    Decide whether to proactively take action based on mode and user state.

    Args:
        user_engaged (bool): Whether the user is actively interacting.
        mode (str): One of 'reactive_only', 'suggestive_mode', 'proactive_mode'

    Returns:
        bool: True if the agent should initiate action.
    """
    if mode == "proactive_mode":
        return True
    if mode == "suggestive_mode":
        return user_engaged
    return False
