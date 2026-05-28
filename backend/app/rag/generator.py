from app.rag.retriever import RetrievedChunk


class Generator:
    """Minimal answer synthesizer for initial custom pipeline."""

    def generate(self, query: str, chunks: list[RetrievedChunk]) -> str:
        if not chunks:
            return f"No relevant context found for: {query}"
        context = " | ".join(chunk.chunk[:120] for chunk in chunks)
        return f"Query: {query}\nAnswer (draft): {context}"
