from collections.abc import Iterable


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> Iterable[str]:
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        yield text[start:end]
        if end == len(text):
            break
        start = end - overlap
