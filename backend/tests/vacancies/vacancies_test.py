from random import choice, choices, randint
from string import ascii_letters

import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.fixture
def random_string():
    def _random_string(length: int) -> str:
        return "".join(choices(ascii_letters, k=length))
    return _random_string
    

@pytest.fixture
def payment_values():
    def _payment_values(max_payment_value: int) -> dict:
        v1 = randint(2, max_payment_value)
        v2 = v1 - randint(1, v1 - 1)
        return {"u_bound": v1, "l_bound": v2}
    return _payment_values


@pytest.fixture
def create_json(random_string, payment_values) -> dict:
    p_values = payment_values(9999999)
    return {
    "title": "test_user",
    "salary": {
        "min_level": p_values["l_bound"],
        "max_level": p_values["u_bound"],
        "currency": choice(["USD", "EUR"])
    },
    "grade": random_string(10),
    "profession": {
        "name": random_string(10),
    },
    "skillset": [
        {
            "name": random_string(10),
        },
        {
            "name": random_string(10)
        }
    ],
    "extra_info": random_string(100)
    }

    
@pytest.fixture
def no_db_entries_error():
    return "Validation error, since the data from database equal to: None"


@pytest.mark.asyncio
async def test_unauthorized_post(test_client: AsyncClient, create_json):
    response = await test_client.post("/api/v1/vacancies/", json=create_json)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_unauthorize_patch(test_client: AsyncClient):
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.patch(f"/api/v1/vacancies/{vacancy_id}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_nothing(test_client: AsyncClient, no_db_entries_error):
    response = await test_client.get("/api/v1/vacancies/random_vacancy")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == no_db_entries_error


@pytest.mark.asyncio
async def test_get_random_nothing(test_client: AsyncClient, no_db_entries_error):
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.get(f"/api/v1/vacancies/{vacancy_id}")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"][0]["msg"] == no_db_entries_error