# Semantic Search Platform

A full-stack app for searching documents by meaning instead of keywords. Text is split into chunks, converted to vector embeddings, and stored in PostgreSQL with pgvector. Natural-language queries are matched against those vectors, so results can be relevant even when they share no words with the query.

Author: Kartik Chaudhary. Feel free to use the code.

## How it works

**Indexing**

```
Text -> split into ~500-character chunks (with overlap) -> embed each chunk -> store text + vector in PostgreSQL
```

**Searching**

```
Query -> embed -> nearest chunks by cosine distance (HNSW index) -> top results with similarity scores
```

- Embedding model: `all-MiniLM-L6-v2` from Sentence Transformers (384 dimensions, normalized vectors)
- Storage: a `documents` table with a pgvector `Vector(384)` column and an HNSW index for cosine distance
- Chunks break at word boundaries and overlap slightly, so a sentence cut at a boundary still appears whole in one chunk

## Tech stack

| Layer | Tools |
| --- | --- |
| Backend | FastAPI, SQLAlchemy, psycopg2 |
| Database | PostgreSQL 16 + pgvector (`pgvector/pgvector:pg16`) |
| Embeddings | Sentence Transformers |
| Frontend | React, Axios |
| Deployment | Docker, Docker Compose |

## Project structure

```
backend/
  main.py                FastAPI app, CORS, startup (extension + tables)
  database.py            Engine, session, DATABASE_URL from environment
  models/document.py     Document model (text + Vector(384) + HNSW index)
  routes/upload.py       POST /upload
  routes/search.py       POST /search
  schemas/               Request and response models
  services/
    chunk_service.py     Word-boundary chunking with overlap
    embedding_service.py Sentence Transformers wrapper
  tests/                 Unit tests
frontend/
  src/components/        Upload, Search, Result
docker-compose.yml       db + backend + frontend
.env.example             Configuration template
```

## Getting started

### Option 1: Docker Compose

```bash
cp .env.example .env     # then edit the password
docker compose up --build
```

The first build downloads the embedding model, so it takes a few minutes.

### Option 2: Run the pieces yourself

**Prerequisites:** Docker (for the database), Python 3.10+, Node.js 18+

```bash
# Database
docker compose up -d db

# Backend (in a new terminal)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (in a new terminal)
cd frontend
npm install
npm start
```

The backend enables the pgvector extension and creates the table on startup. By default it connects to `postgresql://postgres:admin@localhost:5432/ragdb`. If you changed the password in `.env`, set `DATABASE_URL` to match.

**Open**

- Frontend: http://localhost:3000
- Backend: http://localhost:8000 (interactive API docs at `/docs`)

## API

| Method | Endpoint | Body | Response |
| --- | --- | --- | --- |
| POST | `/upload` | `{"text": "..."}` | `{"status": "indexed", "chunks": N}` |
| POST | `/search` | `{"text": "...", "top_k": 5}` | `[{"text": "...", "score": 0.82}, ...]` |

`score` is cosine similarity (higher is more similar). `top_k` is optional, defaults to 5, and can be 1 to 20.

## Tests

```bash
cd backend
pip install -r requirements-dev.txt
pytest
```

## Roadmap

- [ ] Upload files (PDF, TXT, DOCX) with text extraction and cleaning
- [ ] Group and label chunks by source document
- [ ] Hybrid search (vector + keyword) and reranking
- [ ] A small evaluation set to measure how often the right chunk is in the top results
- [ ] Authentication
