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


@pytest.fixture(scope="module", params=[{"name": "test_string"} for _ in range(3)])
def json_data(request):
    return request.param


@pytest.fixture(scope="module")
def expected_status():
    return 200


@pytest.fixture(scope="module", params=["/api/v1/skills/", "/api/v1/professions/"])
def endpoint_urls(request):
    return request.param


@pytest.mark.asyncio
async def test_add_skill(test_client: AsyncClient, endpoint_urls, json_data, expected_status):
    response = await test_client.post(endpoint_urls, json=json_data)
    assert response.status_code == expected_status


@pytest.fixture(scope="module", params=[("limit=1", 1), ("limit=2", 2), ("", 3)])
def expected_len(request):
    return request.param


@pytest.mark.asyncio
async def test_get_sp(test_client: AsyncClient, endpoint_urls, expected_len, expected_status):
    response = await test_client.get(endpoint_urls, params=expected_len[0])
    assert response.status_code == expected_status
    assert len(response.json()) == expected_len[1]