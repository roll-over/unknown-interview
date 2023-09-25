import pytest
from fastapi import status
from httpx import AsyncClient

from tests.utils import get_test_data


class TestCV:
    test_data = get_test_data("cv_vacancy")

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "cv_data, expected_status",
        [
            (test_data.get("valid_data"), status.HTTP_401_UNAUTHORIZED),
        ],
    )
    async def test_add_cv_unauthorized(
        self, test_client: AsyncClient, test_applicant, cv_data, expected_status
    ):
        response = await test_client.post(
            "/api/v1/cvs/",
            json=cv_data,
        )
        assert response.status_code == expected_status

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "cv_data, expected_status",
        [
            (test_data.get("valid_data"), status.HTTP_200_OK),
            (test_data.get("invalid_data"), status.HTTP_422_UNPROCESSABLE_ENTITY),
        ],
    )
    async def test_add_cv_authorized(
        self, test_client: AsyncClient, test_applicant, cv_data, expected_status
    ):
        await test_applicant.login(test_client)
        response = await test_client.post(
            "/api/v1/cvs/",
            json=cv_data,
        )
        assert response.status_code == expected_status
        await test_applicant.logout(test_client)
