# Bài tập thực hành RAG

## Level 1 – Làm quen pipeline RAG

### Thực hành 1: RAG tối giản (Hello RAG)

**Mục tiêu:** Hiểu pipeline end-to-end

**Đề bài:**

1. Chuẩn bị 3–5 đoạn văn bản ngắn (txt) về cùng một chủ đề (ví dụ: nội quy công ty)
2. Thực hiện:

   * Chunk (nếu cần)
   * Embed
   * Lưu vào vector store
3. Đặt 1 câu hỏi và trả lời bằng RAG

✅ Kết quả mong đợi: Trả lời có sử dụng đúng nội dung trong dữ liệu.

---

### Thực hành 2: So sánh LLM thuần vs RAG

**Mục tiêu:** Thấy rõ giá trị của RAG

**Đề bài:**

* Hỏi cùng 1 câu hỏi:

  * Lần 1: không dùng RAG
  * Lần 2: dùng RAG
* So sánh:

  * Độ chính xác
  * Mức độ bịa (hallucination)

---

## Level 2 – Chunking & Data Quality

### Thực hành 3: Thử nghiệm chunk size

**Mục tiêu:** Hiểu chunking ảnh hưởng retrieval

**Đề bài:**
Chạy cùng 1 bộ dữ liệu với 3 cấu hình:

* Chunk 300 tokens
* Chunk 800 tokens
* Chunk 800 tokens + overlap

So sánh chất lượng câu trả lời.

---

### Thực hành 4: Chunk xấu vs chunk tốt

**Mục tiêu:** Nhận diện lỗi data

**Đề bài:**

* Cố tình tạo chunk bị cắt giữa câu / giữa ý
* So sánh kết quả với chunk theo heading

Rút ra kết luận.

---

## Level 3 – Retrieval

### Thực hành 5: Điều chỉnh Top-K

**Mục tiêu:** Hiểu trade-off recall vs precision

**Đề bài:**
Chạy retrieval với:

* Top-K = 3
* Top-K = 5
* Top-K = 10

Quan sát sự thay đổi của câu trả lời.

---

### Thực hành 6: Thêm metadata filtering

**Mục tiêu:** Kiểm soát context

**Đề bài:**

* Gắn metadata (date / category) cho document
* Chỉ truy xuất tài liệu trong 1 khoảng điều kiện

---

## Level 4 – Prompt Augmentation

### Thực hành 7: Prompt ràng buộc nguồn

**Mục tiêu:** Giảm hallucination

**Đề bài:**
Viết prompt yêu cầu:

* Chỉ trả lời từ context
* Trích dẫn đoạn context đã dùng

---

### Thực hành 8: Test prompt xấu

**Mục tiêu:** Hiểu prompt gây lỗi thế nào

**Đề bài:**

* Dùng prompt cho phép "kết hợp kiến thức bên ngoài"
* Quan sát lỗi phát sinh

---

## Level 5 – Advanced RAG

### Thực hành 9: Re-ranking context

**Mục tiêu:** Tăng độ chính xác

**Đề bài:**

* Lấy Top-K = 10
* Re-rank và chỉ giữ lại Top-3

So sánh trước / sau re-ranking.

---

### Thực hành 10: Multi-query retrieval

**Mục tiêu:** Giải quyết câu hỏi mơ hồ

**Đề bài:**

* Sinh 3 biến thể query từ 1 câu hỏi
* Gộp kết quả retrieval

---
