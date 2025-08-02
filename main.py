from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chain import rag_chain
from app.model import QueryRequest
from app.llm import get_llm

app = FastAPI(title="RAG Backend for Islamic Law Assistant")

@app.get("/")
def read_root():
    return {"message": "RAG Backend is running. Use the /ask endpoint to query the system."}

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        response = rag_chain.invoke(request.question)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}