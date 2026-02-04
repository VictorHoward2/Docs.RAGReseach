from rag.loader import load_documents
from rag.chunker import *
from rag.embedder import embed_texts
from rag.vector_store import SimpleVectorStore
from rag.prompt import build_rag_prompt
from rag.llm import call_llm

docs = load_documents("./data/company_policy_files")

store = SimpleVectorStore()
print("-----------------------------------------------------------------")
print("Bài 1")
for d in docs:
    # print("Indexing document:", d["source"])
    chunks = chunk_text(d["text"], chunk_size=300)
    # print("Number of chunks:", len(chunks))
    # print("Sample chunk:", chunks[0])
    embeddings = embed_texts(chunks)
    # print("Sample embedding:", embeddings[0][:5])  # Print first 5 dimensions of the embedding
    for c, e in zip(chunks, embeddings):
        store.add(e, c, {"source": d["source"]})
    # print("--------------------")

# print("Indexing completed.")
# print("--------------------")
# print("--------------------")
# print("Total documents in store:", len(store.texts))
# print("Vector dimension:", len(store.embeddings[0]))
# print("Sample vector:", store.embeddings[0][:5])  # Print first 5 dimensions of the first vector
# print("--------------------")
# print("--------------------")


question = "Nhân viên có được làm việc từ xa không?"
print("Question:", question)
query_emb = embed_texts([question])[0]
# print("Query embedding sample:", query_emb[:5])  # Print first 5 dimensions of the query embedding
# print("--------------------")
# print("--------------------")

results = store.search(query_emb, top_k=3)
print("Top 3 retrieved contexts:")
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
print("-----------------------------------------------------------------")
print("Bài 2")
print("Câu hỏi:", question)
print("Trả lời từ LLM thuần túy:")
print(call_llm("Nhân viên có được làm việc từ xa không?"))
print("-----------------------------------------------------------------")
print("Bài 3")
print("Chunk size hiện tại:", 300)
print("Trả lời với chunk size hiện tại:")
print(answer)
print("------------")
print("Thử nghiệm với các chunk size khác nhau:")
for new_chunk_size in [100, 500]:
    print(f"Thay đổi chunk size thành: {new_chunk_size}")
    store = SimpleVectorStore()
    for d in docs:
        chunks = chunk_text(d["text"], chunk_size=new_chunk_size)
        embeddings = embed_texts(chunks)
        for c, e in zip(chunks, embeddings):
            store.add(e, c, {"source": d["source"]})
    query_emb = embed_texts([question])[0]
    results = store.search(query_emb, top_k=3)
    contexts = [r[0] for r in results]
    prompt = build_rag_prompt(question, contexts)
    print("Prompt RAG với chunk size mới:")
    print(prompt)
    answer = call_llm(prompt)
    print(f"Trả lời với chunk size {new_chunk_size}:")
    print(answer)
    print("------------")
print("-----------------------------------------------------------------")


