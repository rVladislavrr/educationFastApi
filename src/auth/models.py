from typing import AsyncGenerator
from sqlalchemy.orm import Mapped, sessionmaker, mapped_column
from sqlalchemy import func, JSON, ForeignKey
from fastapi import Depends
from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase,SQLAlchemyBaseUserTable
from sqlalchemy.ext.asyncio import AsyncSession
from config import settings
from base import Base, IDPK, str_320, str_1024, async_engine

DATABASE_URL = settings.DATABASE_URL


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'User'

    id: Mapped[IDPK] = mapped_column()
    username: Mapped[str]
    register_at: Mapped[datetime] = mapped_column(server_default=func.now())
    role_id: Mapped[int] = mapped_column(ForeignKey("role.id"))
    email: Mapped[str_320] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str_1024]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    pass


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[IDPK]
    name: Mapped[str]
    permissions = mapped_column(JSON)


async_session_maker = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
