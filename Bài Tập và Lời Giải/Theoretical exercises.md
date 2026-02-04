# RAG Theory Exercises

## Level 1 – Fundamental Awareness & Thinking

### Exercise 1: Differentiating Pure LLM and RAG

**Objective:** Understand *why* RAG is needed

**Problem:**
You have a chatbot that answers questions about **company rules** written in an internal PDF file.

1. If only using LLM (without RAG), what are the risks of using a chatbot?

2. If using RAG, what problems are solved?

👉 Answer with bullet points.

---

### Lesson 2: Identifying whether a problem requires RAG

**Objective:** Know *when to use RAG*

**Assignment:**
Mark ✔ or ✘ for the following cases:

1. Chatbot answering questions about company internal rules

2. Writing romantic love poems

3. Q&A on internal technical documentation

4. Writing a creative marketing slogan

Briefly explain the reason.

---

## Level 2 – Data & Chunking

### Lesson 3: Choosing a chunking strategy

**Objective:** Understand the role of chunking

**Assignment:**
You have a 50-page PDF file (software user manual).

1. Why can't the entire file be included in the LLM?

2. What token size would you choose for the chunk? Is there overlap? Why?

---

### Lesson 4: Identifying Good and Poor Chunks

**Objective:** Understand what constitutes a "meaningful" chunk.

**Assignment:**
Compare two chunking methods:

* A. Cutting exactly 500 tokens, regardless of semantics

* B. Dividing by document headings/sections

Which method do you think is better for RAG? Explain.

---

## Level 3 – Embedding & Retrieval

### Lesson 5: Understanding Embedding Through Examples

**Objective:** Understand that embedding is *semantic comparison*, not keyword comparison.

**Assignment:**
Question: "How to reset a system password"

In your opinion, which section would the embedding system prioritize?

* A. "Instructions for changing account password"

* B. "Information security regulations"

Explain your reasoning.

---
### Lesson 6: Too Many or Too Few Top-Ks?

**Objective:** Understand trade-offs in retrieval

**Question:**
You are using Top-K = 20, but your answers are often rambling.

1. What could be the cause?

2. Which parameters would you adjust?

---

## Level 4 – Prompt Augmentation

### Lesson 7: Writing a safe RAG prompt

**Objective:** Reduce hallucination

**Question:** Write a prompt requesting an LLM:

* Only answer based on context
* If no information is found, say "Not found"

(Just the prompt, no sample answer needed)

---

### Lesson 8: Identifying poor RAG prompts

**Objective:** Understand how prompts affect quality

**Question:** What is wrong with the following prompt?

> "Based on the above document and your knowledge, answer the following question."

Identify the risks.

---

## Level 5 – Advanced RAG

### Lesson 9: When is re-ranking necessary?

**Objective:** Know when Naive RAG is insufficient.

**Assignment:**
The RAG system returns 10 context snippets, but only 3 are truly relevant.

1. What is the purpose of re-ranking?

2. At what step in the pipeline is re-ranking performed?

---

### Lesson 10: Multi-query for ambiguous questions

**Objective:** Understand query transformation.

**Assignment:**
User question: "Leave policy"

Write 3 clearer queries to retrieve the document.

---