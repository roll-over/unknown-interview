import json
from base64 import b64encode

import itsdangerous

from app.config import settings
from app.db.models.user import User
from app.repository.repositories import user_repo


class TestUser:
    def __init__(self, secret_key=settings.SECRET_KEY, *, user_data):
        self.user = user_repo()
        self.user_data = user_data
        self.secret_key = secret_key

    async def __aenter__(self):
        await self.add_new_user()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        del self

    async def add_new_user(self):
        data = User(**self.user_data)
        await self.user.create_one(data)

    def __get_cookie(self) -> dict[str, str]:
        cookie_user = {"user": self.user_data}
        data = b64encode(json.dumps(cookie_user).encode("utf-8"))
        signer = itsdangerous.TimestampSigner(str(self.secret_key))
        cookie_value = signer.sign(data)

        return {
            "name": "session",
            "value": str(cookie_value, "utf-8"),
        }

    async def login(self, client):
        cookies = self.__get_cookie()
        client.cookies.set(**cookies)

    async def logout(self, client):
        client.cookies.clear()
