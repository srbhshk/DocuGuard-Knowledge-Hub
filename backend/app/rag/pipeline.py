from pydantic import BaseModel

from app.rag.chunker import chunk_text
from app.rag.embedder import Embedder
from app.rag.generator import Generator
from app.rag.retriever import Retriever


class QueryRequest(BaseModel):
    query: str
    corpus_text: str


class QueryResponse(BaseModel):
    answer: str
    citations: list[str]


class RagPipeline:
    def __init__(self) -> None:
        self.embedder = Embedder()
        self.retriever = Retriever()
        self.generator = Generator()

    def run(self, request: QueryRequest) -> QueryResponse:
        chunks = list(chunk_text(request.corpus_text))
        # TODO(sprint-2): persist embeddings to Qdrant once vector storage is wired.
        _ = [self.embedder.embed(chunk) for chunk in chunks]
        retrieved = self.retriever.retrieve(request.query, chunks)
        answer = self.generator.generate(request.query, retrieved)
        citations = [item.source_id for item in retrieved]
        return QueryResponse(answer=answer, citations=citations)
