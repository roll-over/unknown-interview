import pytest
from fastapi import status
from httpx import AsyncClient

TEST_USER = {
    "name": "Vasily",
    'role': 'employer',
    "email": "vasya@gmail.com",
}


@pytest.mark.asyncio
async def test_post_user(test_client: AsyncClient):
    response = await test_client.post("/api/v1/users/", json=TEST_USER)
    assert TEST_USER["email"] == response.json()["email"]
    assert response.status_code == status.HTTP_200_OK

    response = await test_client.post("/api/v1/users/", json=TEST_USER)
    assert response.json() == {"detail": "User with this email is already exists"}
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.asyncio
async def test_post_user_without_fields(test_client: AsyncClient):
    response = await test_client.post("/api/v1/users/", json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.asyncio
async def test_get_user_list(test_client: AsyncClient):
    response = await test_client.get("/api/v1/users/")
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2


@pytest.mark.asyncio
async def test_delete_user(test_client: AsyncClient):
    user_email = TEST_USER.get('email')
    response = await test_client.delete(
        f"/api/v1/users/{user_email}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "User deleted successfully"}


@pytest.mark.asyncio
async def test_delete_user_not_found(test_client: AsyncClient):
    response = await test_client.delete(
        "/api/v1/users/not@found.com",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_user_without_fields(test_client: AsyncClient):
    response = await test_client.delete("/api/v1/users/test")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
