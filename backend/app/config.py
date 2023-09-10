from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    STAGE: str
    ME_CONFIG_MONGODB_URL: str

    SECRET_KEY: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    class Config:
        env_file = '.env'


settings = Settings()
