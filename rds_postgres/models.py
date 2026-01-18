from __future__ import annotations

from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, DateTime, ForeignKey, ForeignKeyConstraint, String, Text, Integer, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Article(Base):
    __tablename__ = "articles"

    id = Column(String, primary_key=True)
    source = Column(String, nullable=False)
    title = Column(String, nullable=False)
    summary = Column(Text, nullable=False)
    url = Column(String, nullable=False, unique=True, index=True)
    published_at = Column(DateTime, nullable=False, index=True)
    ingested_at = Column(DateTime, nullable=False, index=True)
    text = Column(Text)


class Entity(Base):
    __tablename__ = "entities"

    type = Column(String, primary_key=True)
    name = Column(String, primary_key=True)


class ArticleEntity(Base):
    __tablename__ = "article_entities"

    article_id = Column(String, ForeignKey("articles.id"), primary_key=True)
    entity_type = Column(String, primary_key=True)
    entity_name = Column(String, primary_key=True)
    entity_count = Column(Integer, nullable=False)
    entity_in_article_title = Column(Boolean, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ["entity_type", "entity_name"],
            ["entities.type", "entities.name"],
        ),
    )


class ArticleEmbedding(Base):
    __tablename__ = "article_embeddings"

    article_id = Column(String, ForeignKey("articles.id"), primary_key=True)
    embedded_text = Column(Text)
    embedding = Column(Vector(None))
    embedding_model = Column(String, primary_key=True)


class ArticleCluster(Base):
    __tablename__ = "article_clusters"

    article_cluster_id = Column(String, primary_key=True)
    clustered_at = Column(DateTime, nullable=False, index=True)


class ArticleClusterArticle(Base):
    __tablename__ = "article_cluster_articles"

    article_cluster_id = Column(
        String, ForeignKey("article_clusters.article_cluster_id"), primary_key=True
    )
    article_id = Column(String, ForeignKey("articles.id"), primary_key=True)
