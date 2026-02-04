import numpy as np

class SimpleVectorStore:
    def __init__(self):
        self.embeddings = []
        self.texts = []
        self.metadatas = []

    def add(self, embedding, text, metadata=None):
        self.embeddings.append(embedding)
        self.texts.append(text)
        self.metadatas.append(metadata or {})

    def search(self, query_embedding, top_k=5, filter_fn=None):
        scores = []
        for i, emb in enumerate(self.embeddings):
            if filter_fn and not filter_fn(self.metadatas[i]):
                continue
            score = np.dot(query_embedding, emb) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(emb)
            )
            scores.append((score, i))
        scores.sort(reverse=True)
        return [
            (self.texts[i], self.metadatas[i], score)
            for score, i in scores[:top_k]
        ]
    
    def build_rerank_prompt(self, question):
        prompt = f"""
    Bạn là hệ thống re-ranking cho RAG.
    Nhiệm vụ của bạn là chọn ra đoạn văn trả lời CHÍNH XÁC NHẤT cho câu hỏi.

    CÂU HỎI:
    {question}

    CÁC ĐOẠN:
    """
        for i, c in enumerate(chunks, 1):
            prompt += f"\n[{i}]\n{c}\n"

        prompt += """
    Hãy trả lời theo định dạng:
    BEST_CHUNK: <số>
    SECOND_BEST_CHUNK: <số>
    """
        return prompt
