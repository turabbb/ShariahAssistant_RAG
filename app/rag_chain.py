from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
# Corrected import statement
from app.llm import get_llm
from app.vectorstore import get_retriever
from app.prompt import prompt

# Build the RAG chain using LCEL
llm = get_llm()
retriever = get_retriever()

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)