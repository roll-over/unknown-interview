from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    class Config:
        env_file = '.env'


settings = Settings()
