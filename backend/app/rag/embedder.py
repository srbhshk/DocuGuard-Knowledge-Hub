class Embedder:
    """Deterministic placeholder embedder for initial pipeline wiring."""

    def embed(self, text: str) -> list[float]:
        seed = sum(ord(c) for c in text) % 1000
        return [float(seed), float(len(text))]
