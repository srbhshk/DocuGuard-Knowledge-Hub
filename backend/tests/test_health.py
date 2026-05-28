from fastapi.testclient import TestClient

def test_healthcheck(test_client: TestClient) -> None:
    response = test_client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
