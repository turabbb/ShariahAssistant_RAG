import os
from dotenv import load_dotenv

load_dotenv()

VECTOR_STORE_PATH = os.path.join("db", "chroma_db")
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"