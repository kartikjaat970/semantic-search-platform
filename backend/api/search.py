from fastapi import APIRouter
from pydantic import BaseModel
from database import SessionLocal, Document
from embedding_service import embedding
import numpy as np
import json


router = APIRouter()


class Query(BaseModel):
	text: str


def cosine(a, b):
	a = np.array(a)
	b = np.array(b)
	return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


@router.post("/search")
def search(query: Query):
	db = SessionLocal()
	docs = db.query(Document).all()
	target = embedding(query.text)

	results = []
	for doc in docs:
		score = cosine(target, json.loads(doc.embedding))
		results.append({
			"text": doc.text,
			"score": round(float(score), 3),
		})

	results.sort(key=lambda x: x["score"], reverse=True)
	return results[:5]