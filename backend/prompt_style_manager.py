\"\"\"
prompt_style_manager.py – Manages stylistic presentation of prompts, including tone,
formality, structure, and visual embellishments (e.g., emoji or markdown emphasis).
\"\"\"

from shared.style_presets import STYLE_PRESETS

class PromptStyleManager:
    def __init__(self):
        self.presets = STYLE_PRESETS

    def apply_style(self, prompt: str, style_key: str) -> str:
        style = self.presets.get(style_key, {})
        if style.get("emoji"):
            prompt = f"{style['emoji']} {prompt} {style['emoji']}"
        if style.get("uppercase"):
            prompt = prompt.upper()
        if style.get("markdown"):
            prompt = f"**{prompt}**"
        return prompt
