import uuid
from qdrant_client.models import PointStruct, VectorParams, Distance

from config import COLLECTION_NAME, EMBEDDING_DIMENSION
from src.core.embeddings import get_embedder
from src.core.vector_store import get_qdrant_client
from src.core.chunking import chunk_text

def init_collection(reset: bool = False):
    client = get_qdrant_client()
    
    # Menghapus data lama
    if reset and client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)

    # Buat baru jika belum ada
    if not client.collection_exists(COLLECTION_NAME):
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=EMBEDDING_DIMENSION, 
                distance=Distance.COSINE
            ),
        )
        print(f"Collection '{COLLECTION_NAME}' berhasil dibuat.")
        
def ingest_knowledge_base(file_path: str):
    # 1. Baca dokumen
    with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
    print(f"Panjang dokumen: {len(raw_text)} karakter")

    # 2. Chunking
    chunks = chunk_text(raw_text)
    print(f"Jumlah chunks: {len(chunks)}")
    for i, c in enumerate(chunks):
        print(f"--- Chunk {i} ---\n{c}\n")

    # 3. Embedding
    embedder = get_embedder()
    vectors = embedder.embed_documents(chunks)

    # 4. Simpan ke Qdrant
    client = get_qdrant_client()

    points = [
        PointStruct(id=str(uuid.uuid4()), vector=vector, payload={"text": chunk, "source": file_path})
        for chunk, vector in zip(chunks, vectors)
    ]
    client.upsert(collection_name=COLLECTION_NAME, points=points)

    print(f"Berhasil simpan {len(points)} chunks ke collection '{COLLECTION_NAME}'")