\"\"\"
module_dispatcher.py – Maps incoming tasks to backend modules using query type, context scope,
and system state. Central routing logic for LLM-based agents.
\"\"\"

from backend.query_classifier import QueryClassifier
from backend.query_router import QueryRouter

class ModuleDispatcher:
    def __init__(self):
        self.classifier = QueryClassifier()
        self.router = QueryRouter()

    def route(self, user_input: str, context_scope: str):
        query_type = self.classifier.classify(user_input)
        module = self.router.get_module(query_type, context_scope)
        return {
            "module": module,
            "query_type": query_type,
            "input": user_input,
            "context": context_scope
        }
