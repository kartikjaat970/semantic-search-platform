# Semantic Search Platform
Semantic Search Platform is a full-stack application for intelligent document retrieval using vector embeddings instead of traditional keyword matching.

Author: Kartik Chaudhary

Feel free to use the code ^ ^

The platform transforms uploaded text into high-dimensional vector representations and stores them in PostgreSQL using pgvector. Users can search using natural language and retrieve semantically similar content ranked by similarity.

## Functionality

### Document upload
Users can upload text documents for indexing. The system:
- extracts content
- cleans and preprocesses text
- splits content into chunks
- generates embeddings
- stores original text and vectors
- prepares data for retrieval-ready AI responses

### Embedding pipeline
Each document is processed using a transformer embedding model.
Pipeline: Document -> Text extraction -> Chunking -> Embedding generation -> Vector storage -> Similarity index

### Semantic search
Search uses embeddings instead of SQL LIKE or exact matching, so queries can return relevant results even without identical words.
Flow: User query -> Embedding generation -> Vector comparison -> Top-ranked results

### Dashboard
Frontend capabilities:
- Upload documents
- Search interface
- Similarity score display
- Ranked results
- API integration

## Tech stack
Backend:
- FastAPI
- PostgreSQL
- pgvector
- Sentence Transformers

AI:
- Sentence Transformers

Frontend:
- React
- Axios

Deployment:
- Docker
- Docker Compose

## Run
Option 1: Docker Compose
```bash
docker compose up
```

Option 2: Manual start
Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Frontend:
```bash
cd frontend
npm install
npm start
```

Open:
- Frontend: http://localhost:3000
- Backend: http://localhost:8000