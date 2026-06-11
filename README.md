# Semantic Search Platform:
Semantic Search Platform is a full-stack application designed to perform intelligent document retrieval using vector embeddings instead of traditional keyword matching.

The platform transforms uploaded text into high-dimensional vector representations and stores them in PostgreSQL using pgvector. Users can then search using natural language and retrieve semantically similar content ranked by similarity.

## Functionality:

### Document Upload;
Users can upload text documents for indexing.

The system:
- extracts content
- cleans and preprocesses text
- generates embeddings
- stores original text and vectors

### Embedding Pipeline;
Each document is processed using a transformer embedding model.
Pipeline:
Document < Text Extraction < Embedding Generation < Vector Storage < Similarity Index

### Semantic Search;
Unlike SQL LIKE queries or exact matching:
Query: parallel gpu processing

can return: CUDA kernel optimization

->> even without identical words.

Search flow: User Query < Embedding Generation < Vector Comparison < Top Ranked Results

### Dashboard;

Frontend capabilities:
-> Upload documents
-> Search interface
-> Similarity score display
-> Ranked results
-> API integration

## Tech Stack;
Backend:
-> FastAPI
-> PostgreSQL
-> pgvector
-> Sentence Transformers

Frontend:
-> React
-> Axios

Deployment:
-> Docker
-> Docker Compose

## Run;
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
http://localhost:3000

Backend:
http://localhost:8000