def run_meta_checks(confidence: float, contradiction: bool, context_stability: float) -> bool:
    """
    Perform meta-level reasoning checks before allowing final output.

    Args:
        confidence (float): Agent confidence (0.0–1.0).
        contradiction (bool): Whether a conflict was detected.
        context_stability (float): Estimate of how coherent context is (0.0–1.0).

    Returns:
        bool: True if output should proceed, False if fallback or review is needed.
    """
    if contradiction:
        return False
    if confidence < 0.65 or context_stability < 0.6:
        return False
    return True
