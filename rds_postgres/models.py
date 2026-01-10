from __future__ import annotations

from sqlalchemy import Column, DateTime, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    author = Column(String)
    published_at = Column(DateTime, nullable=False)
