from sqlalchemy.orm import Mapped

from base import Base, IDPK


class DicheOrm(Base):

    __tablename__ = 'diche'

    id: Mapped[IDPK]
    name: Mapped[str]
    description: Mapped[str | None]
    price: Mapped[float]
    count: Mapped[int]
