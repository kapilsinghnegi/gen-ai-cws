# Generative AI — Working with LLM APIs

## The Basic LLM API Architecture

Suppose the user enters:

```text
Explain Machine Learning in simple language.
```

The architecture is:

```text
User
 │
 ▼
Python Application
 │
 │ API Request
 ▼
Gemini API
 │
 ▼
Gemini Model
 │
 │ Generated Response
 ▼
Gemini API
 │
 ▼
Python Application
 │
 ▼
User
```

The application sends a **request** and receives a **response**.

That communication is what we call an **API call**.

---

#### What Is an API Call?

> **An API call is a request sent by your application to an external service, followed by a response from that service.**

#### Why Use an API?

Without an API, your application doesn't automatically have access to a hosted LLM such as Gemini.

The API provides a controlled interface through which your application can communicate with the model.

The exact SDK and API syntax differs for different API providers, but the underlying architecture is similar.

We'll use Gemini primarily because it provides an accessible/free tier suitable for learning.

---

## Google Gen AI Python SDK
### [Installation](https://googleapis.github.io/python-genai/)

```bash
pip install google-genai
```
With uv:
```bash
uv pip install <package>
```

---

### API Keys

Most hosted LLM APIs require authentication.

An **API key** is a credential that allows your application to access the provider's API.

The provider uses the key to identify/authenticate the API request and apply usage limits/billing policies.

> Note: Never Hard-Code API Keys. Store them outside your source code in an environment variable, then retrieve it from your application.

---

#### Why API Key Security Matters

If an API key becomes public:

* Someone can make API calls using your credentials.
* Your quota can be consumed.
* Your account may incur charges.
* The key may need to be revoked and replaced.

Therefore:

> **API keys are secrets and should be treated like passwords.**

---

### Environment Variables

An environment variable allows configuration/secrets to exist outside your source code.

Python can read it using:

```python
import os

api_key = os.getenv("GEMINI_API_KEY")
```

You can then use the key through the SDK/client configuration.

#### Important

Never print the actual secret merely to verify that it exists.

Instead, check whether it is present:

```python
if api_key:
    print("API key found")
else:
    print("API key not found")
```

---

## First LLM API Program

The basic flow is:

```text
1. Import SDK
      ↓
2. Create client
      ↓
3. Select model
      ↓
4. Send prompt
      ↓
5. Receive response
      ↓
6. Extract generated text
```

Conceptually:

```python
client = ...
response = client.generate(...)

print(response.text)
```

The exact syntax depends on the SDK/version being used.

---

### What Is an SDK?

SDK = **Software Development Kit**

An SDK provides tools/libraries that make it easier for developers to interact with a service.

Instead of manually constructing every HTTP request, authentication header, request body, and response parser, an SDK can provide convenient functions/classes.

#### Without an SDK

Conceptually:

```text
Python
 ↓
HTTP Request
 ↓
API Endpoint
 ↓
JSON Response
 ↓
Parse Response
```

#### With an SDK

```text
Python
 ↓
SDK
 ↓
API
 ↓
Model
```

The SDK handles much of the communication complexity for you.

---

### Client Object

Think of the client as an object that represents your application's connection/interface to the AI service.

Conceptually:

```python
client = ...
```

Then you use the client to make requests:

```python
response = client....
```

This is a useful abstraction when working with APIs.

---

### Model Selection

An LLM provider may expose multiple models.

For example:

```text
Provider
│
├── Fast model
├── More capable model
├── Reasoning model
├── Multimodal model
└── Specialized model
```

Your application needs to specify which model should process the request.

---

#### What Does "Model" Mean?

In AI engineering, **model** means the trained AI system responsible for processing the input and generating the output.

For example:

```text
Prompt
  ↓
Gemini Model
  ↓
Response
```

A provider can offer several models with different:

* Capabilities
* Speed
* Context limits
* Costs
* Hardware requirements
* Input/output modalities

Therefore:

> **Choosing a model is an engineering decision, not just a coding detail.**

---

### The Complete API Flow

```text
             YOUR APPLICATION
                    │
                    │ Prompt
                    ▼
               API / SDK
                    │
                    ▼
              LLM PROVIDER
                    │
                    ▼
                AI MODEL
                    │
                    │ Generated output
                    ▼
               API / SDK
                    │
                    ▼
             YOUR APPLICATION
                    │
                    ▼
                  USER
```

