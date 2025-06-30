\"\"\"
identity_resolver.py – Resolves user identity by linking aliases, fingerprints,
and session metadata for continuity and personalization.
\"\"\"

import hashlib
from shared.utils import normalize_name

class IdentityResolver:
    def __init__(self):
        self.alias_map = {}

    def resolve(self, user_input: str, metadata: dict):
        alias = normalize_name(metadata.get("username", ""))
        fingerprint = self._generate_fingerprint(user_input, metadata)

        if alias not in self.alias_map:
            self.alias_map[alias] = fingerprint
            print(f"[IdentityResolver] New identity mapped: {alias}")

        return {
            "alias": alias,
            "fingerprint": fingerprint,
            "resolved": alias in self.alias_map
        }

    def _generate_fingerprint(self, text: str, metadata: dict) -> str:
        base = text + str(metadata)
        return hashlib.sha256(base.encode()).hexdigest()
