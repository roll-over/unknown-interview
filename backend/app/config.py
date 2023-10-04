from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    STAGE: str
    ME_CONFIG_MONGODB_URL: str

    SECRET_KEY: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    EXTERNAL_URL: str = "http://localhost:2080"
    INTERNAL_URL: str = "http://client:80"

    IS_TEST: bool = False

    class Config:
        env_file = ".env"

    def __init__(self, **values):
        super().__init__(**values)
        self.IS_TEST = self.STAGE == "test"


settings = Settings()
