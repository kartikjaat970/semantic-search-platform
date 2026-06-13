from fastapi import APIRouter

from schemas.upload_schema import Upload
from services.embedding_service import embed
from services.chunk_service import split_text
from database import SessionLocal, engine, Base
from models.document import Document

router = APIRouter()

Base.metadata.create_all(bind=engine)


@router.post("/upload")
def upload(data: Upload):
	db = SessionLocal()

	chunks = split_text(data.text)

	for chunk in chunks:
		vector = embed(chunk)
		db.add(Document(text=chunk, embedding=vector))

	db.commit()

	return {"status": "indexed", "chunks": len(chunks)}