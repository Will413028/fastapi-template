from datetime import timedelta
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.auth.dependencies import get_current_user
from src.auth.schemas import Token, User, UserCreateInput, UserInfo
from src.auth.service import (
    authenticate_user,
    check_new_user,
    create_access_token,
    create_user,
    get_user_info,
)
from src.config import settings
from src.constans import common_responses
from src.database import get_db
from src.logger import stru_logger

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_200_OK,
    response_model=Token,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": dict[str, str],
            "content": {
                "application/json": {
                    "example": {"detail": "An error message explaining the specific issue."}
                }
            },
            "description": "An error message explaining the specific issue.",
        },
    },
    tags=["user"],
)
async def register(user_data: UserCreateInput, db: Session = Depends(get_db)):
    try:
        check_new_user(user_data, db)

        new_user = create_user(db, user_data)

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = create_access_token(
            data={"sub": new_user.account}, expires_delta=access_token_expires
        )

        return Token(access_token=access_token)

    except Exception as exc:
        stru_logger.exception(exc)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Register Error: {str(exc)}",
        ) from exc


@router.post(
    "/login",
    response_model=Token,
    responses={
        status.HTTP_400_BAD_REQUEST: {
            "model": dict[str, str],
            "content": {
                "application/json": {
                    "example": {"detail": "An error message explaining the specific issue."}
                }
            },
        },
        status.HTTP_401_UNAUTHORIZED: {
            "model": dict[str, str],
            "content": {
                "application/json": {"example": {"detail": "Invalid password or username"}}
            },
            "description": "Invalid password or username",
        },
        status.HTTP_404_NOT_FOUND: {
            "model": dict[str, str],
            "content": {"application/json": {"example": {"detail": "User not found"}}},
            "description": "User not found",
        },
        status.HTTP_422_UNPROCESSABLE_ENTITY: {
            "model": dict[str, str],
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Invalid input data. Please check the input fields for errors."
                    }
                }
            },
        },
    },
    tags=["user"],
)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
):
    try:
        user = authenticate_user(form_data.username, form_data.password, db)

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

        access_token = create_access_token(
            data={"sub": user.account}, expires_delta=access_token_expires
        )
        return Token(access_token=access_token)

    except HTTPException as http_exc:
        stru_logger.exception(http_exc)
        raise HTTPException(status_code=http_exc.status_code, detail=http_exc.detail) from http_exc
    except Exception as e:
        stru_logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"login error: {str(e)}",
        ) from e


@router.get(
    "/user/info",
    responses=common_responses,
    response_model=UserInfo,
    tags=["user"],
)
def _get_current_user_info(current_user: User = Depends(get_current_user)):
    try:
        return get_user_info(current_user)
    except Exception as e:
        stru_logger.exception(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"_get_current_user_info error: {str(e)}",
        ) from e
