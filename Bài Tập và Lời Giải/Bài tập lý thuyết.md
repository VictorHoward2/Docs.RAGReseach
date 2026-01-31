# Bài tập lý thuyết RAG

## Level 1 – Nhận thức & tư duy nền tảng

### Bài 1: Phân biệt LLM thuần và RAG

**Mục tiêu:** Hiểu *vì sao* cần RAG

**Đề bài:**
Bạn có một chatbot trả lời câu hỏi về **nội quy công ty** được viết trong file PDF nội bộ.

1. Nếu chỉ dùng LLM (không RAG), chatbot có những rủi ro gì?
2. Nếu dùng RAG, vấn đề nào được giải quyết?

👉 Trả lời bằng gạch đầu dòng.

---

### Bài 2: Nhận diện bài toán có cần RAG hay không

**Mục tiêu:** Biết *khi nào nên / không nên dùng RAG*

**Đề bài:**
Đánh dấu ✔ hoặc ✘ cho các trường hợp sau:

1. Chatbot trả lời về luật nội bộ công ty
2. Viết thơ tình lãng mạn
3. Hỏi đáp tài liệu kỹ thuật nội bộ
4. Viết slogan marketing sáng tạo

Giải thích ngắn gọn lý do.

---

## Level 2 – Data & Chunking

### Bài 3: Chọn chiến lược chunking

**Mục tiêu:** Hiểu vai trò của chunking

**Đề bài:**
Bạn có một file PDF 50 trang (sách hướng dẫn sử dụng phần mềm).

1. Vì sao không thể đưa cả file vào LLM?
2. Bạn chọn chunk size bao nhiêu token? Có overlap hay không? Vì sao?

---

### Bài 4: Nhận diện chunk tốt và chunk kém

**Mục tiêu:** Biết thế nào là chunk "có nghĩa"

**Đề bài:**
So sánh 2 cách chunk:

* A. Cắt đúng 500 token, không quan tâm ngữ nghĩa
* B. Chia theo từng mục / heading của tài liệu

Theo bạn cách nào tốt hơn cho RAG? Giải thích.

---

## Level 3 – Embedding & Retrieval

### Bài 5: Hiểu embedding qua ví dụ

**Mục tiêu:** Hiểu embedding là *so sánh ngữ nghĩa*, không phải keyword

**Đề bài:**
Câu hỏi: "Cách reset mật khẩu hệ thống"

Theo bạn, hệ thống embedding sẽ ưu tiên đoạn nào hơn?

* A. "Hướng dẫn đổi password tài khoản"
* B. "Quy định bảo mật thông tin"

Giải thích lý do.

---

### Bài 6: Top-K quá nhiều hay quá ít?

**Mục tiêu:** Hiểu trade-off trong retrieval

**Đề bài:**
Bạn đang dùng Top-K = 20 nhưng câu trả lời thường bị lan man.

1. Nguyên nhân có thể là gì?
2. Bạn sẽ điều chỉnh tham số nào?

---

## Level 4 – Prompt Augmentation

### Bài 7: Viết prompt cho RAG an toàn

**Mục tiêu:** Giảm hallucination

**Đề bài:**
Hãy viết một prompt yêu cầu LLM:

* Chỉ trả lời dựa trên context
* Nếu không có thông tin thì nói "Không tìm thấy"

(Chỉ cần prompt, không cần câu trả lời mẫu)

---

### Bài 8: Nhận diện prompt RAG kém

**Mục tiêu:** Hiểu prompt ảnh hưởng chất lượng

**Đề bài:**
Prompt sau có vấn đề gì?

> "Dựa vào tài liệu trên và kiến thức của bạn, hãy trả lời câu hỏi sau"

Hãy chỉ ra rủi ro.

---

## Level 5 – Advanced RAG

### Bài 9: Khi nào cần re-ranking?

**Mục tiêu:** Biết lúc nào Naive RAG không đủ

**Đề bài:**
Hệ thống RAG trả về 10 đoạn context, nhưng chỉ 3 đoạn thật sự liên quan.

1. Re-ranking giúp gì?
2. Re-ranking nằm ở bước nào trong pipeline?

---

### Bài 10: Multi-query cho câu hỏi mơ hồ

**Mục tiêu:** Hiểu query transformation

**Đề bài:**
Câu hỏi người dùng: "Chính sách nghỉ phép"

Hãy viết 3 câu query rõ nghĩa hơn để truy xuất tài liệu.

---
