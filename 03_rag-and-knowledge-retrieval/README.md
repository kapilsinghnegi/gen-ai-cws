# RAG and Knowledge Retrieval

## What Problem Does RAG Solve?

An LLM does **not automatically know your private, company-specific, or latest data**.

For example, suppose a company has its own:

* Refund policy
* Course details
* Placement rules
* Interview guarantee policy

A general-purpose LLM won't automatically know these internal policies.

If a student asks:

> "Can I get a refund after 5 days?"

Simply asking a general LLM may produce an incorrect or guessed answer because the model doesn't know the company's actual refund policy.

### The solution

Instead of asking the LLM to guess, we provide the relevant company data to it.

The system:

```text
User Question
      ↓
Search Company Documents
      ↓
Find Relevant Information
      ↓
Give Information to LLM
      ↓
LLM Generates Answer
      ↓
User
```

This approach is called:

> **RAG — Retrieval-Augmented Generation**

---

## RAG — Retrieval-Augmented Generation

RAG consists of two important ideas:

### Retrieval

Find useful/relevant information from your data.

### Generation

Give that retrieved information to the LLM so it can generate the final answer.

Conceptually:

```text
Question
   ↓
Retrieve useful information
   ↓
Relevant context
   ↓
LLM
   ↓
Generated answer
```

The transcript explains it as:

> First retrieve useful knowledge from the data, provide it to the LLM, and then let the LLM generate the answer.

---

## RAG Components

The lecture breaks RAG into smaller concepts:

1. **Chunking**
2. **Embeddings**
3. **Vectors**
4. **Similarity**
5. **Retrieval**
6. **LLM Generation**

---

## Chunking

### What is Chunking?

Suppose you have a large document:

```text
Large Document
       ↓
 ┌─────┬─────┬─────┬─────┬─────┐
 │ P1  │ P2  │ P3  │ P4  │ P5  │
 └─────┴─────┴─────┴─────┴─────┘
```

**Chunking** means dividing a large piece of text into smaller, useful pieces called **chunks**.

The purpose is to make the information easier to search and retrieve.

---

### Why Do We Need Chunking?

Imagine a company document containing:

```text
Course duration
Recorded class access
Live class schedule
Refund policy
Assignment requirements
Interview opportunities
```

Now a user asks:

> "How many interview opportunities do students get?"

We don't want to process the entire document unnecessarily.

The useful information is something like:

> Eligible students receive a minimum of three interview opportunities.

So instead of treating the entire document as one huge block, we divide it into smaller pieces.

---

### Chunks

After splitting a document, each smaller piece is called a:

> **Chunk**

For example:

```text
Document
│
├── Chunk 1
├── Chunk 2
├── Chunk 3
├── Chunk 4
├── Chunk 5
└── Chunk 6
```

In the demonstration, the document is split line-by-line, producing multiple chunks.

---

### Basic Chunking in Python

The transcript demonstrates basic chunking using Python string operations.

The basic idea is:

```python
chunks = text.strip().split("\n")
```

#### `strip()`

Removes unnecessary whitespace from the beginning and end of a string.

Example:

```text
"   Python   "
```

becomes:

```text
"Python"
```

---

#### `split("\n")`

The `split()` method divides a string into multiple pieces.

```python
text.split("\n")
```

Therefore:

```text
Sentence 1
Sentence 2
Sentence 3
Sentence 4
```

can become:

```python
[
    "Sentence 1",
    "Sentence 2",
    "Sentence 3",
    "Sentence 4"
]
```

These individual pieces can then be treated as chunks.

---

### Problem With Very Small Chunks

The first chunking approach creates very small chunks.

This creates an important problem:

> **Context can be lost.**

For example, suppose two pieces of information are related:

```text
Students must complete all assignments.

Eligible students receive three interview opportunities.
```

If these become separate chunks, a question about:

> "When does a student become eligible for three interviews?"

requires information from both chunks.

If the chunks are too small, the relevant context gets separated.

---

### Chunk Size

This introduces an important concept:

> **Chunk Size**

Chunk size means:

> **How much text/information is stored inside one chunk.**

For example:

```text
Chunk size = 1 sentence
```

or:

```text
Chunk size = 2 sentences
```

---

### Grouping Multiple Sentences

Instead of:

```text
Chunk 1 → Sentence 1
Chunk 2 → Sentence 2
Chunk 3 → Sentence 3
Chunk 4 → Sentence 4
```

we can create:

