# import re
# import fitz  # PyMuPDF
# from transformers import LlamaTokenizer

# tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")  # adjust model name as needed

# def extract_text(pdf_path: str) -> str:
    
#     doc = fitz.open(pdf_path)
#     full_text = ""
#     for page in doc:
#         text = page.get_text()
#         full_text += re.sub(r'\s+', ' ', text) + "\n"
#     return full_text

# def chunk_text(text: str, max_tokens=200):
#     # Split text into paragraphs by blank lines
#     paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', text) if p.strip()]
#     chunks = []
#     current_chunk = ""
#     current_length = 0

#     for para in paragraphs:
#         tokens = tokenizer.tokenize(para)
#         token_len = len(tokens)

#         if current_length + token_len <= max_tokens:
#             current_chunk += para + "\n\n"
#             current_length += token_len
#         else:
#             if current_chunk:
#                 chunks.append(current_chunk.strip())
#             if token_len > max_tokens:
#                 # Split large paragraph into smaller chunks by tokens
#                 for i in range(0, token_len, max_tokens):
#                     sub_tokens = tokens[i:i+max_tokens]
#                     sub_text = tokenizer.convert_tokens_to_string(sub_tokens)
#                     chunks.append(sub_text.strip())
#                 current_chunk = ""
#                 current_length = 0
#             else:
#                 current_chunk = para + "\n\n"
#                 current_length = token_len

#     if current_chunk:
#         chunks.append(current_chunk.strip())

#     return chunks



import fitz  # PyMuPDF
import re

def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        # Preserve paragraph breaks by splitting on double newlines
        paragraphs = text.split('\n\n')
        cleaned_paragraphs = []
        for para in paragraphs:
            # Remove excess whitespace inside paragraph
            cleaned = re.sub(r'\s+', ' ', para).strip()
            if cleaned:
                cleaned_paragraphs.append(cleaned)
        full_text += "\n\n".join(cleaned_paragraphs) + "\n\n"  # Reconstruct with double newlines
    return full_text

def chunk_text(text: str, max_len=1000):
    paragraphs = re.split(r'\n\s*\n+', text.strip())  # Split on multiple newlines
    chunks, current_chunk = [], ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if len(current_chunk) + len(para) < max_len:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

