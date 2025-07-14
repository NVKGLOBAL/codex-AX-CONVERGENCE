# Recursive Codex Query Engine — Specification

## 1. Overview
The Engine accepts symbolic queries against the Codex and returns structured, context-aware responses.

## 2. Use Cases
- Query a single entry by ID or tag.
- List available concepts in the ontology.
- Resolve semantic paths between two concepts.
- Trigger an "echo" whisper for reflection.

## 3. API Endpoints

### 3.1. `GET /v1/entries`
List all entries.

- Query Parameters:
  - `limit` (integer, optional) — max entries to return.
  - `tag` (string, optional) — filter by semantic tag.

- Response (JSON):
```json
{
  "version": "1.0",
  "entries": [
    { 
      "id": "entry_081", 
      "title": "codex-is-a-program", 
      "tags": ["meta", "self-reflection"],
      "created_at": "2025-07-14T12:00:00Z"
    },
    {
      "id": "entry_082",
      "title": "symbolic-query-architecture",
      "tags": ["architecture", "query"]
    }
  ]
}
