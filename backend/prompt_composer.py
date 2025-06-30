\"\"\"
prompt_composer.py – Dynamically assembles prompts for agent use
based on task type, user input, memory state, and system config.
\"\"\"

from shared.prompt_utils import format_prompt
from backend.context_scope_analyzer import ContextScopeAnalyzer
from backend.memory_engine import MemoryEngine
from backend.prompt_strategy_manager import PromptStrategyManager

class PromptComposer:
    def __init__(self):
        self.scope_analyzer = ContextScopeAnalyzer()
        self.memory_engine = MemoryEngine()
        self.strategy_manager = PromptStrategyManager()

    def compose(self, user_input: str, session_id: str) -> str:
        scope = self.scope_analyzer.analyze(user_input)
        memory_snippets = self.memory_engine.fetch_relevant(session_id, scope)
        strategy = self.strategy_manager.select_strategy(scope)
        prompt = format_prompt(user_input, memory_snippets, strategy)
        return prompt
