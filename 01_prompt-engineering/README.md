# Generative AI — Prompt Engineering

---

## What Is Prompt Engineering?

Before understanding prompt engineering, understand a **prompt**.

### Prompt

A **prompt** is an instruction or information given to an AI model to get a desired output.

Examples:

```text
Explain Python.
```

```text
Summarize this chapter.
```

```text
Translate "Good Morning" into Hindi.
```

```text
Write a professional email to a recruiter.
```

All of these are prompts.

A prompt can be extremely simple or highly detailed.

---

## Prompting vs Prompt Engineering

These two terms are related but different.

### Prompting

Simply asking an AI model to do something.

```text
Summarize this article.
```

### Prompt Engineering

Designing, testing, evaluating, and improving prompts so that the model produces **reliable and useful outputs**.

> **Prompt engineering is the process of designing, testing, and improving prompts to reliably produce the desired output.**

The important word is **reliably**.

It is not just:

> "I wrote a prompt and got a good answer once."

It is:

```text
Design Prompt
     ↓
Run Prompt
     ↓
Evaluate Output
     ↓
Identify Problems
     ↓
Improve Prompt
     ↓
Test Again
```

---

### Prompt Engineering Is Not About Memorizing Tricks

There are many prompt-engineering techniques available online.

You do **not** need to memorize dozens of tricks.

The fundamental skill is understanding:

> **What information does the model need to perform the task correctly?**

Think about four core questions:

1. **What should the AI do?**
2. **What information does it need?**
3. **What rules should it follow?**
4. **What should the output look like?**

These form the foundation of good prompts.

---

## Why Do We Need Prompt Engineering?

### LLMs Cannot Read Your Mind

An LLM does not automatically know what you want.

Suppose you tell it:

```text
Write an email.
```

The model has to make assumptions:

* Who is the recipient?
* Why are you writing?
* Is it formal or casual?
* How long should it be?
* Is it a job application?
* Is it a follow-up?
* Is it a complaint?
* Is it a sales email?

The more information you leave unspecified, the more the model has to **guess**.

### Core principle

> **The more ambiguity you leave in a prompt, the more the model has to infer.**

Therefore:

> **Clearer prompt → Less guessing → More predictable output**

---

## The Four Core Components of a Good Prompt

The tutorial introduces four fundamental components:

```text
┌────────────────────┐
│       TASK         │
├────────────────────┤
│     CONTEXT        │
├────────────────────┤
│      RULES         │
├────────────────────┤
│  OUTPUT FORMAT     │
└────────────────────┘
```

These are the most important things to understand initially.

---

## Task

### What Is the Task?

The **task** tells the AI exactly what action it should perform.

Ask yourself:

> **What exactly do I want the AI to do?**

Examples:

```text
Analyze this resume.
```

```text
Summarize this article.
```

```text
Extract the skills from this resume.
```

```text
Translate this text into Hindi.
```

```text
Generate interview questions.
```

The task should use a clear action.

### Useful task verbs

* Explain
* Summarize
* Classify
* Compare
* Extract
* Rewrite
* Generate
* Analyze
* Translate

---

### Why a Clear Task Matters

Consider:

```text
Analyze this resume.
```

This is ambiguous.

Analyze **what**?

The model might discuss:

* Formatting
* Skills
* Grammar
* Experience
* Projects
* ATS compatibility
* Overall quality

Now make the task specific:

```text
Analyze this resume for a Data Analyst position
and identify the three biggest weaknesses.
```

Now the desired action is much clearer.

### Mental Model

```text
Vague Task
    ↓
More possibilities
    ↓
More model inference
    ↓
Less predictable output
```

```text
Specific Task
    ↓
Fewer possibilities
    ↓
Less inference
    ↓
More predictable output
```

---

## Context

### What Is Context?

**Context is additional information that helps the AI perform the task correctly.**

Example:

```text
Analyze this resume for a Data Analyst position.
```

