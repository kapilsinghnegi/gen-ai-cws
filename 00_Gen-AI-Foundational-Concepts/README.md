# Generative AI Foundations

## The Big Picture

> **What exactly is AI, and how are AI, Machine Learning, Deep Learning, and Generative AI related?**

A useful hierarchy:

**Artificial Intelligence (AI)**
→ **Machine Learning (ML)**
→ **Deep Learning (DL)**
→ **Generative AI (GenAI)**

The important thing is not to memorize these terms individually. Understand **why each concept emerged** and what problem it helps solve.

### The progression

| Field                | Main idea                                                                          |
| -------------------- | ---------------------------------------------------------------------------------- |
| **AI**               | Make machines capable of performing tasks that normally require human intelligence |
| **Machine Learning** | Instead of manually writing every rule, let the computer learn patterns from data  |
| **Deep Learning**    | Use deep neural networks to automatically learn complex features and patterns      |
| **Generative AI**    | Generate new content such as text, images, audio, or video                         |

---

## What Is Artificial Intelligence?

**Artificial Intelligence (AI)** is the broad idea of building machines that can perform tasks requiring intelligence that humans would normally provide.

Examples:

* Making decisions
* Recognizing faces
* Playing games
* Finding routes
* Understanding language
* Responding to questions

### Real-life Examples

* Chess-playing systems
* Google Maps route selection
* Face recognition / Face ID
* Chatbots such as ChatGPT and Gemini

The key idea is:

> **AI is the goal or broader field, not one specific technology.**

Machine Learning and Deep Learning are approaches used to build AI systems.

---

## Traditional AI: The Rule-Based Approach

One early way of building an intelligent system was to manually write rules.

### Example: Loan Approval

Imagine a bank wants to decide whether someone should receive a loan.

A programmer might create rules such as:

```text
IF salary > threshold
AND credit score > threshold
AND existing loans satisfy certain conditions
THEN approve loan
ELSE reject loan
```

The computer simply follows the rules written by humans.

### The problem

Real-world situations can contain an enormous number of possible patterns.

For example, consider a **spam detector**.

You might initially create:

```text
IF email contains "you won money"
THEN spam
```

A spammer can easily change the wording:

```text
"Congratulations! You have received a reward."
```

Now you need another rule.

Then the spammer changes it again.

Soon you have:

```text
Rule 1
Rule 2
Rule 3
Rule 4
...
Rule 1000
...
```

This approach does not scale well because humans cannot manually write rules for every possible situation.

### Core problem

> **There can be too many possible patterns for humans to explicitly program.**

### This leads to the idea of **Machine Learning**.

## Machine Learning

### The Core Idea

Instead of telling the computer **every rule**, give it **examples** and allow it to learn patterns from those examples.

#### Traditional programming

```text
Rules + Data → Output
```

#### Machine Learning

```text
Data + Expected Outputs → Learned Model
```

The learned model can then be used on new data.

---

### Example: Spam Detection

Suppose we have **100,000 emails**.

Each email is labelled:

```text
Email 1 → Spam
Email 2 → Spam
Email 3 → Not Spam
Email 4 → Spam
Email 5 → Not Spam
...
```

Instead of manually telling the computer:

> "If this word appears, classify it as spam."

we give the computer the labelled examples.

The model attempts to discover patterns in the data.

Then, when a new email arrives:

```text
New Email
    ↓
Learned Model
    ↓
Spam / Not Spam
```

### Beginner-friendly definition

> **Machine Learning is a way of building systems that learn patterns from data and use those learned patterns to make predictions or decisions.**

The important distinction is:

**Traditional approach:**
Human writes the rules.

**Machine Learning:**
Machine learns patterns from examples.

---

### Experience Machine Learning Practically

