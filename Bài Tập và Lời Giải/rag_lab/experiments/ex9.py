from rag.loader import load_documents
from rag.chunker import *
from rag.embedder import embed_texts
from rag.vector_store import *
from rag.prompt import build_rag_prompt
from rag.llm import call_llm

docs = load_documents("./data/company_policy")
# print(docs[0]["text"])

store = SimpleVectorStore()

chunks = chunk_by_heading(docs[0]["text"])
print("Number of chunks:", len(chunks))
embeddings = embed_texts(chunks)
for c, e in zip(chunks, embeddings):
    store.add(e, c)

question = "Nhân viên thử việc có được làm việc từ xa không?"
print("Question:", question)
query_emb = embed_texts([question])[0]

top_k = 5

print("=============NO RE-RANK======================")
results = store.search(query_emb, top_k)
print(f"Top k = {top_k}")
contexts = [r[0] for r in results]

prompt = build_rag_prompt(question, contexts)
print("Final RAG prompt:")
print(prompt)

answer = call_llm(prompt=prompt)
print("Answer:")
print(answer)

print("=============RE-RANK=========================")
results = store.rerank(question, query_emb, top_k=top_k, reranker_fn=llm_pointwise_reranker)
print(f"Top k = {top_k}")
contexts = [r[0] for r in results]

prompt = build_rag_prompt(question, contexts)
print("Final RAG prompt:")
print(prompt)

print("Answer:")
answer = call_llm(prompt=prompt)
print(answer)


# Kết quả DEMO

# (base) PS D:\Docs\RAG Research\Bài Tập và Lời Giải\rag_lab> python -m experiments.ex9
# Number of chunks: 24
# Question: Nhân viên thử việc có được làm việc từ xa không?
# =============NO RE-RANK======================
# Top k = 5
# Final RAG prompt:

# Bạn chỉ được phép trả lời dựa trên CONTEXT bên dưới.
# Nếu không có thông tin, hãy trả lời: "Không tìm thấy trong tài liệu".
# Ưu tiên trả lời bằng tiếng Việt.

# CONTEXT:
# 1. ## Làm việc từ xa
# Nhân viên cần đăng ký lịch làm việc từ xa với quản lý trước ít nhất 1 ngày.     

# 2. ## Làm việc từ xa
# Lưu ý rằng một số cuộc họp quan trọng có thể yêu cầu sự hiện diện tại văn phòng.

# 3. ## Làm việc từ xa
# Trong thời gian làm việc từ xa, nhân viên vẫn phải đảm bảo khả năng liên lạc.

# 4. ## Làm việc từ xa
# Công ty cho phép nhân viên làm việc từ xa tối đa 2 ngày mỗi tuần.

# 5. ## Bảo mật thông tin
# Làm việc từ xa yêu cầu nhân viên sử dụng các biện pháp bảo mật thích hợp để bảo vệ dữ liệu công ty.

# QUESTION:
# Nhân viên thử việc có được làm việc từ xa không?

# ANSWER:

# Answer:
# Không tìm thấy trong tài liệu.
# =============RE-RANK=========================
# Documents: ## Làm việc từ xa
# Nhân viên cần đăng ký lịch làm việc từ xa với quản lý trước ít nhất 1 ngày.
# Score: 8.0
# Documents: ## Làm việc từ xa
# Lưu ý rằng một số cuộc họp quan trọng có thể yêu cầu sự hiện diện tại văn phòng.
# Score: 4.0
# Documents: ## Làm việc từ xa
# Trong thời gian làm việc từ xa, nhân viên vẫn phải đảm bảo khả năng liên lạc.
# Score: 1.0
# Documents: ## Làm việc từ xa
# Công ty cho phép nhân viên làm việc từ xa tối đa 2 ngày mỗi tuần.
# Score: 1.0
# Documents: ## Bảo mật thông tin
# Làm việc từ xa yêu cầu nhân viên sử dụng các biện pháp bảo mật thích hợp để bảo vệ dữ liệu công ty.
# Score: 4.0
# Documents: ## Bảo mật thông tin
# Việc chia sẻ dữ liệu, tài liệu hoặc thông tin cho bên thứ ba khi chưa được phép được xem là vi phạm nghiêm trọng và có thể bị xử lý kỷ luật.
# Score: 1.0
# Documents: ## Nhân viên thử việc
# Nhân viên đang trong thời gian thử việc KHÔNG được phép làm việc từ xa, trừ khi có sự phê duyệt đặc biệt từ quản lý trực tiếp. Nếu vi phạm sẽ bị đuổi việc.
# Score: 10.0
# Documents: # Company Internal Policy
# Score: 2.0
# Documents: ## Nghỉ phép
# Ngày nghỉ phép chưa sử dụng sẽ không được chuyển sang năm sau.
# Score: 0.0
# Documents: ## Nghỉ phép
# Việc nghỉ phép cần được quản lý trực tiếp phê duyệt trước khi thực hiện.
# Score: 1.0
# Top k = 5
# Final RAG prompt:

# Bạn chỉ được phép trả lời dựa trên CONTEXT bên dưới.
# Nếu không có thông tin, hãy trả lời: "Không tìm thấy trong tài liệu".
# Ưu tiên trả lời bằng tiếng Việt.

# CONTEXT:
# 1. ## Nhân viên thử việc
# Nhân viên đang trong thời gian thử việc KHÔNG được phép làm việc từ xa, trừ khi có sự phê duyệt đặc biệt từ quản lý trực tiếp. Nếu vi phạm sẽ bị đuổi việc.

# 2. ## Làm việc từ xa
# Nhân viên cần đăng ký lịch làm việc từ xa với quản lý trước ít nhất 1 ngày.

# 3. ## Làm việc từ xa
# Lưu ý rằng một số cuộc họp quan trọng có thể yêu cầu sự hiện diện tại văn phòng.

# 4. ## Bảo mật thông tin
# Làm việc từ xa yêu cầu nhân viên sử dụng các biện pháp bảo mật thích hợp để bảo vệ dữ liệu công ty.

# 5. # Company Internal Policy

# QUESTION:
# Nhân viên thử việc có được làm việc từ xa không?

# ANSWER:
# Không. Theo quy định tại mục 1, nhân viên đang trong thời gian thử việc KHÔNG được phép làm việc từ xa, trừ khi có sự phê duyệt đặc biệt từ quản lý trực tiếp.

# Tuy nhiên, nếu nhân viên muốn làm việc từ xa, họ cần phải đăng ký lịch làm việc từ xa với quản lý trước ít nhất 1 ngày (mục 2). Nhưng điều này chỉ áp dụng cho nhân viên đã được phê duyệt làm việc từ xa, không phải là nhân viên thử việc.

# Vì vậy, câu trả lời ngắn gọn: Không.