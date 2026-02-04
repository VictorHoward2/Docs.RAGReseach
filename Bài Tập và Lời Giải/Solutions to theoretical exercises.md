### Lesson 1: Distinguishing Between Pure LLM and RAG

#### 1. What are the risks of using **only pure LLM (no RAG)** chatbots?

* ❌ **Content fabrication (hallucination)**

→ The LLM can *arbitrarily infer* company regulations based on general data, even if those regulations **do not exist** in the PDF.

* ❌ **Lack of internal content updates**

→ Company regulations are **private, new, internal** documents → The LLM **is not pre-trained**.

* ❌ **Vague, general answers**

→ For example: instead of quoting specific clauses, the LLM answers like "typically companies will…".

* ❌ **Unverifiable sources**

→ It's unclear which **article or page** in the PDF the answer is based on.

* ❌ **Legal/Operational Risk**

→ Incorrect responses to company regulations can lead to misinterpretations and violations of company policy.

#### 2. If using **RAG (Retrieval-Augmented Generation)**, what problems are solved?

* ✅ **Responses based on the correct internal PDF document**

→ LLMs only respond after *retrieving the relevant section* of the company regulations.

* ✅ **Significantly Reduced Hallucination**

→ No "fabrication," as the information is *anchored to real data*.

* ✅ **Easy Updates**

→ Simply replace the PDF → no need to retrain LLMs.

* ✅ **Can Be Cited and Verified**

→ Know that the response comes from a **specific section/article** in the regulations.

* ✅ **Suitable for private/enterprise data**

→ Solves the right problem: *LLM doesn't know internal data, RAG supplements external memory*.

---

Below is the **solution – focusing on the criterion of “whether or not knowledge outside of LLM is needed”** 👇

---

### Lesson 2: Identifying whether a problem requires RAG

1. **Chatbot answering about company internal rules** → ✔ **REQUIRES RAG**

* Internal rules are **private data, not included in the LLM training data**

* The answer must be **correctly worded, no speculation allowed**

2. **Writing romantic love poems** → ✘ **DOES NOT REQUIRE RAG**

* The problem is **creative**, not dependent on specific data

* Pure LLM has done very well

3. **Questions and answers about internal technical documents** → ✔ **REQUIRES RAG**

* Technical documents are often **long, detailed, and specific to the organization**

* The relevant section must be accessed before answering Words

4. **Write a creative marketing slogan** → ✘ **NO RAG required**

* The goal is **ideas & language**, not data accuracy

* RAG does not provide clear value

---

### Lesson 3: Choosing a chunking strategy

#### 1. Why **cannot include an entire 50-page PDF file in an LLM**?

* ❌ **Exceeds context window limit**

→ LLMs have a limit on the number of tokens that can be entered; a 50-page PDF usually **far exceeds its capacity**.

* ❌ **Costly and slow**

→ Including the entire document in each question is **very token-intensive** and impractical.

* ❌ **Reduces answer quality**

→ Too much information → LLMs **find it difficult to focus on the relevant part**, leading to rambling answers.

* ❌ **Not optimized for retrieval**

→ LLM does not have a “find the right section” mechanism if the document is not split.

#### 2. What **chunk size** should be in tokens? Is there an **overlap**? Why?

* ✅ **Recommended chunk size:** approximately **300–500 tokens**

* Long enough to **contain an entire idea/instruction**

* Not too long to compromise accuracy during retrieval

* ✅ **Overlap:** approximately **50–100 tokens**

* Avoid losing context when important content is **at the boundary between two chunks**

* Makes the answer more complete (e.g., definition at the end of the first chunk, example at the beginning of the second chunk)

* ❌ **Do not use chunks that are too small**

→ Loss of flow, disjointed answer

* ❌ **Do not use chunks that are too large**

→ Reduces embedding and retrieval efficiency

---

### Lesson 4: Identifying good and poor chunks

