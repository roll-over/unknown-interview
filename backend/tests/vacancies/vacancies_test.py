from random import randint
from typing import Callable

import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.fixture
def payment_values() -> Callable[[int], dict]:
    def _payment_values(max_payment_value: int) -> dict:
        v1 = randint(2, max_payment_value)
        v2 = v1 - randint(1, v1 - 1)
        return {"u_bound": v1, "l_bound": v2}
    return _payment_values


@pytest.fixture
def create_json(payment_values: Callable[[int], dict]) -> dict:
    p_values = payment_values(9999999)
    return {
    "title": "lead",
    "salary": {
        "min_level": p_values["l_bound"],
        "max_level": p_values["u_bound"],
        "currency": "USD"
    },
    "grade": "middle",
    "profession": {
        "name": "Backend Developer",
    },
    "skillset": [
        {
            "name": "Python",
        },
        {
            "name": "Django"
        }
    ],
    "extra_info": "I read reddit a lot."
    }


@pytest.mark.asyncio
async def test_unauthorized_post(test_client: AsyncClient, create_json: dict):
    response = await test_client.post("/api/v1/vacancies/", json=create_json)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_unauthorize_patch(test_client: AsyncClient):
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.patch(f"/api/v1/vacancies/{vacancy_id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_nothing(test_client: AsyncClient, no_db_entries_error: bytes):
    response = await test_client.get("/api/v1/vacancies/random_vacancy")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert no_db_entries_error in response.content


@pytest.mark.asyncio
async def test_get_random_nothing(test_client: AsyncClient, no_db_entries_error: bytes):
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.get(f"/api/v1/vacancies/{vacancy_id}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert no_db_entries_error in response.content