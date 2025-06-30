\"\"\"
input_validator.py – Validates and normalizes user input.
Handles cleaning, profanity filtering, and formatting corrections.
\"\"\"

import re

class InputValidator:
    def __init__(self, profanity_list=None):
        self.profanity_list = profanity_list or ["damn", "hell", "crap"]

    def clean_input(self, user_input: str) -> str:
        cleaned = user_input.strip()
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned

    def contains_profanity(self, user_input: str) -> bool:
        lowered = user_input.lower()
        return any(bad_word in lowered for bad_word in self.profanity_list)

    def validate(self, user_input: str) -> str:
        cleaned = self.clean_input(user_input)
        if self.contains_profanity(cleaned):
            print("[InputValidator] Profanity detected.")
        return cleaned
