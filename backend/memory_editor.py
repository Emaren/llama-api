\"\"\"
memory_editor.py – Allows manual review and correction of memory traces,
supporting annotations, deletions, or priority adjustments.
\"\"\"

from shared.memory_types import MemoryTrace

class MemoryEditor:
    def review_trace(self, trace: MemoryTrace) -> None:
        print(f"[MemoryEditor] Reviewing Trace ID: {trace.id}")
        print(f"Content: {trace.content}")
        print(f"Tags: {trace.tags}")
        print(f"Importance: {trace.importance}")

    def update_trace(self, trace: MemoryTrace, new_content: str = None, new_tags: set = None, new_importance: float = None):
        if new_content:
            trace.content = new_content
        if new_tags:
            trace.tags.update(new_tags)
        if new_importance is not None:
            trace.importance = new_importance
        print(f"[MemoryEditor] Trace ID {trace.id} updated.")

    def delete_trace(self, trace: MemoryTrace) -> None:
        trace.deleted = True
        print(f"[MemoryEditor] Trace ID {trace.id} marked as deleted.")
