from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    DEBUG_MODE: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
