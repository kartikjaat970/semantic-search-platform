from functools import lru_cache

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def get_model() -> SentenceTransformer:
    """Load the model on first use, then reuse it."""
    return SentenceTransformer(MODEL_NAME)


def embed(text):
    """Embed a string or a list of strings.

    A single string returns one vector (list[float]); a list of strings
    returns a list of vectors. Vectors are normalized, so cosine similarity
    equals the dot product.
    """
    return get_model().encode(text, normalize_embeddings=True).tolist()
