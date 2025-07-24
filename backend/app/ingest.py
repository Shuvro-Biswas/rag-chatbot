# from app.chunker import extract_text, chunk_text
# from app.embedder import get_embedding
# from app.db import insert_chunk

# def main():
#     print("Extracting and processing PDF...")
#     text = extract_text("data/hsc26_bangla.pdf")

#     print("Chunking text with tokenizer-based method...")
#     # Pass max_tokens to chunk_text if your function accepts it; default is 200 if not
#     chunks = chunk_text(text, max_len=512)  # Adjust max_len (or max_tokens) as per your chunk_text definition

#     print(f"Total chunks to embed: {len(chunks)}")

#     # Optional: print first chunk for verification
#     if chunks:
#         print(f"Sample chunk (first):\n{chunks[0]}")

#     for idx, chunk in enumerate(chunks):
#         embedding = get_embedding(chunk)
#         insert_chunk(chunk, embedding)
#         print(f"Inserted chunk {idx + 1}/{len(chunks)}")

# if __name__ == "__main__":
#     main()

from app.chunker import extract_text, chunk_text
from app.embedder import get_embedding
from app.db import insert_chunk

def main():
    print("Extracting and processing PDF...")
    text = extract_text("data/hsc26_bangla.pdf")
    
    print("Chunking text...")
    chunks = chunk_text(text)

    print(f" Total chunks to embed: {len(chunks)}")

    for idx, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        insert_chunk(chunk, embedding)
        print(f" Inserted chunk {idx+1}/{len(chunks)}")

if __name__ == "__main__":
    main()