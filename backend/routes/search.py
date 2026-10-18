from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models.document import Document
from schemas.search_schema import SearchQuery, SearchResult
from services.embedding_service import embed

router = APIRouter()


@router.post("/search", response_model=list[SearchResult])
def search(query: SearchQuery, db: Session = Depends(get_db)):
    query_vector = embed(query.text)

    # `<=>` is pgvector's cosine distance; the HNSW index serves this ordering.
    distance = Document.embedding.cosine_distance(query_vector)
    rows = db.execute(
        select(Document.text, distance.label("distance"))
        .order_by(distance)
        .limit(query.top_k)
    ).all()

    # Cosine similarity = 1 - cosine distance.
    return [
        SearchResult(text=text, score=round(1 - float(dist), 3))
        for text, dist in rows
    ]
