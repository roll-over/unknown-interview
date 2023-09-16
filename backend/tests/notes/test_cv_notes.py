import pytest
from httpx import AsyncClient
from fastapi import status


@pytest.mark.asyncio
async def test_add_note(test_client: AsyncClient):
    data = {
        "related_id": "3fa85f64-5717-4562-b3fc-2c963f66afb7",
        "note_text": "Test note",
    }
    response = await test_client.post("api/v1/cv_note/", json=data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_get_note(test_client: AsyncClient):
    test_id = "3fa85f64-5717-4562-b3fc-2c963f66afb7"
    response = await test_client.get("api/v1/cv_note/{cv_id}".format(cv_id=test_id))
    assert response.status_code == status.HTTP_200_OK
