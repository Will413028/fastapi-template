from functools import lru_cache
from typing import Annotated

from fastapi import FastAPI, Depends

from config import Settings

app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "test_env_variable": settings.test_env,
    }