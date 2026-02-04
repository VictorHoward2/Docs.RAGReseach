from rag.loader import load_documents
from rag.chunker import *


print("Bài 4")

with open("company_policy.md", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_by_heading(text)

for i, c in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(c)

chunks = chunk_text(text, chunk_size=300, overlap=50)

for i, c in enumerate(chunks, 1):
    print(f"\n--- Chunk {i} ---")
    print(c)