---

## Hosted Model vs Local Model

Until now, the model was hosted remotely.

### Hosted LLM

```text
Your Computer
     │
     │ Internet
     ▼
Provider's Servers
     │
     ▼
LLM
```

Examples:

* Gemini API
* OpenAI API
* Claude API

Your computer sends the request and receives the response.

---

### What Is a Local Model?

A **local model** is an AI model that runs on your own machine rather than sending every request to a remote provider.

### Hosted

```text
Your App
   ↓ Internet
Cloud Provider
   ↓
LLM
   ↓
Response
```

### Local

```text
Your App
   ↓
Local Runtime
   ↓
Local LLM
   ↓
Response
```

---

### Why Run a Model Locally?

Potential advantages include:

#### Privacy

Data can remain on your machine instead of being sent to a third-party API.

#### Offline capability

A sufficiently capable local setup can work without an internet connection after the model is downloaded.

#### Cost

You don't necessarily pay a provider per API request.

#### Control

You have greater control over the model/runtime.

However, local models also have trade-offs:

* Hardware requirements
* RAM/VRAM usage
* Storage requirements
* Speed
* Model capability
* Setup complexity

---

### Ollama

> **Ollama is software/runtime that makes it easier to download and run compatible AI models locally.**

#### Ollama vs Model

This distinction is extremely important.

##### Ollama

**What it is:** Runtime/software.

##### Model

**What it is:** AI model.

Ollama provides the environment/runtime; the model provides the intelligence.

---

### Gemma (Local Model)

Gemma is a family of AI models designed to be deployable in relatively resource-constrained environments compared with very large hosted models.

We'll choose a smaller model for experimentation because larger models require substantially more:

* RAM
* Storage
* Processing power

---

#### Model Size and Parameters

Models are often described using parameter counts.

Examples:

```text
270M
1B
4B
12B
27B
```

Where:

```text
M = Million
B = Billion
```

For example:

```text
1B parameters
≈ 1 billion learned numerical parameters
```

---

#### What Are Model Parameters?

A model contains learned numerical values called **parameters**.

During training, the model adjusts these values so that it becomes better at its task.

A simplified mental model:

```text
Training Data
     ↓
Neural Network
     ↓
Learned Parameters
     ↓
Trained Model
```

During inference, those learned parameters are used to generate predictions/output.

You don't need to understand the underlying mathematics yet.

> **Parameters are learned numerical values inside the model that encode patterns learned during training.**

---

### Bigger Model ≠ Automatically Better for Every Situation

A larger model may have greater capability, but it also tends to require more resources.

For example:

```text
Small Model
↓
Less RAM
Less Storage
Lower Compute Requirement
Potentially Faster

Large Model
↓
More RAM
More Storage
More Compute
Potentially Higher Capability
```

Therefore:

> **Choose a model based on the application's requirements, not simply by choosing the largest model available.**

---

### Running a Local Model

The basic local-model workflow is:

```text
Install Ollama
      ↓
Download/Pull Model
      ↓
Run Model
      ↓
Send Prompt
      ↓
Receive Response
```

---

### Local LLM Through Python

#### Hosted vs Local

| Feature        | Hosted API                      | Local Model                       |
| -------------- | ------------------------------- | --------------------------------- |
| Model location | Provider's servers              | Your machine                      |
| Internet       | Usually required                | Not necessarily after setup       |
| API cost       | Usually usage-based             | No per-request provider fee       |
| Hardware       | Less demanding locally          | Requires suitable hardware        |
| Privacy        | Data sent to provider           | Can remain local                  |
| Setup          | Usually easier                  | More setup                        |
| Scaling        | Provider handles infrastructure | You manage infrastructure         |
| Model choice   | Provider-dependent              | Depends on available local models |

---

## Streaming

Now we move to one of the most important application-level concepts.

Suppose an LLM takes five seconds to generate an answer.

### Without streaming

```text
Request
   ↓
Wait...
   ↓
Wait...
   ↓
Wait...
   ↓
Complete response
   ↓
Display everything
```

The user sees nothing while waiting.

This can feel like the application is frozen.

---

### What Is Streaming?

