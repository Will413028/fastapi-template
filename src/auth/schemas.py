from pydantic import BaseModel


class LoginInput(BaseModel):
    account: str
    password: str


class UserCreateInput(BaseModel):
    account: str
    password: str


class Token(BaseModel):
    access_token: str


class User(BaseModel):
    id: int
    account: str
    password: str
    is_disabled: bool
    role: str


class UserInfo(BaseModel):
    name: str
