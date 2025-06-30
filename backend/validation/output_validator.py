def is_valid_output(text: str) -> bool:
    """
    Check whether the output is non-empty and doesn't contain known invalid patterns.

    Args:
        text (str): Output text to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not text.strip():
        return False
    if "ERROR" in text or "undefined" in text:
        return False
    return True
