def reflect_on_interaction(success: bool, notes: str = "") -> dict:
    """
    Generate a simple reflection log based on interaction outcome.

    Args:
        success (bool): Whether the interaction was deemed successful.
        notes (str): Optional notes or observations.

    Returns:
        dict: Reflection metadata.
    """
    return {
        "success": success,
        "notes": notes,
        "reflection": "Success ✅" if success else "Improvement needed 🔍"
    }
