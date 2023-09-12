import asyncio

import pytest_asyncio
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from motor.motor_asyncio import AsyncIOMotorClient

from app.db.engine import init_client
from app.main import app, init_db


@pytest_asyncio.fixture(scope="session", autouse=True)
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def get_db_client_override() -> AsyncIOMotorClient:
    """Generate new client dependency for the database"""
    db_client: AsyncIOMotorClient = init_client("unknown_mongo_testing")

    yield db_client

    db_client.close()


@pytest_asyncio.fixture(scope="session")
async def test_app(get_db_client_override):
    """Yield new app instance after overridden db client"""
    app.dependency_overrides[init_db] = lambda: get_db_client_override
    async with LifespanManager(app) as manager:
        yield manager.app


@pytest_asyncio.fixture(scope="session")
async def test_client(test_app) -> AsyncClient:
    """Yield an asynchronous test client"""
    async with AsyncClient(app=test_app, base_url="http://test") as client:
        yield client
