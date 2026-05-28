from fastapi import APIRouter

from app.rag.pipeline import QueryRequest, QueryResponse, RagPipeline

router = APIRouter(prefix="/query", tags=["query"])
pipeline = RagPipeline()


@router.post("", response_model=QueryResponse)
async def run_query(request: QueryRequest) -> QueryResponse:
    return pipeline.run(request)
