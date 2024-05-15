from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from src.auth.service import get_user_by_account
from src.auth.utils import oauth2_scheme
from src.config import settings
from src.database import get_db
from src.logger import stru_logger
from src.models import User


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        account: str = payload.get("sub")

        if account is None:
            raise credentials_exception

    except JWTError as e:
        stru_logger.exception(f"JWTError is {e}")

        raise credentials_exception from e

    user = get_user_by_account(db, account)

    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.is_disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
