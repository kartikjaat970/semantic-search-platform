from sentence_transformers import (
SentenceTransformer
)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embedding(text):
	"""Return embedding vector (list) for the given text."""
	vector = model.encode(text, normalize_embeddings=True)
	return vector.tolist()