from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, Request
from starlette.config import Config
from starlette.responses import HTMLResponse, RedirectResponse

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.get('/')
async def home(request: Request):
    user = request.session.get('user')

    if user is not None:
        email = user['email']
        html = (
            f'<pre>Email: {email}</pre><br>'
            '<a href="/docs">documentation</a><br>'
            '<a href="/logout">logout</a>'
        )
        return HTMLResponse(html)
    return HTMLResponse('<a href="login">login</a>')


config = Config('.env')
oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@auth_router.get('/login')  # Tag it as "authentication" for our docs
async def login(request: Request):
    # Redirect Google OAuth back to our application
    redirect_uri = 'http://localhost:2080/api/v1/auth/'

    return await oauth.google.authorize_redirect(request, redirect_uri)


@auth_router.route('/auth')
async def auth(request: Request):
    # Perform Google OAuth
    token = await oauth.google.authorize_access_token(request)
    user = await oauth.google.parse_id_token(request, token)

    # Save the user
    request.session['user'] = dict(user)

    return RedirectResponse(url='/')


@auth_router.get('/logout')  # Tag it as "authentication" for our docs
async def logout(request: Request):
    # Remove the user
    request.session.pop('user', None)

    return RedirectResponse(url='/')
