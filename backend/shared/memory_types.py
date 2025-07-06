# backend/shared/memory_types.py

from pydantic import BaseModel

class MemoryTrace(BaseModel):
    content: str
    score: float = 1.0
