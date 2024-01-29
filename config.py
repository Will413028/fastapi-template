from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    test_env: str

    class Config:
        env_file = ".env"
