from rag.loader import load_documents
from rag.chunker import *
from rag.embedder import embed_texts
from rag.vector_store import SimpleVectorStore
from rag.prompt import build_rag_prompt
from rag.llm import call_llm
from rag.re_rank import *

docs = load_documents("./data/company_policy")
# print(docs[0]["text"])

store = SimpleVectorStore()

# print("Indexing document:", d["source"])
chunks = chunk_by_heading(docs[0]["text"])
print("Number of chunks:", len(chunks))
print("Sample chunk:", chunks[2])
embeddings = embed_texts(chunks)
# print("Sample embedding:", embeddings[0][:5])  # Print first 5 dimensions of the embedding
for c, e in zip(chunks, embeddings):
    store.add(e, c)
# print("--------------------")

# print("Indexing completed.")
# print("--------------------")
# print("--------------------")
# print("Total documents in store:", len(store.texts))
# print("Vector dimension:", len(store.embeddings[0]))
# print("Sample vector:", store.embeddings[0][:5])  # Print first 5 dimensions of the first vector
# print("--------------------")
# print("--------------------")


question = "Nhân viên thử việc có được làm việc từ xa không?"
print("Question:", question)
query_emb = embed_texts([question])[0]
# print("Query embedding sample:", query_emb[:5])  # Print first 5 dimensions of the query embedding
# print("--------------------")
# print("--------------------")
top_k = 10
results = store.search(query_emb, top_k=10)
print(f"Top {top_k} retrieved contexts:")
contexts = [r[0] for r in results]
# print("Retrieved contexts for prompt:")
# for c in contexts:
#     print(c)
#     print("--------------------")

prompt = build_rag_prompt(question, contexts)
print("Final RAG prompt:")
print(prompt)
print("--------------------")

answer = call_llm(prompt)

print(answer)

build_rerank_prompt(question, store)