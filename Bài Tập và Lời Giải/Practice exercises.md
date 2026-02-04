# RAG Practice Exercises

## Level 1 – Getting Started with the RAG Pipeline

### Practice 1: Minimalist RAG (Hello RAG)

**Objective:** Understand the end-to-end pipeline

**Assignment:**

1. Prepare 3–5 short text snippets (txt) on the same topic (e.g., company regulations)

2. Implementation:

* Chunk (if needed)

* Embed

* Save to vector store

3. Formulate a question and answer using RAG

✅ Expected Result: The answer uses the correct content from the data.

---

### Practice 2: Comparing Pure LLM vs. RAG

**Objective:** To clearly see the value of RAG

**Assignment:**

* Ask the same question:

* Attempt 1: Without RAG

* Attempt 2: With RAG

* Comparison:

* Accuracy

* Level of hallucination

---

## Level 2 – Chunking & Data Quality

### Practice 3: Chunk Size Experiment

**Objective:** To understand how chunking affects retrieval

**Assignment:**

Run the same dataset with 3 configurations:

* Chunk 300 tokens
* Chunk 800 tokens
* Chunk 800 tokens + overlap

Compare the quality of the answers.

---

### Practice 4: Bad Chunks vs. Good Chunks

**Objective:** Identify data errors

**Assignment:**

* Intentionally create chunks that are cut off in the middle of sentences/ideas

* Compare the results with chunks according to headings

Draw conclusions.

---

## Level 3 – Retrieval

### Practice 5: Adjust Top-K

**Objective:** Understand the trade-off between recall and precision

**Assignment:**

Run retrieval with:

* Top-K = 3

* Top-K = 5

* Top-K = 10

Observe the changes in the responses.

---

### Practice 6: Adding Metadata Filtering

**Objective:** Control context

**Assignment:**

* Attach metadata (date/category) to the document
* Access the document only within a specified range

---

## Level 4 – Prompt Augmentation

### Practice 7: Source-Bound Prompts

**Objective:** Reduce hallucination

**Assignment:** Write a prompt that requests:

* Only respond from the context
* Quote the context used

---

### Practice 8: Testing Bad Prompts

**Objective:** Understand how prompts cause errors

**Assignment:**

* Use prompts that allow "incorporating external knowledge"

* Observe the errors that occur

---

## Level 5 – Advanced RAG

### Practice 9: Re-ranking Context

**Objective:** Increase accuracy

**Assignment:**

* Get Top-K = 10
* Re-rank and keep only the Top 3

Compare before/after re-ranking.

---

### Practice 10: Multi-query retrieval

**Objective:** Solve ambiguous questions

**Assignment:**

* Generate 3 query variations from 1 question
* Merge retrieval results

---