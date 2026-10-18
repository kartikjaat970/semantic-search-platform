from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Index, Integer, Text

from database import Base

EMBEDDING_DIM = 384  # output size of all-MiniLM-L6-v2


class Document(Base):
    """One chunk of an uploaded document and its embedding."""

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    embedding = Column(Vector(EMBEDDING_DIM), nullable=False)

    __table_args__ = (
        # Approximate nearest-neighbour index for cosine distance.
        Index(
            "documents_embedding_hnsw_idx",
            "embedding",
            postgresql_using="hnsw",
            postgresql_with={"m": 16, "ef_construction": 64},
            postgresql_ops={"embedding": "vector_cosine_ops"},
        ),
    )
