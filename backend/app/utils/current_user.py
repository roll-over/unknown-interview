from fastapi import Request

from app.exceptions import UserNotAuthenticated
from app.repository import UserRepository


async def current_user(User: UserRepository, request: Request):
    """Return current authorized user"""
    user_data = request.session.get("user")
    if user_data:
        return await User.get_user(user_data)

    raise UserNotAuthenticated
