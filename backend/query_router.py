\"\"\"
query_router.py – Routes queries to modules based on classification and context scope.
Ensures the right processing engine handles the query type.
\"\"\"

from backend.query_classifier import QueryClassifier
from backend.prompt_composer import PromptComposer
from backend.reflection_engine import ReflectionEngine
from backend.diagnostic_reporter import DiagnosticReporter
from backend.context_engine import ContextEngine

class QueryRouter:
    def __init__(self):
        self.classifier = QueryClassifier()
        self.context_engine = ContextEngine()
        self.diagnostic = DiagnosticReporter()
        self.reflection = ReflectionEngine()
        self.composer = PromptComposer()

    def route(self, user_input: str, context_scope: str):
        query_type = self.classifier.classify(user_input)
        if query_type == "reflection":
            return self.reflection.generate(user_input)
        elif query_type == "diagnostic":
            return self.diagnostic.report(user_input)
        elif query_type == "meta":
            return self.composer.compose_meta_prompt(user_input)
        else:
            return self.context_engine.process(user_input, context_scope)
