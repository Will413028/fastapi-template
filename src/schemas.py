from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PaginatedResponse(BaseModel, Generic[T]):
    total_count: int
    total_pages: int
    current_page: int
    data: list[T]


class ListResponse(BaseModel, Generic[T]):
    data: list[T]


class DateResponse(BaseModel, Generic[T]):
    data: T


class DetailResponse(BaseModel):
    """
    Basic return message.

    Attributes:
        detail (str): The detail of the return message.
    """

    detail: str = Field(..., example="successful")
