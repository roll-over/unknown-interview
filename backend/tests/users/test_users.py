import pytest
from fastapi import status
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_post_user(test_client: AsyncClient):
    data = {
        "name": "Vasily",
        'role': 'employer',
        "email": "vasya@gmail.com",
    }

    response = await test_client.post("/api/v1/users/", json=data)
    assert data["email"] == response.json()["email"]
    assert response.status_code == status.HTTP_200_OK

    response = await test_client.post("/api/v1/users/", json=data)
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
    response = await test_client.delete(
        "/api/v1/users/email@example.com", params={"user_email": "vasya@gmail.com"}
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"message": "User deleted successfully"}


@pytest.mark.asyncio
async def test_delete_user_not_found(test_client: AsyncClient):
    response = await test_client.delete(
        "/api/v1/users/not@found.com", params={"user_email": "not@found.com"}
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.asyncio
async def test_delete_user_without_fields(test_client: AsyncClient):
    response = await test_client.delete("/api/v1/users/not@found.com")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
