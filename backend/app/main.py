from fastapi import FastAPI, Request
from app.retriever import search_similar_chunks
from app.generator import generate_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"] for specific frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/query")
async def ask_question(data: dict):
    query = data["query"]
    relevant_chunks = search_similar_chunks(query)
    context = "\n".join(relevant_chunks[:5])  # limit context length
    # prompt = (
    #     "You are a knowledgeable assistant. Use the following context to answer the question as accurately as possible.\n\n"
    #     f"Context:\n{context}\n\n"
    #     f"Question: {query}\n\n"
    #     "Answer in the same language as the question:"
    # )
    prompt = (
    "You are an intelligent and multilingual assistant. Your job is to answer the question strictly based "
    "on the information provided in the context below.\n\n"
    "🛑 Do NOT use any outside knowledge.\n"
    "📄 Context:\n"
    f"{context}\n\n"
    "❓ Question:\n"
    f"{query}\n\n"
    "✍️ Respond in the same language as the question.\n"
    "Only use information present in the context. Be concise, accurate, and direct.\n\n"
    "💬 Answer:"
    )

    answer = generate_answer(prompt)
    return {"answer": answer}
