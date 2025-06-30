def is_aligned(output: str, goal_keywords: list) -> bool:
    """
    Check whether output appears aligned with user goals based on keyword overlap.

    Args:
        output (str): The agent's response.
        goal_keywords (list): List of key terms reflecting user intent.

    Returns:
        bool: True if output includes one or more goal terms.
    """
    output_lower = output.lower()
    return any(keyword.lower() in output_lower for keyword in goal_keywords)
