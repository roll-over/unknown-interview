from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    STAGE: str
    ME_CONFIG_MONGODB_URL: str

    SECRET_KEY: str

    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    IS_TEST: bool = False

    class Config:
        env_file = ".env"

    def __init__(self, **values):
        super().__init__(**values)
        self.IS_TEST = self.STAGE == "test"


settings = Settings()
