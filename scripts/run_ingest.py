import sys
import os
from pathlib import Path
from src.knowledge_base.ingestion import init_collection, ingest_knowledge_base

# biar bisa import dari folder src/ meski dijalankan dari scripts/
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

if __name__ == "__main__":
    init_collection(reset=True)

    markdown_files = list(Path("data").glob("*.md"))

    for file_path in markdown_files:
        ingest_knowledge_base(str(file_path))

    print("\nSemua file markdown selesai dimasukkan ke Qdrant.")