**Streaming** means receiving and displaying the model's output incrementally as it is generated instead of waiting for the complete response.

#### Without streaming

```text
[Complete response]
```

#### With streaming

```text
[First chunk]
[Second chunk]
[Third chunk]
[Fourth chunk]
...
[Final chunk]
```

This is similar to how ChatGPT-like interfaces appear to type the response progressively.

---

### Why Streaming Matters

Streaming improves the **perceived responsiveness** of an application.

Instead of:

```text
Loading...
Loading...
Loading...
...
Huge answer appears
```

the user sees:

```text
Here is
how machine
learning
works...
```

as the model generates it.

#### Important

Streaming usually does **not** mean the model generates the answer faster.

It means:

> **The user receives partial output sooner.**

That improves the user experience.

---

### Streaming Architecture

```text
User Request
     ↓
LLM
     ↓
Chunk 1 ───→ UI
     ↓
Chunk 2 ───→ UI
     ↓
Chunk 3 ───→ UI
     ↓
Chunk 4 ───→ UI
     ↓
Final Chunk
```

Instead of waiting for:

```text
Complete Response
        ↓
        UI
```

---

### Events in a Stream

Streaming APIs may not send only plain text.

They can send different types of events, such as:

```text
Interaction started
Generation started
Text chunk
More text
Interaction completed
```

Therefore, the application often needs to inspect each incoming event and determine what it contains.

---

### What Is a Delta?

In streaming systems, **delta** generally represents the newly available piece of data since the previous update.

Example:

```text
Event 1 → "Machine"
Event 2 → " learning"
Event 3 → " is"
Event 4 → "..."
```

Each new piece can be treated as a delta.

So:

> **Delta = newly received incremental data.**

This is a very useful concept when working with streaming LLM responses.

---

### Why Check the Event Type?

A stream may contain more than visible text.

For example:

```text
Stream
├── Metadata
├── Tool-related information
├── Text
├── Other events
└── Completion event
```

If your UI only needs text, you should extract only the relevant text events.

Conceptually:

```python
for event in stream:
    if event contains text:
        print(text)
```

This prevents unrelated stream events from being displayed to the user.

---

### Flushing Output

When printing streaming content in a terminal, output can sometimes be buffered.

That means:

```text
Program receives text
        ↓
Output waits in buffer
        ↓
Terminal displays later
```

For a streaming experience, we want:

```text
Text arrives
   ↓
Display immediately
```

This is why the tutorial uses output flushing.

Conceptually:

```python
print(chunk, end="", flush=True)
```

```text
end=""
→ Don't automatically add a new line.

flush=True
→ Push the output immediately.
```

This helps create a real-time terminal streaming effect.

---

### Where Is Streaming Useful?

Streaming is especially useful when responses can take noticeable time.

Examples:

* AI chat applications
* AI interview platforms
* Coding assistants
* Long-form text generation
* Document analysis
* AI tutors
* Customer support assistants

#### Example

User asks:

> "Explain why my SQL query is wrong."

Instead of waiting for a 500-word answer:

```text
Loading...
```

you can show:

```text
Your query has three issues...

1. ...
2. ...
3. ...
```

as the response is generated.

---

## Generation Parameters

An LLM doesn't have to generate output using only default settings.

Many APIs allow developers to configure **generation parameters**.

These parameters influence how the model generates its response.

Two important parameters covered here are:

1. **Temperature**
2. **Maximum output tokens**

---

### Temperature

Temperature controls the amount of **randomness/variation** during generation.

#### Lower temperature

```text
Lower randomness
↓
More predictable
↓
More consistent outputs
```

#### Higher temperature

```text
Higher randomness
↓
More variation
↓
More creative/diverse outputs
```

This is a general mental model; exact behavior depends on the model/provider.

---

#### Temperature Example

Prompt:

```text
Give me a name for a coffee shop.
```

> With Lower temperature you may get more conventional answers and  Higher temperature you may get more varied answers.
**Temperature controls generation variability, not intelligence.**

---

#### Temperature Is Not a Smartness Setting

Temperature doesn't add knowledge to the model.

It changes how the model chooses among possible outputs.

A useful mental model:

```text
Low Temperature
→ "Stay closer to likely choices."

High Temperature
→ "Allow more variation among possible choices."
```

