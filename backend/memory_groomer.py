\"\"\"
memory_groomer.py – Responsible for structural cleanup and grooming of memory traces
to maintain consistency, formatting, and efficiency before or after storage.
\"\"\"

from shared.memory_types import MemoryTrace

class MemoryGroomer:
    def groom(self, traces: list[MemoryTrace]) -> list[MemoryTrace]:
        groomed = []
        for trace in traces:
            trace.content = trace.content.strip()
            trace.metadata['cleaned'] = True
            groomed.append(trace)
        print(f"[MemoryGroomer] Groomed {len(groomed)} traces")
        return groomed
