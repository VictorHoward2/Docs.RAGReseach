# Training: Retrieval‑Augmented Generation (RAG)

## 1. RAG là gì?

**Retrieval‑Augmented Generation (RAG)** là một kiến trúc kết hợp giữa:

* **Retrieval (Truy xuất thông tin)**: lấy dữ liệu liên quan từ nguồn bên ngoài (documents, database, knowledge base)
* **Generation (Sinh nội dung)**: dùng mô hình ngôn ngữ lớn (LLM) để tạo câu trả lời dựa trên thông tin đã truy xuất

👉 Mục tiêu cốt lõi: **giúp LLM trả lời dựa trên dữ liệu thật, mới, và thuộc domain riêng**, thay vì chỉ dựa vào kiến thức đã học khi train.

---

## 2. Vì sao cần RAG?

### 2.1 Hạn chế của LLM thuần (Vanilla LLM)

* ❌ Kiến thức **đóng băng** tại thời điểm training
* ❌ **Hallucination**: bịa thông tin nghe rất hợp lý
* ❌ Không truy cập được dữ liệu nội bộ (PDF, DB, wiki công ty)
* ❌ Fine‑tune tốn kém, khó cập nhật liên tục

### 2.2 RAG giải quyết gì?

* ✅ Truy cập **tri thức ngoài mô hình**
* ✅ Cập nhật dữ liệu **không cần retrain**
* ✅ Giảm hallucination
* ✅ Phù hợp enterprise, dữ liệu private

> Có thể hiểu ngắn gọn:
> **LLM = bộ não**
> **RAG = trí nhớ + tra cứu tài liệu**

---

## 3. Kiến trúc tổng quát của RAG

### 3.1 Luồng xử lý cơ bản

1. User đặt câu hỏi
2. Câu hỏi được **embedding** thành vector
3. Tìm các document/vector liên quan trong Vector Database
4. Ghép (augment) nội dung truy xuất vào prompt
5. LLM sinh câu trả lời dựa trên context đó

```
User Query
   ↓
Embedding
   ↓
Vector Search
   ↓
Relevant Chunks
   ↓
Prompt + Context
   ↓
LLM Answer
```

---

## 4. Các thành phần cốt lõi của RAG

### 4.1 Data Source (Nguồn dữ liệu)

* PDF, Word, Excel
* Website, Wiki nội bộ
* Log, ticket, chat history
* Database (SQL / NoSQL)

⚠️ Dữ liệu **phải được tiền xử lý** trước khi dùng cho RAG

---

### 4.2 Document Processing (Tiền xử lý tài liệu)

#### a. Cleaning

* Xóa HTML tag
* Xóa header/footer lặp lại
* Chuẩn hóa encoding

#### b. Chunking (Chia nhỏ tài liệu)

**Vì sao phải chunk?**

* LLM có giới hạn context window
* Vector search hiệu quả hơn trên đoạn nhỏ

**Chiến lược chunk phổ biến:**

* Fixed size (500–1000 tokens)
* Overlap (ví dụ overlap 50–100 tokens)
* Semantic chunking (chia theo ngữ nghĩa)

---

### 4.3 Embedding

Embedding là quá trình biến text → vector số học (high‑dimensional vector)

* Vector gần nhau ⇒ nội dung ngữ nghĩa gần nhau

Ví dụ:

* "Giá vàng hôm nay" ≈ "Gold price now"
* Xa với "Cách nấu phở"

📌 Embedding model ≠ LLM generation model

---

### 4.4 Vector Database

Nơi lưu trữ và tìm kiếm embedding

**Chức năng chính:**

* Lưu vector + metadata
* Similarity search (cosine, dot product, L2)

**Vector DB phổ biến:**

* FAISS (local)
* Chroma
* Milvus
* Pinecone
* Weaviate

---

### 4.5 Retrieval (Truy xuất)

#### a. Similarity Search

* Top‑K vector gần nhất

#### b. Hybrid Search

* Kết hợp **keyword search (BM25)** + vector search

#### c. Filtering

* Theo metadata (date, author, category)

---

### 4.6 Prompt Augmentation

Ghép context truy xuất được vào prompt

Ví dụ cấu trúc:

```
You are an assistant...
Use ONLY the following context:

[Context 1]
[Context 2]

Question: ...
Answer:
```

👉 Prompt design ảnh hưởng rất lớn tới chất lượng RAG

---

## 5. Naive RAG (RAG cơ bản)

### 5.1 Định nghĩa

Naive RAG = Embedding → Vector Search → Prompt → LLM

### 5.2 Ưu điểm

* Dễ hiểu
* Dễ triển khai
* Phù hợp PoC, dự án nhỏ

### 5.3 Nhược điểm

* Lấy context **chưa chắc đã tốt nhất**
* Không đánh giá lại độ liên quan
* Dễ nhiễu nếu dữ liệu lớn

---

## 6. Advanced RAG (RAG nâng cao)

### 6.1 Re‑ranking

Sau khi lấy Top‑K (ví dụ K=20):

* Dùng model khác để **xếp hạng lại theo mức liên quan thực sự**
* Chọn Top‑N tốt nhất (N=5)

👉 Giảm noise, tăng precision

---

### 6.2 Query Transformation

#### a. Query Expansion

* Mở rộng câu hỏi (synonym, paraphrase)

#### b. Multi‑Query

* Tạo nhiều phiên bản câu hỏi
* Truy xuất song song

#### c. Query Rewriting

* Viết lại câu hỏi rõ ràng hơn (đặc biệt với hội thoại)

---

### 6.3 Context Compression

* Tóm tắt context trước khi đưa vào LLM
* Giữ ý chính, bỏ phần thừa

Hữu ích khi:

* Context dài
* Context window hạn chế

---

### 6.4 Modular RAG

Tách RAG thành các module độc lập:

* Retriever
* Reranker
* Generator
* Evaluator

👉 Dễ tối ưu từng phần, dễ scale

---

## 7. RAG vs Fine‑tuning

| Tiêu chí         | RAG         | Fine‑tuning       |
| ---------------- | ----------- | ----------------- |
| Cập nhật dữ liệu | Dễ          | Khó               |
| Chi phí          | Thấp        | Cao               |
| Dữ liệu private  | Rất phù hợp | Có rủi ro         |
| Hallucination    | Thấp hơn    | Có thể vẫn xảy ra |

👉 Thực tế enterprise thường **RAG + prompt engineering**, chỉ fine‑tune khi thật cần

---

## 8. Đánh giá chất lượng RAG

### 8.1 Các tiêu chí

* Context relevance
* Answer correctness
* Faithfulness (bám sát nguồn)

### 8.2 Các lỗi phổ biến

* Retriever lấy sai context
* Context đúng nhưng LLM diễn giải sai
* Prompt không ràng buộc nguồn

---

## 9. Khi nào nên dùng RAG?

✅ Chatbot hỏi đáp tài liệu
✅ Trợ lý nội bộ doanh nghiệp
✅ QA trên dữ liệu riêng
✅ Knowledge assistant

❌ Không cần RAG khi:

* Bài toán thuần sáng tạo
* Kiến thức chung, không cần dữ liệu riêng

---

## 10. Tư duy quan trọng

* RAG **không phải phép màu**
* 70% chất lượng đến từ **data + retrieval**
* LLM chỉ tốt khi context tốt

> **RAG là cách cho LLM “đọc tài liệu trước khi trả lời”, thay vì trả lời theo trí nhớ mơ hồ.**

