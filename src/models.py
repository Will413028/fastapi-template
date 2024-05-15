import datetime

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import false, func

from src.auth.constants import Role


class Base(DeclarativeBase):
    pass


class User(Base):
    """
    User class represents a user entity in the database.

    Attributes:
        id (int): The unique identifier for the user.
        account (str): The user's account name.
        password (str): The user's password.
        is_disabled (bool): Indicates whether the user is disabled or not.
        role (Role): The role of the user, represented by an instance of the Role enum.
        created_at (datetime.datetime): The timestamp of when the user was created.
        updated_at (datetime.datetime): The timestamp of when the user was last updated.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    account: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_disabled: Mapped[bool] = mapped_column(nullable=False, server_default=false())
    role: Mapped[int] = mapped_column(server_default=str(Role.GUEST.value))
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )
