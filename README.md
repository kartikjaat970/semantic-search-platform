# Semantic Search Platform

A full-stack app for searching documents by meaning instead of keywords. Text is split into chunks, converted to vector embeddings, and stored in PostgreSQL with pgvector. Natural-language queries are matched against those vectors, so results can be relevant even when they share no words with the query.

* **Author:** Kartik Chaudhary. Feel free to use the code.
* **Status:** Work in progress. Upload and indexing work. The search endpoint is being migrated to pgvector (see Roadmap).

---

## How It Works

### Indexing
Text → split into 500-character chunks → embed each chunk → store text + vector in PostgreSQL

### Searching
Query → embed → compare to stored vectors (cosine similarity) → top 5 results with scores

* **Embedding model:** `all-MiniLM-L6-v2` from Sentence Transformers (384 dimensions, normalized vectors)
* **Storage:** A `documents` table with a pgvector `Vector(384)` column

---

## Tech Stack

| Layer | Tools |
| :--- | :--- |
| **Backend** | FastAPI, SQLAlchemy, psycopg2 |
| **Database** | PostgreSQL 16 + pgvector (via the `pgvector/pgvector:pg16` Docker image) |
| **Embeddings** | Sentence Transformers |
| **Frontend** | React, Axios |

---

## Project Structure

```text
backend/
  main.py              FastAPI app and CORS setup
  database.py          SQLAlchemy engine and session
  models/document.py   Document model (text + Vector(384))
  routes/upload.py     POST /upload
  services/
    chunk_service.py   Fixed-size text chunking
    embedding_service.py  Sentence Transformers wrapper
  api/                 Earlier prototype code (being replaced)
frontend/
  src/                 React app (Upload, Search, Result components)
docker-compose.yml     PostgreSQL + pgvector
```

---

## Getting Started

### Prerequisites
Docker, Python 3.10+, Node.js 18+

### 1. Start the Database

```bash
docker compose up -d db
```

Then enable the pgvector extension once:

```bash
docker compose exec db psql -U postgres -d ragdb -c "CREATE EXTENSION IF NOT EXISTS vector;"
```

### 2. Start the Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
*Note: The first run downloads the embedding model, so it may take a minute.*

### 3. Start the Frontend

```bash
cd frontend
npm install
npm start
```

### Access Endpoints
* **Frontend:** `http://localhost:3000`
* **Backend:** `http://localhost:8000`

> ⚠️ **Warning:** The database connection string is currently set in `backend/database.py` and matches the credentials in `docker-compose.yml`. These are development defaults.

---

## API

| Method | Endpoint | Body | Response |
| :--- | :--- | :--- | :--- |
| **POST** | `/upload` | `{"text": "..."}` | `{"status": "indexed", "chunks": N}` |
| **POST** | `/search` | `{"text": "..."}` | `[{"text": "...", "score": 0.82}, ...]` (top 5) |

*Note: `/search` is not yet registered in `main.py`. See the roadmap.*

---

## Roadmap

- [ ] Register the search route and use pgvector's cosine distance operator (`<=>`) instead of comparing vectors in Python
- [ ] Add an HNSW or IVFFlat index on the embedding column
- [ ] Remove the old `api/` prototype code and merge the duplicate `database.py` files
- [ ] Add Dockerfiles for the backend and frontend so docker compose up runs the whole app
- [ ] Add `react-scripts` to `frontend/package.json`
- [ ] Support file upload (PDF, TXT, DOCX) with text extraction and cleaning
- [ ] Smarter chunking (sentence or paragraph boundaries, with overlap)
- [ ] Move database credentials and URLs into environment variables
