from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text):
	"""Encode text (str or list[str]) and return embeddings as list(s).
	"""
	embeddings = model.encode(text, normalize_embeddings=True)
	# if a single string was provided, convert to list
	try:
		return embeddings.tolist()
	except AttributeError:
		# embeddings is already a list
		return embeddings