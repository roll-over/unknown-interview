import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ping(test_client: AsyncClient):
    response = await test_client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == "pong"
