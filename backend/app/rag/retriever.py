from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    chunk: str
    score: float
    source_id: str


class Retriever:
    """Simple lexical retriever placeholder."""

    def retrieve(self, query: str, chunks: list[str], k: int = 3) -> list[RetrievedChunk]:
        ranked = sorted(
            chunks,
            key=lambda chunk: sum(1 for token in query.split() if token.lower() in chunk.lower()),
            reverse=True,
        )
        return [
            RetrievedChunk(chunk=chunk, score=float(k - idx), source_id=f"local-{idx}")
            for idx, chunk in enumerate(ranked[:k])
        ]
