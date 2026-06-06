# Model Approach

## Overview

The chatbot is designed to provide evidence-based exercise, hydration, nutrition, and recovery guidance for athletes recovering from heat stress.

## Workflow Diagram

```mermaid
flowchart TD

A[User asks a question]
--> B[Convert question into embedding vector]

B --> C[Compare with saved example-question embeddings]

C --> D[Calculate cosine similarity]

D --> E{Closest matching category}

E -->|Exercise| F[Exercise Guidance]

E -->|Hydration| G[Hydration Guidance]

E -->|Diet| H[Diet and Recovery Nutrition]

E -->|Cooling| I[Cooling Strategies]

E -->|Symptoms| J[Warning Symptoms]

F --> K[Return evidence-based response]
G --> K
H --> K
I --> K
J --> K

K --> L[Display chatbot reply]
```

## Categories

- Exercise Guidance
- Hydration Guidance
- Diet and Recovery Nutrition
- Cooling Strategies
- Warning Symptoms

## Embedding Model

The chatbot uses a lightweight embedding model to convert user questions into vector representations.

## Similarity Matching

Cosine similarity is used to compare user questions against stored example-question embeddings.

## Response Strategy

Responses are retrieved from evidence extracted from peer-reviewed literature and professional guidelines rather than unrestricted text generation.
