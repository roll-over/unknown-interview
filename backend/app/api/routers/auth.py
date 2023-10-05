from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request, Response
from fastapi.responses import JSONResponse, RedirectResponse

from app.api.schemas.user import UserInfoSchema
from app.config import settings
from app.exceptions import UserNotAuthenticated
from app.repository import UserRepository

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])

oauth = OAuth()

oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_id=settings.GOOGLE_CLIENT_ID,
    client_secret=settings.GOOGLE_CLIENT_SECRET,
    client_kwargs={"scope": "openid email profile"},
)


@auth_router.get("/login/google")
async def google_login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = f"{settings.EXTERNAL_URL}/api/v1/auth/google"

    return await oauth.google.authorize_redirect(request, redirect_uri)


@auth_router.get("/user_info", response_model=UserInfoSchema)
async def user_info(request: Request):
    user = request.session.get("user")
    if user:
        email = user.get("email", None)
        picture = user.get("picture", None)
        return JSONResponse({"email": email, "picture": picture})

    raise UserNotAuthenticated


@auth_router.get("/google")
async def google_auth(request: Request, User: UserRepository):
    token = await oauth.google.authorize_access_token(request)
    request_user = token.get("userinfo")

    existing_user = await User.get_user(request_user)
    if not existing_user:
        await User.create_one(request_user)

    request.session["user"] = request_user

    return RedirectResponse(url="/")


@auth_router.get("/logout")
async def logout(request: Request, response: Response):
    if "user" in request.session:
        del request.session["user"]

    return RedirectResponse(url="/")
