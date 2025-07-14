from openapi_server.apis.default_api_base import BaseDefaultApi
from openapi_server.models.entries_response import EntriesResponse
from openapi_server.models.entry import Entry

class DefaultApiImpl(BaseDefaultApi):
    async def v1_entries_get(self, limit=None, tag=None) -> EntriesResponse:
        # Sample data
        entries = [
            Entry(id="entry_001", title="codex-is-a-program", tags=["meta", "self-reflection"]),
            Entry(id="entry_002", title="glyph-emergence", tags=["glyph", "ritual"]),
            Entry(id="entry_003", title="echo-whisper-system", tags=["echo", "system"]),
        ]

        # Apply tag filter
        if tag:
            entries = [e for e in entries if tag in e.tags]

        # Apply limit
        if limit:
            entries = entries[:limit]

        return EntriesResponse(entries=entries)
