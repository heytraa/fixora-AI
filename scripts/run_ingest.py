import sys
import os
import time
from pathlib import Path

# biar bisa import dari folder src/ meski dijalankan dari scripts/
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.knowledge_base.ingestion import init_collection, ingest_knowledge_base

if __name__ == "__main__":
    init_collection(reset=True)

    markdown_files = list(Path("data").glob("*.md"))

    for i, file_path in enumerate(markdown_files):
        ingest_knowledge_base(str(file_path))
        
        if i < len(markdown_files) - 1:
            time.sleep(60)

    print("\nSemua file markdown selesai dimasukkan ke Qdrant.")