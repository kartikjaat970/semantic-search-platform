from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.document import Document
from schemas.upload_schema import Upload
from services.chunk_service import split_text
from services.embedding_service import embed

router = APIRouter()


@router.post("/upload")
def upload(data: Upload, db: Session = Depends(get_db)):
    chunks = split_text(data.text)
    if not chunks:
        raise HTTPException(status_code=422, detail="Text is empty")

    # Embed all chunks in one batch, which is much faster than one by one.
    vectors = embed(chunks)

    db.add_all(
        Document(text=chunk, embedding=vector)
        for chunk, vector in zip(chunks, vectors)
    )
    db.commit()

    return {"status": "indexed", "chunks": len(chunks)}