---

#### Temperature and Model Defaults

Different model providers may recommend different temperature ranges/defaults.

The tutorial notes that the current Gemini 3.x models recommend using the default temperature rather than blindly lowering it.

> **Check the documentation for the specific model you are using instead of assuming temperature behaves identically across every model.**

---

### Maximum Output Tokens

The second parameter is **maximum output tokens**.

It limits how many tokens the model can generate for the response.

Suppose:

```text
max_output_tokens = 100
```

This means the model should not generate more than approximately that many output tokens for that generation.

#### Important

```text
100 tokens ≠ 100 words
```

A token can be:

* A complete word
* Part of a word
* Punctuation
* Another piece of text

---

#### Why Maximum Output Tokens Matter

Imagine an AI interview feedback tool.

You only want:

```text
3–4 lines of feedback
```

You don't want the model generating:

```text
500 lines
```

Setting a maximum output token limit provides a safeguard.

#### Benefits

* Controls response length
* Controls resource usage
* Helps control API costs
* Prevents unnecessarily long outputs

---

#### Token Limit Is Not a Word Limit

This distinction is important.

Suppose:

```text
max_output_tokens = 50
```

Don't interpret this as:

> "Generate exactly 50 words."

Instead:

> **Limit the generated output to approximately 50 tokens.**

The exact number of words can vary significantly depending on the text.

---

#### Why Token Limits Matter in Production

Without output limits:

```text
User
 ↓
Very broad request
 ↓
Long response
 ↓
Many output tokens
 ↓
Higher cost
```

With limits:

```text
User
 ↓
Request
 ↓
Maximum output tokens = N
 ↓
Controlled response
```

This is particularly important when many users are making API calls.

---

## Cost Management

When using hosted LLM APIs, cost becomes an engineering concern.

The tutorial identifies four major factors:

1. Input tokens
2. Output tokens
3. Model pricing
4. Number of API calls

---

### Input Tokens

Everything you send to the model consumes input tokens.

For example:

```text
Prompt:
"Explain Python."
```

The text sent to the model contributes to input-token usage.

Large prompts can therefore increase cost.

---

### Output Tokens

Everything the model generates contributes to output-token usage.

For example:

```text
Prompt
  ↓
Model
  ↓
Long response
```

A longer response means more output tokens.

Depending on the provider/model, input and output tokens may have different prices.

---

### Number of API Calls

Even if each individual request is inexpensive, many requests can add up.

Example:

```text
1,000 users
×
20 API calls/user
=
20,000 API calls
```

At scale, seemingly small per-request costs can become significant.

---

### Model Price

Different models can have different prices.

Conceptually:

```text
Small/Cheap Model
       ↓
Lower cost

Large/Premium Model
       ↓
Higher cost
```

Therefore, don't automatically use the most expensive model for every task.

#### Engineering principle

> **Use the cheapest model that reliably meets the task's quality requirements.**

---

### Four Ways to Reduce LLM Costs

#### 1. Avoid unnecessarily huge prompts

Don't send information the model doesn't need.

#### 2. Limit unnecessary long responses

Use an appropriate output-token limit.

#### 3. Choose an appropriate model

Don't use a premium model when a smaller model performs the task adequately.

#### 4. Avoid unnecessary API calls

Don't repeatedly make the same request when the result can be reused or avoided.

These practices are especially important when building production AI applications.

---

### Cost Optimization Mental Model

```text
LLM Cost
   │
   ├── Input Tokens
   ├── Output Tokens
   ├── Model Price
   └── Number of API Calls
```

Therefore:

```text
Reduce unnecessary input
        +
Control output length
        +
Choose the right model
        +
Reduce unnecessary calls
        ↓
Lower cost
```

---

## Error Handling

What happens if an LLM API fails?

For example:

```text
User
 ↓
Your Application
 ↓
LLM API
 ↓
❌ Error
```

If your application doesn't handle the error:

```text
API Error
 ↓
Python Exception
 ↓
Application crashes
```

That's bad UX.

A production application should catch expected failures and respond appropriately.

---

### Basic Python Error Handling

Python provides:

```python
try:
    # risky operation
except Exception as e:
    # handle error
```

Conceptually:

