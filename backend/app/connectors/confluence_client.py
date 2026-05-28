from typing import Any

import httpx


class ConfluenceClient:
    """Prototype client for Confluence document ingestion."""

    def __init__(self, base_url: str, api_token: str, email: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_token = api_token
        self.email = email

    async def list_pages(self, space_key: str, limit: int = 25) -> dict[str, Any]:
        url = f"{self.base_url}/wiki/rest/api/content"
        params = {"spaceKey": space_key, "limit": limit, "expand": "body.storage,version"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params, auth=(self.email, self.api_token))
            response.raise_for_status()
            return response.json()

    async def get_page(self, page_id: str) -> dict[str, Any]:
        url = f"{self.base_url}/wiki/rest/api/content/{page_id}"
        params = {"expand": "body.storage,version"}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(url, params=params, auth=(self.email, self.api_token))
            response.raise_for_status()
            return response.json()
