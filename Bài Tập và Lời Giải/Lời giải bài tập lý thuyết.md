### Bài 1: Phân biệt LLM thuần và RAG

#### 1. Nếu **chỉ dùng LLM thuần (không RAG)**, chatbot có những rủi ro gì?

* ❌ **Bịa nội dung (hallucination)**
  → LLM có thể *tự suy đoán* nội quy công ty dựa trên dữ liệu chung, dù nội quy đó **không tồn tại** trong PDF.

* ❌ **Không cập nhật nội dung nội bộ**
  → Nội quy công ty là tài liệu **riêng, mới, nội bộ** → LLM **không được huấn luyện sẵn**.

* ❌ **Trả lời mơ hồ, chung chung**
  → Ví dụ: thay vì trích điều khoản cụ thể, LLM trả lời kiểu “thông thường các công ty sẽ…”.

* ❌ **Không kiểm chứng được nguồn**
  → Không biết câu trả lời dựa vào **điều nào, trang nào** trong PDF.

* ❌ **Rủi ro pháp lý / vận hành**
  → Trả lời sai nội quy có thể dẫn đến hiểu sai quy định, vi phạm chính sách công ty.

#### 2. Nếu dùng **RAG (Retrieval-Augmented Generation)**, vấn đề nào được giải quyết?

* ✅ **Trả lời dựa trên đúng tài liệu PDF nội bộ**
  → LLM chỉ trả lời sau khi đã *truy xuất đoạn liên quan* trong nội quy công ty.

* ✅ **Giảm mạnh hallucination**
  → Không “bịa”, vì thông tin được *neo vào dữ liệu thật*.

* ✅ **Cập nhật dễ dàng**
  → Chỉ cần thay PDF → không cần huấn luyện lại LLM.

* ✅ **Có thể trích dẫn, kiểm chứng**
  → Biết câu trả lời đến từ **mục/điều cụ thể** trong nội quy.

* ✅ **Phù hợp cho dữ liệu private / enterprise**
  → Giải quyết đúng bài toán: *LLM không biết nội bộ, RAG bổ sung trí nhớ ngoài*.

---

Dưới đây là **lời giải – tập trung vào tiêu chí “có cần tri thức ngoài LLM hay không”** 👇

---

### Bài 2: Nhận diện bài toán có cần RAG hay không

1. **Chatbot trả lời về luật nội bộ công ty** → ✔ **CẦN RAG**

   * Luật nội bộ là **dữ liệu riêng, không có trong dữ liệu huấn luyện** của LLM
   * Cần trả lời **đúng điều khoản, không được suy đoán**

2. **Viết thơ tình lãng mạn** → ✘ **KHÔNG cần RAG**

   * Bài toán **sáng tạo**, không phụ thuộc dữ liệu cụ thể
   * LLM thuần đã làm rất tốt

3. **Hỏi đáp tài liệu kỹ thuật nội bộ** → ✔ **CẦN RAG**

   * Tài liệu kỹ thuật thường **dài, chi tiết, riêng của tổ chức**
   * Cần truy xuất đúng phần liên quan trước khi trả lời

4. **Viết slogan marketing sáng tạo** → ✘ **KHÔNG cần RAG**

   * Mục tiêu là **ý tưởng & ngôn ngữ**, không phải độ chính xác dữ liệu
   * RAG không mang lại giá trị rõ ràng

---

### Bài 3: Chọn chiến lược chunking

#### 1. Vì sao **không thể đưa cả file PDF 50 trang vào LLM**?

* ❌ **Vượt giới hạn context window**
  → LLM có giới hạn số token đầu vào; 50 trang PDF thường **vượt xa khả năng chứa**.

* ❌ **Tốn chi phí và chậm**
  → Đưa toàn bộ tài liệu vào mỗi câu hỏi là **rất tốn token**, không thực tế.

* ❌ **Giảm chất lượng trả lời**
  → Quá nhiều thông tin → LLM **khó tập trung vào phần liên quan**, dễ trả lời lan man.

