from fastapi import APIRouter
from pydantic import BaseModel
import json

from database import SessionLocal, Document
from embedding_service import embedding

router = APIRouter()


class Upload(BaseModel):
	text: str


@router.post("/upload")
def upload(data: Upload):
	db = SessionLocal()

	vec = embedding(data.text)

	doc = Document(
		text=data.text,
		embedding=json.dumps(vec),
	)

	db.add(doc)
	db.commit()

	return {"status": "uploaded"}