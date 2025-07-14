# Recursive Codex Query Engine — Specification

## 1. Overview
The Engine accepts symbolic queries against the Codex and returns structured, context-aware responses.

## 2. Use Cases
- Query a single entry by ID or tag.
- List available concepts in the ontology.
- Resolve semantic paths between two concepts.
- Trigger an "echo" whisper for reflection.

## 3. API Endpoints

### 3.1. `GET /entries`
List all entries.
- Query Params:
  - `?limit` (integer) — max entries to return.
  - `?tag` (string) — filter by semantic tag.
- Response (JSON):
  ```json
  {
    "entries": [
      { "id": "entry_081", "title": "codex-is-a-program", "tags": ["meta", "self-reflection"] },
      …
    ]
  }