This is useful, but the model still doesn't know:

* Is the candidate a fresher?
* How much experience do they have?
* Which company are they targeting?
* Is the target company a startup or large company?
* What level is the role?

Add context:

```text
The candidate is a fresher
applying for an entry-level Data Analyst position.
```

Now the model has more information to work with.

### Definition

> **Context = relevant information provided to the model so it can perform the task more effectively.**

---

### Context Can Change the Answer

Suppose two candidates have the same resume.

#### Candidate A

```text
Fresh graduate
Applying for an entry-level role
```

#### Candidate B

```text
8 years of experience
Applying for a senior role
```

The weaknesses in their resumes should not necessarily be evaluated in the same way.

Therefore:

> **Context changes how the task should be interpreted.**

This is especially important when building AI applications where the model needs information about the user, business, task, or environment.

---

## Rules / Constraints

### What Are Rules?

Rules tell the AI:

> **What it should and should not do.**

Examples:

```text
Use simple English.
```

```text
Do not rewrite the resume.
```

```text
Find only three weaknesses.
```

```text
Do not invent information.
```

```text
Do not offer a refund.
```

```text
Use only the attached company policy.
```

Rules reduce unwanted behavior and make the output more controlled.

---

## Example: Customer Complaint

Suppose a customer complains:

> "My order arrived three days late."

We want the AI to write a response.

### Task

```text
Write a reply to the customer.
```

### Context

```text
The customer's order arrived three days late.
```

### Rules

```text
Be polite.
Do not argue with the customer.
Do not offer a refund.
```

### Output format

```text
Maximum 100 words.
```

Now the AI has much less ambiguity.

The conceptual structure is:

```text
Task
 ↓
Write a reply

Context
 ↓
Order arrived 3 days late

Rules
 ↓
Be polite
No refund
No argument

Output
 ↓
Maximum 100 words
```

---

## Output Format

The final component is:

> **What should the answer look like?**

Don't leave the output format completely up to the model when your application requires a specific structure.

For example:

```text
Write Python code that adds two numbers.
```

is better than:

```text
Write code that adds two numbers.
```

because the programming language is specified.

Other output requirements can include:

* Number of points
* Word limit
* JSON
* Markdown
* Table
* Bullet points
* Specific fields
* Specific sections
* Programming language

---

## Complete Prompt Example

A strong prompt can therefore look like:

```text
TASK:
Analyze the resume for a Data Analyst position.

CONTEXT:
The candidate is a fresher applying for an
entry-level Data Analyst role.

RULES:
1. Identify only the three biggest weaknesses.
2. Use simple English.
3. Do not invent information.
4. Do not rewrite the resume.

OUTPUT:
For each weakness provide:
- Problem
- Why it matters
- How to improve it

Also provide an overall score out of 100.
```

This is much more reliable than:

```text
Analyze this resume.
```

---

## The "Make This Better" Problem

Consider this prompt:

```text
Make this better.
```

This is a weak prompt.

Why?

Because **better** can mean many things:

* Improve grammar
* Make it shorter
* Make it longer
* Make it more professional
* Make it clearer
* Make it more persuasive
* Simplify it
* Change the tone

The AI doesn't know which meaning you intend.

### Better approach

Specify:

```text
Rewrite this email to make it more professional.
Keep it under 100 words.
Preserve the original meaning.
Use a polite and confident tone.
```

Now:

```text
Task       → Rewrite
Context    → Existing email
Rules      → Preserve meaning + professional tone
Output     → Under 100 words
```

---

## Prompt Anatomy

A useful prompt framework from the tutorial contains **five components**:

```text
1. TASK
2. CONTEXT / INPUT
3. CONSTRAINTS / RULES
4. OUTPUT FORMAT
5. EXAMPLES (Optional)
```

### Important

Not every prompt requires all five.

For example:

```text
Translate "Good Morning" into Hindi.
```

doesn't need a complicated structure.

