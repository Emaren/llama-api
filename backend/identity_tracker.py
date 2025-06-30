\"\"\"
identity_tracker.py – Tracks identity profiles, session history, and evolving
metadata for each known user identity.
\"\"\"

from collections import defaultdict
from datetime import datetime

class IdentityTracker:
    def __init__(self):
        self.identities = defaultdict(lambda: {"sessions": [], "last_seen": None})

    def log_session(self, alias: str, session_id: str):
        self.identities[alias]["sessions"].append(session_id)
        self.identities[alias]["last_seen"] = datetime.utcnow().isoformat()
        print(f"[IdentityTracker] Logged session for {alias}: {session_id}")

    def get_profile(self, alias: str):
        return self.identities.get(alias, {"sessions": [], "last_seen": None})

    def all_profiles(self):
        return dict(self.identities)
