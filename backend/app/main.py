from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
from app.exceptions import response_validation_exception_handler
from fastapi.exceptions import ResponseValidationError

from app.api.routers import v1
from app.db.engine import init_db

templates = Jinja2Templates(directory="app/templates")


app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs", debug=True)

app.include_router(v1)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(
    ResponseValidationError, response_validation_exception_handler
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
