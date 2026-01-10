from __future__ import annotations

from uuid import uuid4

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    text_clean = Column(Text)
    text_processed = Column(Text)
    url = Column(String, nullable=False, unique=True, index=True)
    ingested_at = Column(DateTime, nullable=False, index=True)
    cleaned_at = Column(DateTime)
    processed_at = Column(DateTime)
    embedding = Column(Vector(1536))
