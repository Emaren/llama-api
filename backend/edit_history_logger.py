import json
import os
from datetime import datetime

HISTORY_FILE = "data/edit_history.json"

def log_edit(edit_record: dict):
    """
    Append an edit record to the edit history file.

    Args:
        edit_record (dict): Details about the edit.
    """
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        else:
            history = []
        edit_record["timestamp"] = datetime.utcnow().isoformat()
        history.append(edit_record)
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f, indent=2)
    except Exception as e:
        print(f"Failed to log edit: {e}")
