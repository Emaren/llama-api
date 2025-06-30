def validate_edit(plan: dict) -> bool:
    """
    Basic sanity checks to ensure the edit plan is valid.

    Args:
        plan (dict): The plan dict with files to edit/create.

    Returns:
        bool: True if plan passes basic validation, False otherwise.
    """
    files = plan.get("files_to_edit", [])
    if not files:
        print("Validation failed: No files to edit.")
        return False
    for file_edit in files:
        if "path" not in file_edit or "content" not in file_edit:
            print(f"Validation failed: Missing path or content in {file_edit}")
            return False
    return True
