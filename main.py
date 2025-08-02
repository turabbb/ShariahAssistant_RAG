from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_chain import rag_chain
from app.model import QueryRequest
from app.llm import get_llm

# Initialize FastAPI app
app = FastAPI(title="RAG Backend for Islamic Law Assistant")

# Test endpoint to ensure the app is running
@app.get("/")
def read_root():
    return {"message": "RAG Backend is running. Use the /ask endpoint to query the system."}

# Endpoint for RAG queries
@app.post("/ask")
async def ask_question(request: QueryRequest):
    """
    Takes a user question and returns a RAG-generated response.
    """
    try:
        response = rag_chain.invoke(request.question)
        return {"answer": response}
    except Exception as e:
        return {"error": str(e)}

# Optional: Endpoint to check LLM and vector store status
@app.get("/status")
async def get_status():
    try:
        get_llm()
        rag_chain.invoke("test")
        return {"status": "ok", "message": "Backend is fully operational."}
    except Exception as e:
        return {"status": "error", "message": f"Initialization failed: {str(e)}"}