* ❌ **Không tối ưu cho truy xuất**
  → LLM không có cơ chế “tìm đúng đoạn” nếu không chia nhỏ tài liệu.

#### 2. Chọn **chunk size** bao nhiêu token? Có **overlap** không? Vì sao?

* ✅ **Chunk size đề xuất:** khoảng **300–500 token**

  * Đủ dài để **giữ trọn một ý / một mục hướng dẫn**
  * Không quá dài để mất độ chính xác khi truy xuất

* ✅ **Có overlap:** khoảng **50–100 token**

  * Tránh mất ngữ cảnh khi nội dung quan trọng nằm **ở ranh giới giữa 2 chunk**
  * Giúp câu trả lời đầy đủ hơn (ví dụ: định nghĩa ở cuối chunk trước, ví dụ ở đầu chunk sau)

* ❌ **Không nên chunk quá nhỏ**
  → Mất mạch nội dung, trả lời rời rạc

* ❌ **Không nên chunk quá lớn**
  → Giảm hiệu quả embedding và retrieval

---

### Bài 4: Nhận diện chunk tốt và chunk kém

#### 🔹 A. Cắt đúng 500 token, không quan tâm ngữ nghĩa

* ❌ **Chunk có thể bị cắt giữa chừng một ý**
* ❌ **Mất ngữ cảnh logic** (định nghĩa ở chunk này, ví dụ ở chunk khác)
* ❌ **Embedding kém chất lượng** vì nội dung lộn xộn
* ❌ Khi retrieve, LLM nhận được đoạn **không trọn vẹn để trả lời**

👉 Cách này **đơn giản về kỹ thuật nhưng kém về chất lượng**


#### 🔹 B. Chia theo từng mục / heading của tài liệu

* ✅ **Mỗi chunk tương ứng một ý hoàn chỉnh**
* ✅ **Giữ được ngữ cảnh và logic nội dung**
* ✅ **Embedding mang ý nghĩa rõ ràng**
* ✅ Retrieval trả về **đúng đoạn cần đọc**, giúp LLM trả lời chính xác hơn

👉 Đây là **chunk “có nghĩa” (semantic chunk)**

---

### Bài 5: Hiểu embedding qua ví dụ

#### Đoạn được ưu tiên: **A. "Hướng dẫn đổi password tài khoản"** ✔

#### Giải thích vì sao **A > B**

* 🔍 **Ngữ nghĩa gần với câu hỏi**

  * *reset mật khẩu* ≈ *đổi password*
  * *hệ thống / tài khoản* → cùng một hành động kỹ thuật

* 🧠 **Embedding mã hóa ý nghĩa, không chỉ từ khóa**

  * Dù không có đúng chữ “reset”
  * Nhưng **hành động + mục tiêu** là giống nhau

* 📈 **Vector embedding của A gần câu hỏi hơn**

  * Cùng nói về **thao tác thay đổi mật khẩu**
  * Nằm cùng “không gian ngữ nghĩa”


### Vì sao **B không được ưu tiên** ❌

* "Quy định bảo mật thông tin":

  * Mang tính **chính sách / nguyên tắc**
  * Không trả lời **cách làm cụ thể**
* Ngữ nghĩa **xa hành động “reset”**

  * Dù có chữ *bảo mật* liên quan mơ hồ

---

### Bài 6 : Top-K quá nhiều hay quá ít?

### 1. Nguyên nhân vì sao **Top-K = 20** khiến câu trả lời bị lan man?

* ❌ **Quá nhiều chunk được đưa vào context**

  * Không phải 20 chunk đều liên quan chặt chẽ
  * LLM phải “đọc” quá nhiều thông tin

* ❌ **Nhiễu ngữ nghĩa (semantic noise)**

  * Một số chunk chỉ *hơi liên quan*
  * Nhưng vẫn chiếm chỗ trong context

* ❌ **LLM mất trọng tâm**

  * Không biết đoạn nào là “quan trọng nhất”
  * Dẫn đến tổng hợp câu trả lời dàn trải

* ❌ **Context dilution**

  * Thông tin đúng bị “pha loãng” bởi thông tin ít liên quan

