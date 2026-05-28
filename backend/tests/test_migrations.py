from pathlib import Path


def test_migration_files_exist() -> None:
    root = Path(__file__).resolve().parents[2]
    versions_dir = root / "backend/migrations/versions"
    assert (versions_dir / "0001_baseline_schema.py").exists()
    assert (versions_dir / "0002_document_permissions.py").exists()