#### 🔹 A. Cut to exactly 500 tokens, regardless of semantics

* ❌ **Chunks can be cut off midway** **Points**
* ❌ **Loss of logical context** (definition in this chunk, example in another chunk)
* ❌ **Poor quality embedding** due to disorganized content
* ❌ When retrieved, LLM receives an **incomplete** section to answer

👉 This method is **technically simple but poor in quality**

#### 🔹 B. Divide by document headings/sections

* ✅ **Each chunk corresponds to a complete idea**
* ✅ **Maintains context and content logic**
* ✅ **Embedding has clear meaning**
* ✅ Retrieval returns **the correct section to read**, helping LLM answer more accurately

👉 This is a **meaningful chunk (semantic chunk)**

---
### Lesson 5: Understanding embedding through examples

#### Preferred chunk: **A. "Instructions for changing account password"** ✔

#### Explanation of why **A > B**

* 🔍 **Semantics are closer to the question**

* *reset password* ≈ *change password*

* *system/account* → same technical action

* 🧠 **Embedding encodes meaning, not just keywords**

* Although it doesn't contain the exact word "reset"

* But the **action + goal** is the same

* 📈 **A's embedding vector is closer to the question**

* Both talk about **the process of changing a password**

* Lie in the same “semantic space”

### Why **B is not prioritized** ❌

* "Information security regulations":

* **Policy/principle-based**

* Does not answer **specific instructions**
* Semantics are **far removed from the action of “reset”**

* Although There is an ambiguous *confidentiality* related word.

---

### Lesson 6: Too many or too few Top-K?

### 1. Why does **Top-K = 20** cause the answer to be rambling?

* ❌ **Too many chunks are included in the context**

* Not all 20 chunks are closely related

* The LLM has to “read” too much information

* ❌ **Semantic noise**

* Some chunks are only *slightly related*

* But still take up space in the context

* ❌ **The LLM loses focus**

* It's unclear which section is “most important”

* Leading to a scattered answer synthesis

* ❌ **Context dilution**

* Correct information is “diluted” by less relevant information

### 2. Which parameters will you adjust?

* 🔧 **Reduce Top-K**

* Example: from **20 → 5 or 3**

* Only keep the **most relevant** chunks

* 🔧 *(Advanced Option)* **Apply score threshold**

* Only take chunks with similarity > a certain threshold

* Avoid pulling in "similar" chunks

* 🔧 *(If more information is still needed)* **Re-ranking**

* Take the larger Top-K first (e.g., 20)

* Then **re-rank → choose the smaller Top-N**

---

### Lesson 7: Writing a safe RAG prompt

#### Suggested Prompt

> You are an AI assistant answering questions **based only on the CONTEXT provided below**.

>
> **Required Rules:**

>
> * Only use information contained in the CONTEXT

> * No speculation, no use of external knowledge

> * If the CONTEXT **does not contain information to answer the question**, answer with a single sentence: **“No information found.”**

>
> **CONTEXT:**

> {{context}}

>
> **QUESTION:**

> {{question}}

---

### Lesson 8: Identifying Poorly RAG Prompts

#### What's wrong with the prompt?

> **“Based on the above document *and your knowledge*…”**

👉 The phrase **“and your knowledge”** is the most dangerous point.

#### Specific Risks

* ❌ **Allows LLMs to use knowledge outside the context**

* LLMs will mix **documents + training knowledge**

* Loss of the true nature of “answers grounded on data”

* ❌ **Opens the door to hallucination**

* When documents lack information → LLMs **compensate with speculation**

* ❌ **Unable to distinguish information from documents**

* Answers sound “reasonable” but **cannot be verified**

* ❌ **RAG becomes a purely disguised LLM**

* Retrieval is ineffective

* Does not guarantee the accuracy of internal data

---

### Lesson 9: When is re-ranking necessary?

#### 1. **What are the benefits of re-ranking?**

* 🔍 **Rearranges the relevance of chunks**

