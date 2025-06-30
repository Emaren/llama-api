\"\"\"
config_manager.py – Centralized manager for loading and accessing system config.
Pulls from shared config loader and caches for runtime use.
\"\"\"

from shared.config_loader import load_all_configs

class ConfigManager:
    def __init__(self):
        self.config = {}

    def load_config(self):
        print("[ConfigManager] Loading system config...")
        self.config = load_all_configs()
        return self.config

    def get(self, key: str, default=None):
        return self.config.get(key, default)
