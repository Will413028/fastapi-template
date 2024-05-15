from datetime import UTC, datetime, timedelta

from fastapi import Depends, HTTPException, status
from jose import jwt
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.auth.schemas import LoginInput, UserCreateInput, UserInfo
from src.auth.utils import get_password_hash, verify_password
from src.config import settings
from src.database import get_db
from src.logger import stru_logger
from src.models import User


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def get_user_by_account(db: Session, account: str) -> User:
    query = select(User).where(User.account == account)
    user = db.execute(query).scalar()

    return user


def get_user_by_id(db: Session, user_id: int) -> User:
    query = select(User).where(User.id == user_id)
    user = db.execute(query).scalar()

    return user


def create_user(db: Session, user: UserCreateInput):
    user.password = get_password_hash(user.password)

    db_user = User(account=user.account, password=user.password)

    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        db.rollback()

        stru_logger.exception(f"create_user failed, error: {e}")

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User create failed: {str(e)}",
        ) from e

    return db_user


def check_new_user(user: UserCreateInput, db: Session) -> UserCreateInput:
    db_user = get_user_by_account(db, user.account)

    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")


def authenticate_user(data: LoginInput, db: Session = Depends(get_db)) -> User:
    db_user = get_user_by_account(db, data.account)

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not verify_password(data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid password or account"
        )

    return db_user


def get_user_info(user: User) -> UserInfo:
    return UserInfo(name=user.account)
