from pathlib import Path


def test_ci_workflows_exist() -> None:
    root = Path(__file__).resolve().parents[2]
    assert (root / ".github/workflows/ci.yml").exists()
    assert (root / ".github/workflows/docker-build.yml").exists()
    assert (root / ".github/workflows/docs.yml").exists()