```text
Chunk 1 → Sentence 1 + Sentence 2
Chunk 2 → Sentence 3 + Sentence 4
Chunk 3 → Sentence 5 + Sentence 6
```

This preserves more context.

---


### Converting Chunk Lists Into Text

After grouping multiple pieces, each chunk may initially be represented as a **list**.

For example:

```python
[
    "Sentence 1",
    "Sentence 2"
]
```

But for RAG, we want a clean text chunk:

```text
Sentence 1 Sentence 2
```

#### `join()`

`join()` combines multiple strings using a specified separator.

Example:

```python
" ".join(["Hello", "Python"])
```

produces:

```text
Hello Python
```

The same concept is applied to the chunks.

---

### The Real Chunking Question

The difficult part of chunking is **not simply using `split()`**.

The important question is:

> **How much information should one chunk contain?**

For example:

```text
1 sentence per chunk?
2 sentences?
5 sentences?
500 characters?
1000 characters?
```

The appropriate choice depends on the application and data.

---

### How Is Chunk Size Measured?

In real RAG systems, chunk size can be measured using:

* **Characters**
* **Tokens**

---

### Why Chunk Size Matters

If chunks are **too small**:

```text
Too little context
       ↓
Context gets separated
       ↓
Retrieval may miss related information
```

If chunks are **too large**:

```text
Too much information
       ↓
Less focused retrieval
       ↓
Unnecessary information may be retrieved
```

Therefore, chunking is a balance between:

> **Enough context + focused information**

---

## Embeddings

After chunking, the next important concept is:

> **Embeddings**

Embeddings is the process of converting text into numbers so that those numerical representations can be used for searching.

Conceptually:

```text
Text
 ↓
Embedding Model
 ↓
Numbers / Vector
```

For example:

```text
"Refund requests are allowed within 7 days"
                 ↓
        Embedding Model
                 ↓
        [0.12, -0.45, 0.73, ...]
```

The exact numbers aren't important for understanding the basic idea.

---

### Why Convert Text Into Numbers?

Computers can work with numerical representations to compare information.

Suppose we have:

```text
Document 1:
"Refund requests are allowed within 7 days."

Document 2:
"Classes happen Monday to Friday."

Document 3:
"Students receive three interview opportunities."
```

A user's question might be:

```text
"Can I get my money back after five days?"
```

The wording isn't identical to the document.

The user says:

```text
"money back"
```

while the document says:

```text
"refund"
```

The system needs to understand that these concepts are related.

Embeddings allow the text to be represented in a numerical space where semantic similarity can be compared.

---

### Semantic Similarity

Consider:

```text
Question:
"Can I get my money back after five days?"
```

Document:

```text
"Refund requests are allowed within 7 days."
```

The words are not identical:

```text
money back ≠ refund
```

But the **meaning is similar**.

This is why simple exact keyword matching isn't enough.

Embeddings help compare the **meaning/semantic relationship** between the question and document chunks.

---

### Question Embedding

The user's question is also converted into an embedding.

```text
User Question
      ↓
Embedding Model
      ↓
Question Vector
```

Similarly, the document chunks have their own vectors:

```text
Chunk 1 → Vector
Chunk 2 → Vector
Chunk 3 → Vector
Chunk 4 → Vector
```

Now we can compare:

```text
Question Vector
      ↓
Compare with
      ↓
Document Vectors
```

---

### Cosine Similarity

To compare the question vector with document vectors, the lecture uses:

> **Cosine Similarity**

Conceptually:

```text
Question Vector
       ↓
   Cosine Similarity
       ↓
Similarity Score
```

The score indicates how similar the vectors are.

Higher score:

```text
Higher similarity
```

Lower score:

```text
Lower similarity
```

The transcript uses values such as:

```text
0.78
0.20
0.24
0.31
```

to demonstrate that the highest score represents the most similar document.

---

#### Example of Similarity Scores

Suppose we have:

```text
Document 1 → 0.78
Document 2 → 0.20
Document 3 → 0.24
Document 4 → 0.31
```

The highest score is:

```text
0.78
```

Therefore:

```text
Document 1
```

is considered the best match for the question.

---

### Finding the Best Match

The lecture uses NumPy's:

```python
np.argmax(scores)
```

The purpose of `argmax()` is:

> Find the **index of the largest value**.

Example:

```python
scores = [10, 20, 30, 100, 50]
```

The largest value is:

```text
100
```

Its index is:

```text
3
```

Therefore:

```python
np.argmax(scores)
```

returns:

```text
3
```

---

### Retrieving the Best Document

Once we have the best index:

