from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("distiluse-base-multilingual-cased-v1")

def get_embedding(text: str) -> np.ndarray:
    return model.encode([text])[0]
