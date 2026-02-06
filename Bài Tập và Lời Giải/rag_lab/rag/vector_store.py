import re
import numpy as np
from rag.llm import *

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
        if not self.embeddings:
            return []
        
        emb_matrix = np.array(self.embeddings)
        q_norm = np.linalg.norm(query_embedding)
        e_norms = np.linalg.norm(emb_matrix, axis=1)

        # Tính Cosine Similarity bằng vectorization
        dot_products = np.dot(emb_matrix, query_embedding)
        scores = dot_products / (q_norm * e_norms)

        results = []
        for i, score in enumerate(scores):
            if filter_fn and not filter_fn(self.metadatas[i]):
                continue
            # Trả về cả index (i) để rerank level 1 không cần tìm kiếm lại
            results.append((self.texts[i], self.metadatas[i], score, i))
            
        results.sort(key=lambda x: x[2], reverse=True)
        return results[:top_k]
    
    
    def rerank(self, query_text, query_embedding=None, candidates=None, top_k=5, reranker_fn=None):
        """Rerank a list of candidate documents for a query.

        Parameters
        - query_embedding: numpy array embedding for the query. Required if no
          `reranker_fn` is provided or if `candidates` need to be rescored by
          embedding similarity.
        - candidates: list of tuples as returned by `search()`: (text, metadata, score).
          If None, the method will use `search()` over all items (requires
          `query_embedding`).
        - top_k: number of top results to return.
        - reranker_fn: optional callable with signature
              reranker_fn(query_embedding, text, metadata) -> float
          that returns a relevance score (higher is better). If provided, it
          will be used to compute new scores for each candidate.

        Returns: list of (text, metadata, score) sorted by `score` desc.
        """
        if candidates is None:
            if query_embedding is None:
                raise ValueError("Cần query_embedding để tìm kiếm ứng viên")
            candidates = self.search(query_embedding, top_k=top_k*2)

        scored = []

        for text, metadata, old_score, idx in candidates:
            if reranker_fn:
                # Ưu tiên dùng hàm rerank tùy chỉnh (Heuristic hoặc LLM)
                try:
                    score = reranker_fn(query_text, text, metadata)
                    print(f"Documents: {text}")
                    print(f"Score: {score}")
                except:
                    score = old_score 
            else:
                # Level 1: Dùng embedding đã có sẵn qua index (tối ưu speed)
                score = old_score 
            
            scored.append((text, metadata, score))

        scored.sort(key=lambda x: x[2], reverse=True)
        return scored[:top_k]
    
# Re-rank Level: 2 - Rule / Heuristic semantic
def heuristic_reranker(query, text, metadata):
    score = 0.0

    if "định nghĩa" in query.lower():
        if metadata.get("section") == "definition":
            score += 2

    if len(text) > 300:
        score += 0.5

    return score

# Re-rank Level: 3 - LLM Pointwise Scoring

def parse_score(llm_output):
    # Tìm tất cả các con số (bao gồm cả số thập phân) trong chuỗi
    match = re.search(r"Score:\s*(\d+\.?\d*)", llm_output)
    if not match:
        # Nếu không tìm thấy format "Score: X", thử tìm con số bất kỳ
        match = re.search(r"(\d+\.?\d*)", llm_output)
    
    if match:
        try:
            score = float(match.group(1))
            # Đảm bảo điểm nằm trong khoảng 0-10
            return max(0.0, min(10.0, score))
        except ValueError:
            return 0.0
    return 0.0 # Giá trị mặc định nếu thất bại hoàn toàn

def llm_pointwise_reranker(query, text, metadata):
    system = """
    You are a strict relevance judge. Your task is to evaluate if a Document segment contains enough information to answer a specific Query.

    ### SCORING GUIDELINES:
    - **10**: Contains the EXACT and DIRECT answer to the query.
    - **7-9**: Highly relevant, provides partial answer or very strong context.
    - **4-6**: Related to the topic but does not answer the specific question.
    - **1-3**: Shares keywords but context is different.
    - **0**: Completely irrelevant or unrelated.

    ### CRITICAL RULES:
    1. If the document mentions the topic (e.g., Remote work) but does not address the specific subject (e.g., Probationary employees), the score MUST be below 5.
    2. Be extremely stingy with '10' scores. 
    """

    prompt = f"""
    Query: {query}
    Document Content: {text}
    Document Metadata: {metadata}

    Analyze the relationship:
    1. Does the document mention "{query}"?
    2. Does it provide a clear Yes/No or specific rule for it?

    Output Format:
    Reasoning: <Short analysis>
    Score: <Integer 0-10>
    """
    return float(parse_score(call_instruction_llm(system=system, prompt=prompt)))


    # Re-rank Level: 4 up - LLM Pairwise Rerank, LLM Pairwise Rerank, LLM Listwise Rerank