The goal is **clarity**, not unnecessary complexity.

---

## Examples Are Optional

Sometimes you can provide an example of the output you want.

For example:

```text
Return the answer in this format:

Problem:
Why it matters:
How to improve:
```

An example can help the model understand the expected pattern.

But don't automatically add examples, personas, tones, and elaborate frameworks to every prompt.

> **Use additional prompt components when they solve an actual problem.**

---

## Don't Over-Engineer Simple Prompts

Suppose your task is:

```text
Translate "Good Morning" into Hindi.
```

You don't need:

```text
TASK:
...

CONTEXT:
...

RULES:
...

OUTPUT:
...

PERSONA:
...

OBJECTIVE:
...

TONE:
...
```

That's unnecessary.

The engineering mindset is:

> **Use as much structure as needed — but no more than necessary.**

The tutorial explicitly emphasizes avoiding unnecessary structure.

---

## Delimiters

When prompts contain multiple types of information, it can become difficult to distinguish:

* Instructions
* User data
* Context
* Questions
* Documents

**Delimiters** help separate these sections.

Examples:

```text
### TASK
Analyze the resume.

### RESUME
John Doe
Python
SQL
...

### OUTPUT
Return three weaknesses.
```

Or:

```text
"""
Resume content goes here
"""
```

Other possibilities include:

```text
<resume>
...
</resume>
```

```text
--- RESUME ---
...
--- END RESUME ---
```

The exact delimiter is less important than **consistent separation**.

---

### Why Delimiters Help

Without clear separation:

```text
Task + User Data + Rules + Question
```

can become one large block of text.

With delimiters:

```text
TASK
 ↓
Clearly separated

DATA
 ↓
Clearly separated

RULES
 ↓
Clearly separated

QUESTION
 ↓
Clearly separated
```

This makes the prompt easier for both humans and models to interpret.

---

## Example: Policy Question

Suppose a company policy says:

```text
Annual Leave: 20 days
Casual Leave: 10 days
```

Now we ask:

```text
How many maternity leave days are provided?
```

If the policy doesn't mention maternity leave, the model shouldn't invent an answer.

A better prompt can specify:

```text
TASK:
Answer the employee's question.

RULES:
- Use only the attached company policy.
- If the information is missing, respond "Not found."

POLICY:
Annual Leave: 20 days
Casual Leave: 10 days

QUESTION:
How many maternity leave days are provided?
```

Expected behavior:

```text
Not found.
```

This is a very important application of constraints and grounding.

---

## Structured Prompting

A **structured prompt** organizes instructions into clear sections.

Instead of:

```text
Analyze this resume and tell me problems
and score it and don't be too long and the
candidate is a fresher and return three points.
```

use:

```text
TASK:
Analyze the resume for a Data Analyst role.

CONTEXT:
The candidate is a fresher.

RULES:
- Find only three important problems.
- Use simple English.
- Do not invent information.

OUTPUT:
- Score out of 100.
- For each problem:
  - Problem
  - Why it matters
  - How to fix it
```

The second version is easier to:

* Read
* Debug
* Modify
* Test
* Maintain
* Reuse

---

### Structured Prompt ≠ Fancy Formatting

Using:

```text
### TASK
```

doesn't magically make a prompt better.

You could use:

```text
TASK:
```

or:

```text
<task>
...
</task>
```

or another consistent structure.

The important thing is:

> **Logical organization and clear separation.**

Not the specific symbol or formatting style.

---

## Prompt Chaining

Some tasks are too complex to give to an LLM as one huge instruction.

Example:

```text
Analyze resume
↓
Find skills
↓
Find missing skills
↓
Score candidate
↓
Suggest projects
↓
Generate interview questions
↓
Create study plan
```

That's a lot of work for one prompt.

Instead, break it into multiple steps.

This is called **Prompt Chaining**.

---

### How Prompt Chaining Works

Suppose we have a resume.

