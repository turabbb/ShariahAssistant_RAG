from pydantic import BaseModel

class QueryRequest(BaseModel):
    """Pydantic model for a user's query."""
    question: str