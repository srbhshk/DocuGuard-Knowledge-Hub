from pathlib import Path


def test_local_dev_compose_files_exist() -> None:
    root = Path(__file__).resolve().parents[2]
    assert (root / "infra/docker-compose.yml").exists()
    assert (root / "infra/docker-compose.dev.yml").exists()