### 2. Bạn sẽ điều chỉnh tham số nào?

* 🔧 **Giảm Top-K**

  * Ví dụ: từ **20 → 5 hoặc 3**
  * Chỉ giữ những chunk **liên quan nhất**

* 🔧 *(Tuỳ chọn nâng cao)* **Áp dụng score threshold**

  * Chỉ lấy chunk có similarity > ngưỡng nhất định
  * Tránh kéo vào những đoạn “na ná”

* 🔧 *(Nếu vẫn cần nhiều thông tin)* **Re-ranking**

  * Lấy Top-K lớn trước (ví dụ 20)
  * Sau đó **re-rank → chọn Top-N nhỏ hơn**

---

### Bài 7: Viết prompt cho RAG an toàn

#### Prompt đề xuất

> Bạn là trợ lý AI trả lời câu hỏi **chỉ dựa trên phần CONTEXT được cung cấp bên dưới**.
>
> **Quy tắc bắt buộc:**
>
> * Chỉ sử dụng thông tin có trong CONTEXT
> * Không suy đoán, không dùng kiến thức bên ngoài
> * Nếu CONTEXT **không chứa thông tin để trả lời câu hỏi**, hãy trả lời đúng một câu: **“Không tìm thấy thông tin.”**
>
> **CONTEXT:**
> {{context}}
>
> **CÂU HỎI:**
> {{question}}

---

### Bài 8: Nhận diện prompt RAG kém

#### Prompt có vấn đề gì?

> **“Dựa vào tài liệu trên *và kiến thức của bạn*…”**

👉 Cụm **“và kiến thức của bạn”** là điểm nguy hiểm nhất.


#### Các rủi ro cụ thể

* ❌ **Cho phép LLM dùng kiến thức ngoài context**

  * LLM sẽ trộn **tài liệu + kiến thức huấn luyện**
  * Mất đúng bản chất “answer grounded on data”

* ❌ **Mở cửa cho hallucination**

  * Khi tài liệu thiếu thông tin → LLM **tự bù bằng suy đoán**

* ❌ **Không phân biệt được đâu là thông tin từ tài liệu**

  * Câu trả lời nghe “hợp lý” nhưng **không kiểm chứng được**

* ❌ **RAG trở thành LLM thuần trá hình**

  * Retrieval có cũng như không
  * Không đảm bảo độ chính xác cho dữ liệu nội bộ

---

### Bài 9: Khi nào cần re-ranking?

#### 1. **Re-ranking giúp gì?**

* 🔍 **Sắp xếp lại mức độ liên quan của các chunk**

  * Đưa **3 đoạn thật sự liên quan** lên trên
  * Đẩy các đoạn “na ná” xuống dưới hoặc loại bỏ

* 🎯 **Tăng precision cho context**

  * LLM đọc **ít nhưng đúng**
  * Giảm nhiễu, giảm câu trả lời lan man

* 🧠 **Hiểu sâu hơn mối quan hệ question–context**

  * Re-ranker (thường là cross-encoder) xét **câu hỏi + từng đoạn**
  * Chính xác hơn embedding similarity thuần

* 🚫 **Giảm hallucination gián tiếp**

  * Ít context sai → ít cơ hội LLM suy đoán


#### 2. **Re-ranking nằm ở bước nào trong pipeline?**

👉 **Sau retrieval, trước khi đưa context vào LLM**

Pipeline chuẩn:

```
User Question
      ↓
Embedding Search (Top-K lớn)
      ↓
Re-ranking (chọn Top-N nhỏ hơn, đúng nhất)
      ↓
LLM Answer Generation
```

---

### Bài 10: Multi-query cho câu hỏi mơ hồ

Câu gốc: **“Chính sách nghỉ phép”** → quá ngắn, không rõ người dùng muốn *khía cạnh nào*.

#### 3 câu query rõ nghĩa hơn để truy xuất tài liệu

1. **“Quy định về số ngày nghỉ phép năm của nhân viên”**
   → Làm rõ *loại nghỉ* và *đối tượng áp dụng*

