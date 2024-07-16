from sqlalchemy import String
from typing import Annotated
from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import mapped_column, DeclarativeBase

async_engine = create_async_engine(
    url=settings.DATABASE_URL,
)

session_factory = async_sessionmaker(async_engine)

IDPK = Annotated[int, mapped_column(primary_key=True)]

str_320 = Annotated[str, 320]
str_1024 = Annotated[str, 1024]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_320: String(320),
        str_1024: String(1024)
    }

    def __repr__(self) -> str:
        cols = [f"{col}={getattr(self, col)}" for col in self.__table__.columns.keys()]
        return f"<{self.__class__.__name__}: {', '.join(cols)}>"