```python
best_index = np.argmax(scores)
```

we can retrieve the corresponding document:

```python
best_document = documents[best_index]
```

Conceptually:

```text
Question
   ↓
Question Embedding
   ↓
Compare with Document Embeddings
   ↓
Similarity Scores
   ↓
Find Highest Score
   ↓
Best Index
   ↓
Best Document
```

This is the basic retrieval process demonstrated in the lecture.

---

### Complete Retrieval Example

Suppose the user asks:

> "Can I get my refund after five days?"

The documents contain:

```text
Document 1:
Refund requests are allowed within 7 days.

Document 2:
Classes happen Monday to Friday.

Document 3:
Students get three interview opportunities.
```

After embedding and comparison:

```text
Document 1 → 0.82
Document 2 → 0.17
Document 3 → 0.21
```

The highest score is Document 1.

Therefore:

```text
Retrieved Context:
"Refund requests are allowed within 7 days."
```

---

### Retrieval

The transcript summarizes the process as:

```text
User Question
      ↓
Question Embedding
      ↓
Compare with Document Embeddings
      ↓
Calculate Similarity Scores
      ↓
Find Highest Score
      ↓
Retrieve Relevant Information
```

This entire process is referred to as:

> **Retrieval**

---

### RAG Does More Than Retrieval

Retrieval alone doesn't produce the final natural-language answer.

We then pass the retrieved information to an LLM.

So:

```text
Question
   ↓
Retrieval
   ↓
Relevant Context
   ↓
LLM
   ↓
Final Answer
```

This is where **Retrieval-Augmented Generation** comes together.

---

### Passing Retrieved Context to the LLM

The mini-project creates a prompt containing:

* Retrieved context
* User question
* An instruction to answer based on the context

Conceptually:

```text
Context:
[Retrieved document]

Question:
[User question]

Instruction:
Answer the question using the provided context.
```

The retrieved information acts as the knowledge source for the LLM.

---

### Why Tell the LLM to Use the Context?

Suppose we retrieve:

```text
Refund requests are allowed within 7 days.
```

and the user asks:

> "Can I get a refund after five days?"

The LLM should answer based on the retrieved information rather than relying on its general knowledge.

Therefore, the prompt explicitly instructs the model to answer using the supplied context.

---

## Why This Is Better Than Asking the LLM Directly

### Without RAG

```text
User
 ↓
LLM
 ↓
LLM guesses using its existing knowledge
```

Problem:

```text
Private company information
        ↓
Not known by model
        ↓
Possible incorrect answer
```

### With RAG

```text
User
 ↓
Retrieve company data
 ↓
Relevant context
 ↓
LLM
 ↓
Grounded answer
```

This allows the LLM to work with information that wasn't part of its original training knowledge.

---


## Key Takeaways

### RAG

Used when an LLM needs access to external/private/current information.

### Chunking

Breaks large documents into smaller pieces.

### Chunk

A smaller piece of the original document.

### Chunk Size

How much information is contained in each chunk.

### Embedding

Converts text into a numerical/vector representation.

### Similarity

Measures how closely the query and document representations are related.

### Cosine Similarity

Used in the demonstration to calculate similarity between vectors.

### Retrieval

Finds the most relevant information for a user's question.

### Generation

The LLM uses the retrieved context to generate the final response.

---

## Most Important Questions

### What problem does RAG solve?

It allows an LLM application to use external/private/domain-specific information that the base LLM may not know.

### What is chunking?

Dividing a large document into smaller pieces so relevant information can be retrieved efficiently.

### Why can't chunks simply be extremely small?

Because important context may be separated across chunks.

### What is chunk size?

The amount of text/information contained in each chunk.

### How can chunk size be measured?

The lecture mentions **characters or tokens**.

### What is an embedding?

A numerical/vector representation of text that can be used for semantic comparison.

### Why are embeddings useful?

They allow semantically related text to be compared even when the exact words are different.

### What is cosine similarity?

A similarity measure used to compare vector representations.

### What does `np.argmax()` do?

It returns the index of the largest value in an array/list.

### What is retrieval?

Finding the most relevant document/chunk based on the similarity between the user's question and stored information.

### What happens after retrieval?

The retrieved context is provided to the LLM along with the user's question, and the LLM generates the final answer.

### Why is RAG better than simply asking the LLM?

Because the LLM gets relevant external information instead of having to rely only on its existing knowledge or guess.

### What happens if the answer isn't present in the retrieved context?

The system can instruct the LLM to say that the information isn't available rather than inventing an answer.

---