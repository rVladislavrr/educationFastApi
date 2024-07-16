from fastapi_users import FastAPIUsers
from fastapi import APIRouter
from auth.auth import auth_backend
from auth.models import User
from auth.schemas import UserRead, UserCreate, UserUpdate
from auth.user_manager import get_user_manager

router = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["получение"],
)

router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["регистрация"],
)
