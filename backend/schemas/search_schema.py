from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    text: str = Field(min_length=1, max_length=2_000)
    top_k: int = Field(default=5, ge=1, le=20)


class SearchResult(BaseModel):
    text: str
    score: float  # cosine similarity, higher is more similar
