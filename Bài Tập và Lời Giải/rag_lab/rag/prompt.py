def build_rag_prompt(question, contexts):
    context_text = "\n\n".join(contexts)
    return f"""
Bạn chỉ được phép trả lời dựa trên CONTEXT bên dưới.
Nếu không có thông tin, hãy trả lời: "Không tìm thấy trong tài liệu".
Ưu tiên trả lời bằng tiếng Việt.

CONTEXT:
{context_text}

QUESTION:
{question}

ANSWER:
"""
