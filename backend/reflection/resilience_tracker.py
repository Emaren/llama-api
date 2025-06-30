resilience_log = []


def log_recovery(event_type: str, duration_sec: float, recovered: bool):
    """
    Record a recovery attempt and its outcome.

    Args:
        event_type (str): Type of failure or interruption.
        duration_sec (float): Time taken to recover.
        recovered (bool): Whether the system successfully resumed.
    """
    resilience_log.append({
        "event": event_type,
        "duration": duration_sec,
        "success": recovered
    })


def recovery_rate() -> float:
    """
    Calculate percentage of successful recoveries.

    Returns:
        float: Success rate (0.0 to 1.0)
    """
    if not resilience_log:
        return 1.0
    successes = sum(1 for r in resilience_log if r["success"])
    return successes / len(resilience_log)