#### Step 1

```text
Extract the candidate's skills.
```

Output:

```text
Python
SQL
Excel
Power BI
```

#### Step 2

Use Step 1's output:

```text
Find missing skills for a Data Analyst role.
```

Input:

```text
Candidate skills:
Python
SQL
Excel
Power BI
```

Output:

```text
Statistics
Tableau
...
```

#### Step 3

Use previous results:

```text
Generate interview questions based on
the candidate's skills and missing skills.
```

So:

```text
Resume
  ↓
Prompt 1
  ↓
Skills
  ↓
Prompt 2
  ↓
Missing Skills
  ↓
Prompt 3
  ↓
Interview Questions
```

This is a **chain**.

---

### Why Use Prompt Chaining?

Complex tasks can be divided into smaller, easier-to-manage tasks.

Benefits:

#### 1. Easier debugging

If something goes wrong, you can identify which step failed.

#### 2. Better control

Each prompt can have a specific responsibility.

#### 3. Easier testing

Each step can be evaluated independently.

#### 4. Potentially better outputs

Instead of asking one model call to solve a huge problem, each call focuses on one task.


### Prompt Chaining Has a Downside

More steps usually mean:

```text
More LLM Calls
      ↓
More Time
      ↓
More Cost
```

There is another important problem:

#### Error Propagation

Suppose:

```text
Step 1 → Wrong Output
          ↓
Step 2 uses wrong output
          ↓
Step 3 uses wrong output
          ↓
Final result is wrong
```

One error can propagate through the entire chain.

This is called:

> **Error Propagation**

---

## Prompt Testing

A prompt that works once is **not necessarily production-ready**.

Suppose you build a customer-support classifier.

Categories:

```text
Billing
Technical
Cancellation
Refund
```

Test:

```text
"I was charged twice."
```

The model correctly returns:

```text
Billing
```

Good — but one test isn't enough.

---

### Test Different Types of Inputs

You should test:

#### Normal Cases

Expected, common inputs.

```text
"I was charged twice."
```

#### Edge Cases

Unusual but valid inputs.

#### Confusing Cases

Inputs that could reasonably belong to multiple categories.

#### Missing Information

Inputs where required information is absent.

#### Very Large Inputs

Large documents/messages.

#### Bad Inputs

Malformed or poor-quality input.

#### Unexpected Inputs

Inputs outside what you originally expected.

---

### Measuring Prompt Performance

Suppose you test a prompt 100 times.

Results:

```text
Correct → 87
Incorrect → 13
```

Then:

```text
Accuracy = 87 / 100 = 87%
```

The important lesson is:

> **Evaluate prompts using test cases and measurable results instead of judging them by one impressive response.**

A beginner may say:

> "This prompt looks good."

An engineer asks:

> "How many test cases does this prompt pass?"

---

### Test Before Trust

A key takeaway from the lecture:

> **Test before trust.**

Don't trust a prompt merely because:

* It produced one good answer.
* It looks well written.
* Someone online recommended it.
* The output sounds convincing.

Instead:

```text
Prompt
 ↓
Test
 ↓
Measure
 ↓
Improve
 ↓
Test Again
 ↓
Trust
```

This is especially important when building AI products.

---

## Structured Prompting + Chaining + Testing

These three concepts work together.

### Structured Prompting

Makes the prompt:

* Clear
* Organized
* Easier to debug

### Prompt Chaining

Breaks complex tasks into:

* Smaller steps
* Multiple model calls

### Prompt Testing

Checks:

* Whether the system actually works
* How often it succeeds
* Where it fails

Together:

```text
STRUCTURE
    ↓
Clear prompt
    ↓
CHAIN
    ↓
Complex task divided into steps
    ↓
TEST
    ↓
Measure performance
    ↓
IMPROVE
```

---


## Important Definitions

### What is Prompt Engineering?

> **Prompt engineering is the process of designing, testing, evaluating, and improving prompts to reliably obtain desired outputs from an AI model.**

