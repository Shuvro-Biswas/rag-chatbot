import psycopg2
import numpy as np
from app.config import DB_CONFIG  

def insert_chunk(chunk: str, embedding: np.ndarray):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    
    embedding_list = embedding.flatten().tolist()
    
    cur.execute(
        "INSERT INTO documents (chunk, embedding) VALUES (%s, %s)",
        (chunk, embedding_list)
    )
    
    conn.commit()
    cur.close()
    conn.close()
