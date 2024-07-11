import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.auth.router import router as user_router
from src.config import settings
from src.database import run_migrations
from src.logger import stru_logger

origins = [
    "*",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        stru_logger.info("Running migrations...")
        run_migrations()
        stru_logger.info("Migrations completed.")
    except Exception as e:
        stru_logger.exception(f"run_migrations failed, error: {e}")

    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url="/docs" if settings.MODE == "dev" else None,
    redoc_url="/redoc" if settings.MODE == "dev" else None,
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/info")
async def info():
    return {
        "env": settings,
    }


app.include_router(user_router)