The tutorial demonstrates Machine Learning using [**Google's Teachable Machine**](https://teachablemachine.withgoogle.com/train).

The basic experiment:

1. Create classes.
2. Provide examples for each class.
3. Collect multiple samples.
4. Train the model.
5. Give it a new example.
6. Observe its prediction.

---

### The Problem With Traditional Machine Learning

Machine Learning solves the problem of manually writing thousands of rules, but another problem appears.

Consider **face recognition**.

An image consists of pixels, and each pixel contains color information.

A traditional ML system may require engineers to identify useful features such as:

* Distance between the eyes
* Face width
* Nose shape
* Skin color
* Other measurable properties

These useful pieces of information are called **features**.

---

### What Is a Feature?

A **feature** is a piece of information about the input that a model can use when making a prediction or decision.

#### Face recognition

Possible features:

```text
Face width
Distance between eyes
Nose shape
Other facial characteristics
```

#### Pencil recognition

Possible features:

```text
Color
Shape
Sharp tip
Length
Thickness
```

#### House price prediction

Possible features:

```text
House size
Number of rooms
Location
Age of house
```

So:

> **Feature = useful information about the input used by a model.**

---

### Why Features Become a Problem

For simple structured data, humans can often identify useful features.

But consider:

* Images
* Speech
* Video
* Natural language

These contain extremely complicated patterns.

Manually defining every useful feature becomes difficult.

This leads to the next major idea:

> **Can the model learn the useful features by itself?**

That question leads to **Deep Learning**.

---

## Deep Learning

> **Deep Learning is a type of Machine Learning that uses neural networks with multiple layers to learn complex patterns from data.**

The important relationship is:

```text
AI
└── Machine Learning
    └── Deep Learning
```

Deep Learning is therefore **not separate from Machine Learning**. It is a subfield/type of Machine Learning.

---

### Neural Networks

A **neural network** can be understood initially as a learning system consisting of interconnected layers.

A simplified structure:

```text
Input
  ↓
Hidden Layer
  ↓
Hidden Layer
  ↓
Hidden Layer
  ↓
Output
```

A network with multiple hidden layers is commonly called a **deep neural network**.

The model receives data and learns useful patterns through these layers.

---

### How Deep Learning Learns Features

Consider image recognition.

Suppose we provide a raw image to a deep neural network.

A simplified conceptual flow is:

```text
Raw Image
    ↓
Early Layers
    ↓
Edges / Lines
    ↓
Later Layers
    ↓
Shapes / Parts
    ↓
Deeper Layers
    ↓
Higher-level Patterns
    ↓
Prediction
```

The important idea is that we don't manually specify every feature.

The network learns useful representations through multiple layers during training.

#### Why this matters

This is one of the major reasons Deep Learning became powerful for:

* Image processing
* Speech
* Natural language
* Video
* Other complex data

---

### Experience Deep Learning

The tutorial recommends [Google's interactive neural-network exercises](https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises).

You can experiment with:

* Number of hidden layers
* Different network configurations
* Linear/non-linear settings
* How patterns change as the network changes

The goal is not initially to understand the mathematics behind neural networks.

The goal is to **visually develop an intuition for how multiple layers learn patterns**.

---

## The Limitation of ML/DL: Prediction

Traditional Machine Learning and Deep Learning systems are often built to **predict something**.

Examples:

```text
Email → Spam / Not Spam

Image → Cat / Dog

Transaction → Fraud / Not Fraud

Input → Predicted Number
```

These systems generally answer questions such as:

> "Which category does this input belong to?"

or

> "What value should I predict?"

But engineers wanted systems that could do something different:

> **Create something new.**

This leads to **Generative AI**.

---

## Generative AI

**Generative AI** refers to AI systems capable of generating new content based on a request.

Examples of generated content:

* Text
* Images
* Audio
* Video
* Code

### Classification vs Generation

Suppose we give a model an email.

#### Traditional ML

```text
Email
 ↓
Positive / Negative
```

#### Generative AI

```text
Instruction:
"Write a reply to this email."

        ↓

New Email
```

The major shift is:

> **Instead of only predicting/classifying existing information, the system can generate new content.**

---

### AI → ML → Deep Learning → GenAI

A useful way to remember the progression:

#### AI

**Goal:**
Make machines capable of intelligent tasks.

#### Machine Learning

**Problem solved:**
Writing every possible rule manually is impractical.

**Approach:**
Learn patterns from data.

#### Deep Learning

**Problem solved:**
Manually defining complex features is difficult.

**Approach:**
Use deep neural networks to learn complex patterns/features.

#### Generative AI

**New capability:**
Generate new content rather than only making predictions/classifications.

---

### Generative AI Is Defined by Its Output

> **Generative AI is characterized by the type of output it creates.**

For example:

```text
Text Generator
Image Generator
Video Generator
Audio Generator
```

Large Language Models (LLMs), image generators, and video generators are modern systems built using deep-learning techniques.

---

## What Is an LLM?

LLM = **Large Language Model**

Break the term into three parts.

### Large

It is trained on a very large amount of textual/language data.

The tutorial gives examples such as:

* Books
* Websites
* Articles
* Code
* Research papers
* Conversations

### Language

The model works with patterns in language.

This can include:

* English
* Hindi
* French
* Other human languages
* Programming languages such as Python, Java, SQL, etc.

### Model

A model is a trained system that has learned patterns from its training data and can use those learned patterns to produce outputs.

---

### What Does an LLM Actually Do?

> **An LLM predicts the next token.**

For example:

```text
"The capital of France is ___"
```

The model predicts a likely continuation:

```text
Paris
```

Similarly:

```text
"Python is a programming ___"
```

A likely continuation is:

```text
language
```

The model repeatedly predicts the next token to construct a complete response.

---

### What Can an LLM Do?

LLMs can perform many language-related tasks, such as:

* Generate text
* Answer questions
* Summarize text
* Translate
* Generate code
* Rewrite content
* Continue text

These capabilities come from the model's ability to learn patterns in language.

---

### What Can't an LLM Automatically Do?

An LLM does **not automatically have access to everything around you**.

For example, it cannot inherently:

* Search the live internet
* Read your company's private database
* Access your emails
* Read local files
* Send WhatsApp messages

Such capabilities require appropriate external tools, permissions, APIs, or integrations.

### Important mental model

An AI system's capabilities depend on:

```text
What it learned during training
+
What you provide in the prompt/context
+
What external tools it is connected to
```

---

### Common LLM Misconceptions

### ❌ ChatGPT is an LLM

Better mental model:

**ChatGPT is an application that uses an LLM.**

### ❌ LLM = AI

No.

An LLM is **one type of AI model specialized in language**.

### ❌ An LLM can access everything

No.

Its available information depends on:

* Training
* Current provided context
* Connected tools/data sources

### ❌ LLM automatically knows current/private information

Not necessarily.

External information generally needs to be provided or made available through appropriate tools.

---

## Tokens

Computers ultimately operate on numerical representations.

An LLM therefore does not directly process a sentence in the same way humans read it.

The text is broken into smaller pieces called **tokens**.

Example:

```text
"I love tea"
```

Conceptually:

```text
"I"   → Token
"love" → Token
"tea"  → Token
```

Each token is associated with a numerical ID.

---

### What Is Tokenization?

> **Tokenization is the process of breaking text into tokens.**

A token is **not necessarily a complete word**.

Depending on the tokenizer:

```text
One word → One token
```

or

```text
One word → Multiple tokens
```

Practice Tokenizer: [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

For example, a long or less common word may be split into multiple pieces.

This is why:

> **Token ≠ Word**

---


### Token IDs

Each token is assigned an ID.

For example:

```text
"I"     → 123
"love"  → 456
"tea"   → 789
```

These numbers are primarily **identifiers**, not values that have mathematical meaning by themselves.

### Important analogy

Think of student roll numbers:

```text
Aman → Roll No. 1
Amit → Roll No. 2
```

The number identifies the student; it doesn't mean Aman is somehow "less" than Amit.

Token IDs work similarly as identifiers within a model's vocabulary.

---

### Vocabulary

A model has a collection/list of tokens it knows.

This collection is called its **vocabulary**.

Conceptually:

```text
Vocabulary

Token A → ID
Token B → ID
Token C → ID
Token D → ID
...
```

The token ID identifies where a token exists in that vocabulary.

---

### Token IDs Can Depend on the Model

Tokenization is model/tokenizer-dependent.

The same text can receive different token IDs when using different models/tokenizers.

Therefore:

> **Do not assume that a token always has one universal ID across every AI model.**

---

## Context

Before understanding Context Window, first understand **context** itself.

### Context

Context means:

> **Information surrounding something that helps us understand it.**

Example:

```text
"It is ready."
```

By itself, this is ambiguous.

But:

```text
"The pizza is in the oven.
It is ready."
```

Now "it" and "ready" have meaningful context.

The additional information helps us interpret the current statement.

---

## Context Window

A **context window** is the amount of information an AI model can consider as context when generating a response.

Think of it like a window in a room.

If the window is small:

```text
You can see less.
```

If the window is large:

```text
You can see more.
```

Similarly:

```text
Small Context Window
→ Less information available to the model

Large Context Window
→ More information available to the model
```

---

### Context Window in a Conversation

Suppose a conversation contains:

```text
Message 1
Message 2
Message 3
...
Message 500
```

The model cannot necessarily treat an unlimited conversation as simultaneously available context.

Once the amount of information exceeds the model's usable context window, older information may no longer fit into the active context.

This can result in the model no longer having access to some earlier conversation content.

---

### Context Window ≠ Memory

This distinction is important.

#### Context Window

Answers:

> **"What information can the model currently see/use as context?"**

#### Memory

Answers:

> **"What information is retained across conversations or interactions?"**

They are related concepts, but they are **not the same thing**.

#### Easy analogy

```text
Context Window = What is currently visible through the window

Memory = What has been remembered
```

---

### Why Context Window Matters

Suppose you provide a large document to an AI system.

You then ask:

> "What does page 3 say?"

The model needs the relevant information available in its context to answer accurately.

A larger context window allows the model to consider more information at once.

Therefore:

> **Context window size is important when working with long conversations, documents, codebases, or other large inputs.**

---

## Temperature

The tutorial introduces **temperature** as a model-generation setting.

It does **not** mean physical temperature.

Temperature controls how predictable vs. creative the generated output can be.

### Simplified mental model

```text
Lower Temperature
        ↓
More predictable / consistent

Higher Temperature
        ↓
More variation / creativity
```

---

### Low vs High Temperature

Imagine a teacher asks:

> "What fruit is this?"

#### Student A

> "Apple."

A safe, likely answer.

#### Student B

> "It could be a lychee or dragon fruit."

There are multiple possibilities, so the answer is more exploratory.

This is the intuition behind temperature.

---

### Low Temperature

Useful when you want:

* Consistency
* Predictability
* More deterministic behavior
* Reliable answers where one answer is expected

Example:

```text
What is the capital of India?
```

Expected:

```text
New Delhi
```

---

### Higher Temperature

Useful when you want:

* Creative ideas
* Brainstorming
* Story generation
* Poetry
* Multiple possibilities

Example:

```text
Write a creative story about a robot.
```

There can be many valid answers.

---

### Temperature Does NOT Add Knowledge

A common misunderstanding:

> **Increasing temperature does not give the model additional knowledge.**

It changes the generation behavior/variation.

For example:

```text
2 + 2 = 4
```

Changing temperature should not magically change the mathematical fact.

Temperature matters much more when multiple possible outputs exist.

---

## Next Token Prediction

This is one of the most important concepts in understanding LLMs.

The simplified idea is:

> **Given the preceding tokens, predict what token is likely to come next.**

Example:

```text
The capital of France is
                ↓
              Paris
```

Another example:

```text
Python is a programming
                     ↓
                  language
```

The model repeatedly performs this process to generate a response.

---

### LLMs Generate Responses Step by Step

Suppose you ask:

```text
Write a poem.
```

The model does not conceptually produce the entire poem as one indivisible operation.

A simplified view is:

```text
Predict token 1
      ↓
Predict token 2
      ↓
Predict token 3
      ↓
Predict token 4
      ↓
...
      ↓
Complete response
```

This repeated next-token prediction is a fundamental mental model for understanding language generation.

---

### Why Next-Token Prediction Can Produce Complex Text

Consider:

```text
The sun rises in the
```

A likely continuation is:

```text
east
```

Then:

```text
The sun rises in the east and
```

A likely continuation might be:

```text
sets
```

Then:

```text
The sun rises in the east and sets
```

Each prediction changes the context available for the next prediction.

Therefore:

```text
Previous tokens
      ↓
Predict next token
      ↓
Updated context
      ↓
Predict next token
      ↓
...
```

This repeated process can produce long and coherent outputs.

---

## Hallucination

A major limitation of generative AI is **hallucination**.

A hallucination occurs when an AI generates information that **does not have adequate supporting evidence or grounding**.

It is more than simply saying:

> "The answer is wrong."

The important issue is:

> **The model produces an answer even though it does not have reliable evidence for that answer.**

---

### Hallucination Example

Imagine a company chatbot has access to this policy:

```text
Annual Leave: 20 days
Casual Leave: 10 days
```

Now ask:

> "How many annual leaves can I take?"

It can answer:

```text
20 days
```

because that information exists in the provided document.

Now ask:

> "How many maternity leaves can I take?"

Suppose the document says nothing about maternity leave.

A reliable system should say something like:

> "The provided document does not specify a maternity leave policy."

But if the AI invents:

```text
Maternity Leave: 90 days
```

without evidence, that is a hallucination.

---

### Why Do Hallucinations Happen?

Connect this back to **next-token prediction**.

The model's basic generation process is focused on producing a likely continuation.

It does not inherently perform a perfect:

```text
Generate answer
      ↓
Verify every claim
      ↓
Check authoritative source
      ↓
Answer only if proven
```

Therefore, an AI system can sometimes generate a plausible-sounding answer without sufficient evidence.

> **Plausible does not necessarily mean true.**

---

## How to Think About AI Reliability

When using AI for factual or important tasks, ask:

1. **Where did this information come from?**
2. **Was the source provided to the model?**
3. **Does the model have access to an external source/tool?**
4. **Can the answer be verified?**
5. **Is the model generating or retrieving evidence?**

This becomes especially important for:

* Legal information
* Financial information
* Medical information
* Company policies
* Current events
* Exact statistics
* Important business decisions

---

## Important Terminology — Quick Reference

| Term                      | Meaning                                                                 |
| ------------------------- | ----------------------------------------------------------------------- |
| **AI**                    | Broad field/goal of building systems capable of intelligent tasks       |
| **Machine Learning**      | Learning patterns from data rather than manually programming every rule |
| **Feature**               | Useful piece of information used by a model                             |
| **Deep Learning**         | ML using neural networks with multiple layers                           |
| **Neural Network**        | Interconnected learning system made of layers                           |
| **Generative AI**         | AI capable of generating new content                                    |
| **LLM**                   | Large Language Model                                                    |
| **Token**                 | A unit/piece of text processed by a language model                      |
| **Tokenization**          | Breaking text into tokens                                               |
| **Token ID**              | Numerical identifier assigned to a token                                |
| **Vocabulary**            | Collection of tokens known by a tokenizer/model                         |
| **Context**               | Information that helps interpret the current input                      |
| **Context Window**        | Amount of information available to the model as context                 |
| **Temperature**           | Generation setting controlling output variability/creativity            |
| **Next-Token Prediction** | Predicting the next token based on previous context                     |
| **Hallucination**         | Unsupported/invented AI output presented as an answer                   |

---
