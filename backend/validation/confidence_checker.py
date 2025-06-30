def is_confident(score: float, threshold: float = 0.75) -> bool:
    """
    Check if a confidence score meets or exceeds the threshold.

    Args:
        score (float): Confidence score between 0.0 and 1.0.
        threshold (float): Minimum acceptable confidence.

    Returns:
        bool: True if confident enough, False if fallback or clarification needed.
    """
    return score >= threshold
