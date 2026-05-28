def test_query_endpoint_returns_answer_and_citations(test_client) -> None:
    response = test_client.post(
        "/api/v1/query",
        json={"query": "DocuGuard", "corpus_text": "DocuGuard is a secure internal knowledge hub."},
    )
    assert response.status_code == 200
    body = response.json()
    assert "answer" in body
    assert "citations" in body
