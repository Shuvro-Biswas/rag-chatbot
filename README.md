RAG/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── chunker.py          #(extract_text, chunk_text) 
│   │   ├── embedder.py         # (get_embedding)
│   │   ├── db.py               # (insert_chunk)
│   │   ├── generator.py        # (generate_answer)
│   │   ├── retriever.py        # (search_similar_chunks)
│   │   └── config.py           # (DB_CONFIG)
│   ├── init_index.py           # (chunk + embed + insert logic)
│   ├── main.py                 # (FastAPI app)
│   └── .env
│
├── data/
│   └── hsc26_bangla.pdf
│
├── evaluation/
│   └── evaluation.md
│
├── rag-frontend/
│   └── (React App)
│
├── requirements.txt
├── README.md
└── .gitignore

## Tools and Libraries 
| Library/Tool               | Purpose                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `fitz (PyMuPDF)`           | Extract text from PDF documents                             |
| `re`                       | Regex for cleaning and chunking text                        |
| `psycopg2`                 | Interact with PostgreSQL database (store text & embeddings) |
| `numpy`                    | Numerical operations for embeddings                         |
| `sentence-transformers`    | Generate dense semantic embeddings (multilingual)           |
| `dotenv`                   | Load environment variables securely from `.env`             |
| `os`                       | Access environment and system-level operations              |
| `requests`                 | Make HTTP requests (e.g., to Groq API)                      |
| `fastapi`                  | Build API endpoints                                         |
| `sklearn.metrics.pairwise` | Cosine similarity between query and document vectors        |
| `uvicorn`                  | ASGI server to serve the FastAPI backend                    |
| `CORS Middleware`          | Allow secure communication with frontend (React)            |


## Models
| Name                                   | Use                                           |
| -------------------------------------- | --------------------------------------------- |
| `distiluse-base-multilingual-cased-v1` | Embedding model from `sentence-transformers`  |
| `LLaMA-3 70B via Groq API`             | Language model to generate human-like answers |



## 🔧 Project Setup Guide

### Backend (Python + FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


## Put your PDF in 
/data/ folder.
## env
Configure .env:GROQ_API_KEY=your_groq_key

## Set DB config in config.py:

DB_CONFIG = {
  "host": "localhost",
  "port": 5432,
  "database": "ragdb",
  "user": "postgres",
  "password": "1234"}
Initialize DB (PostgreSQL):


CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    chunk TEXT,
    embedding FLOAT8[]
);

## Run Ingester: (backend directory)
python -m app.ingest //cd backend

## Start API Server:
uvicorn main:app --reload (backend directory)

##Frontend (React)
cd rag-frontend
npm install axios bootstrap
npm start


##API Documentation (FastAPI)
Endpoint	Method	Description
/query	POST	Accepts a user query, returns top relevant responses

✅ Answers to Required Questions
 ## 1. What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?
Library Used: PyMuPDF (fitz)
Why: Fast and reliable for extracting structured text from PDFs.
Challenges: Yes, PDF layout had inconsistent newlines and white spaces. I cleaned it using regex and double-newline paragraph splitting to preserve paragraph integrity.

## 2. What chunking strategy did you choose? Why do you think it works well for semantic retrieval?
Strategy: Paragraph-based chunking with a character limit (max_len=1000)
Why: Preserves semantic units. Paragraphs typically contain self-contained ideas which makes them suitable for retrieval tasks using embeddings.

##3. What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
Model: distiluse-base-multilingual-cased-v1 from sentence-transformers
Why: It's lightweight, supports Bangla and English, and provides sentence-level embeddings good for multilingual tasks. It captures semantic meaning using context-aware transformer-based architecture.


##4. How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?
Similarity Method: cosine_similarity using sklearn
Why: It's a standard for comparing vector distances when magnitude doesn't matter.
Storage: PostgreSQL to store chunk and embedding[]. It's simple and reliable for prototyping.

##5. How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?
Ensured by: Using multilingual sentence embeddings and cosine similarity to match contextually similar chunks.

If query is vague: The model might fetch less relevant chunks, leading to generic or incorrect answers. It’s best to log similarity scores and fallback to "Insufficient context" if all scores are low.

