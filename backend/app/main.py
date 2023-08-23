import asyncio
import json
from fastapi import FastAPI, Request

from starlette.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import jwt

from app.api.routers.user import user_router

templates = Jinja2Templates(directory="app/templates")

app = FastAPI(
    openapi_url="/api/v1/users/openapi.json", docs_url="/api/v1/users/docs", debug=True
)

app.include_router(user_router)


@app.get("/")
async def hello_world():
    return 'hello world'


@app.on_event("startup")
async def startup():
    print("Starting up...")


@app.on_event("shutdown")
async def shutdown():
    print("Shutting down...")


@app.get("/")
async def read_index():
    return FileResponse("index.html")
