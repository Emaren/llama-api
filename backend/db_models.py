"""
db_models.py – Defines basic data models for memory, session, and feedback tracking.
Currently operates in-memory, but structured for future DB migration.
"""

import uuid
from sqlalchemy import Column, String, Text, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MemoryEntry(Base):
    __tablename__ = 'memory_entries'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(String, index=True, nullable=False)
    agent_name = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=False)
    score = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
