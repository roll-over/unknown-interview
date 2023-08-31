from fastapi import FastAPI, APIRouter
from fastapi.exceptions import ResponseValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.templating import Jinja2Templates

from app.api.routers.auth import auth_router
from app.api.routers.cv import cv_router
from app.api.routers.user import user_router
from app.api.routers.vacancy import vacancy_router
from app.config import settings
from app.db.engine import init_db
from app.exceptions import response_validation_exception_handler


templates = Jinja2Templates(directory="app/templates")


app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs", debug=True)

# TODO: "Move v1 to separate file and import it here"
v1 = APIRouter(prefix="/api/v1")

v1.include_router(user_router)
v1.include_router(cv_router)
v1.include_router(auth_router)
v1.include_router(vacancy_router)

app.include_router(v1)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY
)


app.add_exception_handler(
    ResponseValidationError,
    response_validation_exception_handler
)


@app.get("/api/ping")
async def ping():
    return "pong"


@app.on_event("startup")
async def startup():
    await init_db()
    print("Starting up...")


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")
