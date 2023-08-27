import asyncio
import json
from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import jwt

from app.api.routers.cv import cv_router
from app.api.routers.user import user_router
from app.api.routers.vacancy import vacancy_router

templates = Jinja2Templates(directory="app/templates")


app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs", debug=True)

v1 = APIRouter(prefix="/api/v1", tags=["V1"])

v1.include_router(user_router)
v1.include_router(cv_router)
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


@app.get("/api/ping")
async def ping():
    return "pong"


@app.on_event("startup")
async def startup():
    print("Starting up...")


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")
