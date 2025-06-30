def generate_fallback_response(reason: str) -> dict:
    """
    Generate a safe, minimal fallback response when normal processing fails.

    Args:
        reason (str): A brief explanation of why fallback was triggered.

    Returns:
        dict: A default response payload.
    """
    return {
        "status": "fallback_triggered",
        "reason": reason,
        "message": "We're working on that — let's try again shortly or rephrase your request."
    }
