from qdrant_client import QdrantClient
from config import QDRANT_URL

def get_qdrant_client() -> QdrantClient:
    return QdrantClient(url=QDRANT_URL)