```text
try
 ↓
Call LLM API
 ↓
Success → Process response

Failure
 ↓
except
 ↓
Handle error
```

---

### Why Use `try/except` Around API Calls?

API calls can fail because of:

* Invalid requests
* Authentication problems
* Missing/invalid API keys
* Rate limits
* Quota exhaustion
* Model/resource not found
* Provider-side failures
* Network problems
* Temporary service outages

You don't want one failed request to crash the entire application.

---

### Common HTTP/API Error Codes

The tutorial introduces several important status codes.

| Code    | General Meaning                       |
| ------- | ------------------------------------- |
| **400** | Bad Request                           |
| **401** | Unauthorized / Authentication problem |
| **404** | Resource not found                    |
| **429** | Rate limit / quota exceeded           |
| **500** | Internal server error                 |
| **503** | Service unavailable                   |

---

### Don't Handle Every Error the Same Way

A common beginner mistake is:

```python
except:
    print("Something went wrong")
```

This hides useful information.

Instead, identify important failure categories and respond appropriately.

For example:

```text
401
 ↓
Check API credentials

429
 ↓
Rate-limit handling / retry / reduce usage

500/503
 ↓
Temporary provider problem
```

The exact handling strategy depends on the application.

---

### Error Handling Is a UX Feature

Error handling isn't only about preventing crashes.

It also helps users understand what happened.

#### Bad UX

```text
Application crashed.
```

#### Better UX

```text
The AI service is temporarily unavailable.
Please try again in a moment.
```

The user doesn't need to see an enormous Python traceback.

---

### Error Handling and Reliability

A production AI application should be designed around the possibility that external services can fail.

Remember:

```text
Your Application
      ↓
External API
      ↓
Can fail
```

Therefore:

```text
API failure
   ↓
Catch error
   ↓
Log useful information
   ↓
Show safe user-facing message
   ↓
Optionally retry/fallback
```

This is a major difference between a demo and a production application.

---

## The Four Production Concerns

The tutorial specifically emphasizes four concepts from a **Generative AI engineer/job perspective**:

```text
1. Streaming
2. Parameters
3. Cost Management
4. Error Handling
```

These are not merely API syntax details.

They affect the quality and reliability of real applications.

---

## Putting Everything Together

A production-style LLM application can conceptually look like:

```text
                    USER
                      │
                      ▼
               YOUR APPLICATION
                      │
              ┌───────┴────────┐
              │                │
              ▼                ▼
          Prompt          Configuration
                               │
                       ┌───────┼────────┐
                       │       │        │
                       ▼       ▼        ▼
                  Temperature  Tokens  Model
                       │
                       ▼
                   LLM API
                       │
                  ┌────┴────┐
                  │         │
                Success    Error
                  │         │
                  ▼         ▼
              Streaming   Error
              Response    Handling
                  │
                  ▼
                  USER
```

And throughout the system:

```text
Cost Management
      ↓
Control tokens + model + API calls
```

---

## Important Questions

### 1. What is an LLM API?

An interface through which an application can send requests to an LLM service and receive generated responses.

### 2. What is an API call?

A request from one software system to another through an API, followed by a response.

### 3. What is an SDK?

A software development toolkit/library that simplifies interaction with a service or platform.

### 4. What is a local LLM?

An LLM that runs on your own machine/infrastructure rather than being accessed exclusively through a remote hosted API.

### 5. What is Ollama?

Software/runtime that makes it easier to run compatible AI models locally.

### 6. What is Gemma?

A family of AI models that can be run in suitable local environments and is used in the tutorial as a local-model example.

---

### 7. What is streaming in LLM applications?

Receiving generated output incrementally as it becomes available instead of waiting for the complete response.

### 8. Why is streaming useful?

It improves perceived responsiveness and user experience, especially for long responses.

### 9. What does temperature control?

The variability/randomness of generated output.

### 10. What are maximum output tokens?

A limit on the number of tokens the model can generate in its response.

### 11. What factors affect LLM API cost?

Primarily:

* Input tokens
* Output tokens
* Model pricing
* Number of API calls

### 12. Why should API keys not be hard-coded?

Because exposing them can allow unauthorized use and potentially cause unexpected costs or quota consumption.

### 13. Why use a virtual environment?

To isolate project-specific Python dependencies and prevent conflicts between projects.

---