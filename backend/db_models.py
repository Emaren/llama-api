\"\"\"
db_models.py – Defines basic data models for memory, session, and feedback tracking.
Currently operates in-memory, but structured for future DB migration.
\"\"\"

from dataclasses import dataclass, field
from typing import List, Dict, Any
import datetime

@dataclass
class MemoryEntry:
    content: str
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
    importance: float = 0.5
    scope: str = "general"

@dataclass
class SessionData:
    session_id: str
    history: List[Dict[str, Any]] = field(default_factory=list)
    memories: List[MemoryEntry] = field(default_factory=list)

@dataclass
class FeedbackRecord:
    session_id: str
    input_text: str
    output_text: str
    tags: List[str]
    score: float
    timestamp: str = field(default_factory=lambda: datetime.datetime.now().isoformat())