2. **“Điều kiện và thủ tục đăng ký nghỉ phép trong công ty”**
   → Nhắm vào *quy trình / cách thực hiện*

3. **“Các trường hợp nghỉ phép có hưởng lương và không hưởng lương”**
   → Nhắm vào *quyền lợi và phân loại*


#### Vì sao multi-query hiệu quả? 🧠

* 🔍 Bao phủ **nhiều intent hợp lý** của cùng một câu hỏi
* 📈 Tăng **recall** khi truy xuất
* 🤖 Giúp RAG không phụ thuộc vào **một cách diễn đạt duy nhất**


#### Prompt đề xuất

```
Bạn là hệ thống hỗ trợ truy xuất tài liệu cho RAG.

Nhiệm vụ của bạn là:
- Phân tích câu hỏi của người dùng
- Sinh ra 3–5 câu truy vấn khác nhau, mỗi câu làm rõ một khía cạnh (intent) hợp lý của câu hỏi
- Các truy vấn phải:
  + Giữ nguyên ý định gốc
  + Rõ ràng, cụ thể
  + Phù hợp để tìm kiếm trong tài liệu nội bộ
- Không bịa thêm chủ đề mới
- Không trả lời câu hỏi

CÂU HỎI NGƯỜI DÙNG:
{{question}}

Hãy trả về danh sách các truy vấn, mỗi truy vấn trên một dòng.
```

👉 Prompt này thường đặt **trước bước retrieval**, để LLM đóng vai “query rewriter”.

#### Vì sao prompt này được đề xuất?

* 🧠 **Tách intent mơ hồ thành nhiều góc nhìn**
* 🚫 Cấm trả lời → tránh “LLM trả lời luôn”
* 🎯 Giữ truy vấn **gần tài liệu**, không bay xa

#### Khi nào **multi-query gây hại vì kéo nhiễu** 

Multi-query **không phải lúc nào cũng tốt**. Dưới đây là các trường hợp **KHÔNG nên dùng hoặc phải kiểm soát chặt**:

##### ❌ 1. Câu hỏi đã **rất cụ thể**

Ví dụ:

> “Quy trình reset mật khẩu cho tài khoản admin”

👉 Multi-query lúc này:

* Không tăng recall
* Chỉ tạo ra các query **na ná nhau**
* Kéo thêm chunk dư thừa

➡️ **Hại nhiều hơn lợi**


##### ❌ 2. Tài liệu quá rộng, nhiều chủ đề gần nhau

Ví dụ:

* Handbook công ty
* Chính sách HR tổng hợp

Multi-query có thể:

* Truy xuất **nhiều chương khác nhau**
* Context bị **loãng**, LLM khó tổng hợp

##### ❌ 3. Không có bước re-ranking phía sau

Multi-query → nhiều kết quả → nếu:

* Gộp tất cả context lại
* Không lọc / không re-rank

👉 Kết quả:

* Recall ↑ nhưng **precision ↓ mạnh**
* Câu trả lời lan man, dài dòng


##### ❌ 4. Query sinh ra bị “over-interpret”

Ví dụ câu hỏi:

> “Chính sách nghỉ phép”

LLM sinh query:

* “Nghỉ thai sản”
* “Nghỉ việc riêng”
* “Nghỉ ốm dài hạn”

👉 Nếu người dùng **chỉ hỏi nghỉ phép năm**
→ Multi-query đã **đi quá xa intent gốc**

#### Cách dùng multi-query cho đúng (best practice)

* ✅ Chỉ dùng khi **câu hỏi ngắn, mơ hồ**
* ✅ Giới hạn **3–5 query**
* ✅ Kết hợp **re-ranking**
* ✅ Hoặc **score threshold** sau retrieval


> **Multi-query tăng recall, nhưng nếu không kiểm soát sẽ phá precision.**

Hoặc nói gọn hơn:

> “Multi-query là con dao hai lưỡi: cứu câu hỏi mơ hồ, nhưng làm loãng câu hỏi rõ.”

---
