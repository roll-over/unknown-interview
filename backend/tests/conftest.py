import asyncio

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

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
async def test_user():
    test_user_data = {"name": "Test User", "email": "hide_test@hire.hi"}

    async with TestUser(user_data=test_user_data) as _user:
        yield _user
