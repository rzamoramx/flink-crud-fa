
import os
from pydantic import BaseSettings


SOME_ENV_VAR = os.getenv("SOME_ENV_VAR")


class Settings(BaseSettings):
    DATABASE_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_HOSTNAME: str

    class Config:
        env_file = './dev.env' if os.getenv("CLOUD") is None else './cloud.env'


postgres_settings = Settings()


