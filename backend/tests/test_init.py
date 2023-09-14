import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_ping(test_client: AsyncClient):
    response = await test_client.get("/api/ping")
    assert response.status_code == 200
    assert response.json() == "pong"


@pytest.mark.asyncio
async def test_all_users(test_client: AsyncClient):
    response = await test_client.get("api/v1/users/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_note(test_client: AsyncClient):
    data = {
        "related_id": "3fa85f64-5717-4562-b3fc-2c963f66afb7",
        "note_text": "Test note",
    }
    response = await test_client.post("api/v1/cv_note/", json=data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_note(test_client: AsyncClient):
    test_id = "3fa85f64-5717-4562-b3fc-2c963f66afb7"
    response = await test_client.get("api/v1/cv_note/{cv_id}".format(cv_id=test_id))
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_skill(test_client: AsyncClient):
    params = {
        "limit": 5
    }
    response = await test_client.get("/api/v1/skills/", params=params)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_skill(test_client: AsyncClient):
    data = {
        "name": "test_string"
    }
    response = await test_client.post("/api/v1/skills/", json=data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_profession(test_client: AsyncClient):
    params = {
        "limit": 5
    }
    response = await test_client.get("/api/v1/professions/", params=params)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_add_profession(test_client: AsyncClient):
    data = {
        "name": "test_string"
    }
    response = await test_client.post("/api/v1/professions/", json=data)
    assert response.status_code == 200