* Brings **3 truly relevant chunks** to the top

* Moves similar chunks to the bottom or removes them

* 🎯 **Increases context precision**

* LLM reads **less but more accurately**

* Reduces noise and rambling answers

* 🧠 **Better understanding of question-context relationships**

* Re-ranker (usually a cross-encoder) considers **the question + each chunk**

* More accurate than pure embedding similarity

* 🚫 **Reduces indirect hallucination**

* Fewer incorrect contexts → fewer opportunities for LLM to speculate

#### 2. **Where is re-ranking located in the pipeline?**

👉 **After retrieval, before adding context to LLM**

Standard pipeline:

```
User Question

↓
Embedding Search (Large Top-K)

↓
Re-ranking (select the smaller, most accurate Top-N)

↓
LLM Answer Generation
```

---

### Lesson 10: Multi-query for ambiguous questions

Original sentence: **“Leave Policy”** → too short, unclear which *aspect* the user wants.

#### 3 clearer queries for document retrieval

1. **“Regulations on the number of annual leave days for employees”**

→ Clarify the *type of leave* and *applicable subjects*

2. **“Conditions and procedures for requesting leave in the company”**

→ Focus on the *process/method of implementation*

3. **“Paid and unpaid leave cases”**

→ Focus on *benefits and classifications*

#### Why is multi-query effective? 🧠

* 🔍 Covers **multiple reasonable intents** of the same question

* 📈 Increases **recall** when retrieving

* 🤖 Helps RAG not depend on **a single way of expressing**

#### Suggested Prompt

```
You are the system supporting document retrieval for RAG.

Your task is:
- Analyze the user's question
- Generate 3–5 different queries, each clarifying a reasonable aspect (intent) of the question
- The queries must:

+ Maintain the original intent

+ Be clear and specific

+ Be suitable for searching within internal documentation
- Not invent new topics
- Not answer the question

USER QUESTION:

{{question}}

Return a list of queries, each on a separate line.

```

👉 This prompt is usually placed **before the retrieval step**, so that the LLM acts as a “query rewriter”.

#### Why is this prompt recommended?

* 🧠 **Separate ambiguous intents into multiple perspectives**
* 🚫 Prohibit replies → avoid “LLM always replies”
* 🎯 Keep queries **close to the documentation**, don't let them stray too far

#### When **multi-query is harmful because it creates interference**

Multi-query **is not always good**. Below are cases where **multi-query should NOT be used or must be strictly controlled**:

##### ❌ 1. The question is already **very specific**

Example:

> “Procedure for resetting the password for the admin account”

👉 Multi-query in this case:

* Does not increase recall
* Only creates **similar** queries
* Adds unnecessary chunks

➡️ **Does more harm than good**

##### ❌ 2. The document is too broad, with many closely related topics

Example:

* Company handbook
* Comprehensive HR policy

Multi-query can:

* Access **many different chapters**
* The context becomes **diluted**, making LLM difficult to synthesize

##### ❌ 3. There is no subsequent re-ranking step.

Multi-query → multiple results → if:

* All contexts are combined

* No filtering / no re-ranking

👉 Result:

* Recall increases but **precision decreases significantly**

* The answer is rambling and lengthy

##### ❌ 4. The generated query is “over-interpreted”

Example question:

> “Leave Policy”

LLM generates queries:

* “Maternity leave”

* “Personal leave”

* “Long-term sick leave”

👉 If the user **only asks about annual leave**
→ Multi-query has **gone too far from the original intent**

#### How to use multi-query correctly (best practice)

* ✅ Only use when the question is short and vague

* ✅ Limit to **3–5 queries**
* ✅ Combine **re-ranking**

* ✅ Or **score threshold** after retrieval

> **Multi-query increases recall, but if not controlled, it will destroy precision.**

Or to put it more concisely:

> “Multi-query is a double-edged sword: it saves ambiguous questions, but dilutes clear questions.”

---