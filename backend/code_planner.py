def plan_code_edits(prompt: str) -> dict:
    """
    Convert a natural language prompt into a structured code editing plan.

    Args:
        prompt (str): User or system prompt describing desired change.

    Returns:
        dict: Plan outlining files to create or edit and changes needed.
    """
    # Placeholder example plan for demo
    return {
        "files_to_edit": [
            {"path": "backend/new_feature.py", "action": "create", "content": "# New feature code stub\n"}
        ],
        "summary": f"Plan generated from prompt: {prompt}"
    }
