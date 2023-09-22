import pytest
from fastapi import status
from httpx import AsyncClient

from tests.utils import get_test_data


@pytest.mark.asyncio
async def test_get_random_nothing(test_client: AsyncClient, no_db_entries_error: bytes):
    response = await test_client.get("/api/v1/vacancies/random_vacancy")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert no_db_entries_error in response.content


@pytest.mark.asyncio
async def test_get_nothing(test_client: AsyncClient, no_db_entries_error: bytes):
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.get(f"/api/v1/vacancies/{vacancy_id}")

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert no_db_entries_error in response.content


@pytest.mark.asyncio
async def test_unauthorized_post(test_client: AsyncClient, test_user):
    await test_user.logout(test_client)
    
    data = get_test_data("cv_vacancy")["valid_data"]
    response = await test_client.post("/api/v1/vacancies/", json=data)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_unauthorize_patch(test_client: AsyncClient, test_user):
    await test_user.logout(test_client)
    
    vacancy_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    response = await test_client.patch(f"/api/v1/vacancies/{vacancy_id}")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.fixture(scope="module")
def posted_test_ids() -> list:
    return []


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "json_data, expected_status",
    [
        (get_test_data("cv_vacancy")["valid_data"], status.HTTP_200_OK) for _ in range(4)
    ]
)
async def test_vacancy_post(
    test_client: AsyncClient, test_user, json_data, expected_status, posted_test_ids: list
):
    await test_user.login(test_client)

    response = await test_client.post("/api/v1/vacancies/", json=json_data)
    posted_test_ids.append(response.json()["custom_id"])

    assert response.status_code == expected_status

    await test_user.logout(test_client)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "pointer, expected_status",
    [
        (pointer, status.HTTP_200_OK) for pointer in range(4)
    ]
)
async def test_vacancy_get(
    test_client: AsyncClient, test_user, posted_test_ids, pointer, expected_status
):
    await test_user.login(test_client)
    
    vacancy_id = posted_test_ids[pointer]
    response = await test_client.get(f"/api/v1/vacancies/{vacancy_id}")

    assert response.status_code == expected_status
    
    await test_user.logout(test_client)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "expected_status",
    [
        status.HTTP_200_OK for _ in range(5)
    ]
)
async def test_get_random_vacancy(
    test_client: AsyncClient, test_user, posted_test_ids: list, expected_status
):
    await test_user.login(test_client)
    
    response = await test_client.get("/api/v1/vacancies/random_vacancy")
    vacancy_id = response.json()["custom_id"]

    assert response.status_code == expected_status
    assert vacancy_id in posted_test_ids
    
    await test_user.logout(test_client)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "pointer, expected_status",
    [
        (pointer, status.HTTP_200_OK) for pointer in range(4)
    ]
)
async def test_vacancy_patch(
    test_client: AsyncClient, test_user, posted_test_ids: list, pointer, expected_status
):
    await test_user.login(test_client)
    
    vacancy_id = posted_test_ids[pointer]
    data = get_test_data("cv_vacancy")["valid_data"]
    changed_info = f"This line was changed {pointer}"
    data["extra_info"] = changed_info
    
    response = await test_client.patch(f"/api/v1/vacancies/{vacancy_id}", json=data)
    
    assert response.status_code == expected_status
    assert response.json()["extra_info"] == changed_info
    
    await test_user.logout(test_client)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "pointer, expected_delete_status, expected_get_status",
    [
        (pointer, status.HTTP_200_OK, status.HTTP_422_UNPROCESSABLE_ENTITY) 
        for pointer in range(4)
    ]
)
async def test_delete_vacancy(
    test_client: AsyncClient, test_user, posted_test_ids, pointer, 
    expected_delete_status, expected_get_status, no_db_entries_error
):
    await test_user.login(test_client)
    
    vacancy_id = posted_test_ids[pointer]
    delete_response = await test_client.delete(f"/api/v1/vacancies/{vacancy_id}")
    get_response = await test_client.get(f"/api/v1/vacancies/{vacancy_id}")
    
    assert delete_response.status_code == expected_delete_status
    assert get_response.status_code == expected_get_status
    assert no_db_entries_error in get_response.content
    
    await test_user.logout(test_client)