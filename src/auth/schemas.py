from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    pass


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    password: str | None = None
    email: EmailStr = None


class UserUpdate(schemas.BaseUserUpdate):
    username: str | None