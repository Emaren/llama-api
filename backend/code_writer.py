import os

def write_code_files(plan: dict) -> (bool, str):
    """
    Execute the code editing plan by creating or modifying files.

    Args:
        plan (dict): Contains files to edit/create and their content.

    Returns:
        tuple: (success (bool), notes (str))
    """
    try:
        for file_edit in plan.get("files_to_edit", []):
            path = file_edit["path"]
            content = file_edit.get("content", "")
            action = file_edit.get("action", "edit")

            if action == "create" and os.path.exists(path):
                return False, f"File already exists: {path}"
            with open(path, "w") as f:
                f.write(content)
        return True, "All files written successfully."
    except Exception as e:
        return False, str(e)
