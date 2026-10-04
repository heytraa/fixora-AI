import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")

EMBEDDING_MODEL = "gemini-embedding-2"
EMBEDDING_DIMENSION = 768
LLM_MODEL = "gemini-3.5-flash-lite"

COLLECTION_NAME = "knowledge_fixora"