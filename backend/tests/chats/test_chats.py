import pytest
from fastapi import status
from httpx import AsyncClient
from utils import get_test_data


class TestChats:
    test_data = get_test_data("chats")
    
    chats = test_data["chats"]
    messages = test_data["messages"]

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "json_data, expected_status",
        [
            (chats[0], status.HTTP_200_OK),
            (chats[1], status.HTTP_200_OK),
        ]
    )
    async def test_post_chat(self, test_client: AsyncClient, json_data, expected_status):
        response = await test_client.post("/api/v1/chats/", json=json_data)
        assert response.status_code == expected_status
        
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "expected_status",
        [
            (status.HTTP_200_OK),
        ]
    )
    async def test_get_all_chats(self, test_client: AsyncClient, expected_status):
        response = await test_client.get("/api/v1/chats/")
        assert response.status_code == expected_status
        assert len(response.json()) == 2
    
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "json_data, expected_status",
        [
            (messages[0], status.HTTP_200_OK),
            (messages[1], status.HTTP_200_OK),
            (messages[2], status.HTTP_200_OK),
            (messages[3], status.HTTP_200_OK)
        ]
    )
    async def test_post_messages(
        self, test_client: AsyncClient, json_data, expected_status
    ):
        response = await test_client.post("/api/v1/chats/add_message", json=json_data)
        assert response.status_code == expected_status
        assert response.json()["text"] == json_data["text"]
        
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "related_id, expected_status",
        [
            (messages[0]["related_id"], status.HTTP_200_OK),
            (messages[2]["related_id"], status.HTTP_200_OK),
        ]
    )
    async def test_get_messages(
        self, test_client: AsyncClient, related_id, expected_status
    ):
        response = await test_client.get(f"/api/v1/chats/{related_id}")
        assert response.status_code == expected_status
        assert len(response.json()) == 2