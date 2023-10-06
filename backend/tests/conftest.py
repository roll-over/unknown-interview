import asyncio

import pytest
import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from app.db.models.mixins import Role
from app.main import app
from tests.auth.user import TestUser


@pytest_asyncio.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def test_app():
    """Yield new app instance after overridden db client"""
    async with LifespanManager(app) as manager:
        yield manager.app


@pytest_asyncio.fixture(scope="session")
async def test_client(test_app) -> AsyncClient:
    """Yield an asynchronous test client"""
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client


@pytest_asyncio.fixture(scope="session")
async def test_applicant():

    async with TestUser(user_role=Role.applicant) as _user:
        yield _user


@pytest_asyncio.fixture(scope="session")
async def test_employer():
    async with TestUser(user_role=Role.employer) as _user:
        yield _user


@pytest.fixture
def no_db_entries_error() -> bytes:
    return b"[]"