### What is a Structured Prompt?

> **A structured prompt organizes instructions into clear sections such as task, context, rules, input, and output requirements.**

### What is Prompt Chaining?

> **Prompt chaining is breaking a complex task into multiple smaller LLM steps, where the output of one step can be used as input to a subsequent step.**

### What is Prompt Testing?

> **Prompt testing is evaluating a prompt across different test cases and measuring how reliably the AI produces the expected output.**

---

## Complete Prompt Engineering Workflow

The entire process can be remembered as:

```text
                 ┌──────────────┐
                 │ Define Task  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Add Context  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Add Rules    │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Define Output│
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Run Prompt   │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Test Output  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Find Issues  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ Improve      │
                 └──────┬───────┘
                        ↓
                   Test Again
```

For complex tasks:

```text
Complex Task
     ↓
Prompt Chain
     ↓
Step 1 → Step 2 → Step 3
     ↓
Test Each Step
```

---

## Practical Prompt Template

A reusable template:

```text
TASK:
[What exactly should the AI do?]

CONTEXT:
[What information does the AI need?]

RULES / CONSTRAINTS:
[What should it do or avoid?]

INPUT:
[The actual data/document/text]

OUTPUT FORMAT:
[How should the answer be structured?]

EXAMPLE:
[Optional example of desired output]
```

### Example

```text
TASK:
Analyze the resume for an entry-level Data Analyst role.

CONTEXT:
The candidate is a fresher.

RULES:
- Identify only the three biggest weaknesses.
- Use simple English.
- Do not invent information.
- Do not rewrite the resume.

INPUT:
[Resume content]

OUTPUT:
For each weakness provide:
1. Problem
2. Why it matters
3. How to improve it

Also provide an overall score out of 100.
```

---

## Common Mistakes

### Mistake 1: Vague Task

```text
Make this better.
```

#### ✅ Better

```text
Rewrite this email to make it more professional
while preserving its original meaning.
```

---

### Mistake 2: Missing Context

```text
Analyze this resume.
```

#### ✅ Better

```text
Analyze this resume for an entry-level Data Analyst role.
The candidate is a fresher.
```

---

### Mistake 3: No Constraints

If you don't specify limitations, the model may produce more or different information than you need.

#### ✅ Better

```text
Identify only three weaknesses.
Do not rewrite the resume.
```

---

### Mistake 4: No Output Format

```text
Analyze the resume.
```

#### ✅ Better

```text
For each weakness provide:
- Problem
- Why it matters
- How to fix it
```

---

### Mistake 5: Trusting One Good Response

One successful response does not prove reliability.

#### ✅ Better

Test:

```text
Normal cases
Edge cases
Confusing cases
Missing information
Large inputs
Bad inputs
Unexpected inputs
```

---

### Mistake 6: Over-Engineering

Don't create a huge structured prompt for:

```text
Translate "Hello" to Hindi.
```

Use complexity only when complexity is useful.

---

## Important Concepts at a Glance

| Concept                | Simple Meaning                                                 |
| ---------------------- | -------------------------------------------------------------- |
| **Prompt**             | Instruction/information given to an AI model                   |
| **Prompting**          | Asking an AI to perform a task                                 |
| **Prompt Engineering** | Designing, testing, and improving prompts for reliable results |
| **Task**               | What the AI should do                                          |
| **Context**            | Information needed to perform the task properly                |
| **Constraint/Rule**    | What the AI should or should not do                            |
| **Output Format**      | How the answer should be structured                            |
| **Delimiter**          | Marker used to separate different parts of a prompt            |
| **Structured Prompt**  | Prompt organized into logical sections                         |
| **Prompt Chaining**    | Breaking a complex task into multiple LLM steps                |
| **Prompt Testing**     | Testing prompts against multiple cases                         |
| **Error Propagation**  | An early error affecting later steps in a chain                |

---

