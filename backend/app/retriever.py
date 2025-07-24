from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import psycopg2
from app.config import DB_CONFIG
from app.embedder import get_embedding

def search_similar_chunks(query: str, top_k=3):
    query_vec = get_embedding(query)
    
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT chunk, embedding FROM documents")
    rows = cur.fetchall()
    
    chunks, vectors = zip(*[(r[0], np.array(r[1])) for r in rows])
    similarities = cosine_similarity([query_vec], vectors)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    return [chunks[i] for i in top_indices]
