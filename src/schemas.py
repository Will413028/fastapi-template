from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginatedDataResponse(BaseModel, Generic[T]):
    total_count: int = Field(..., example=100)
    total_pages: int = Field(..., example=10)
    current_page: int = Field(..., example=1)
    data: list[T]


class ListDataResponse(BaseModel, Generic[T]):
    data: list[T]


class DataResponse(BaseModel, Generic[T]):
    data: T


class DetailResponse(BaseModel):
    detail: str = Field(..., example="successful")
