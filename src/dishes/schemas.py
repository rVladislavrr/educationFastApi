from pydantic import BaseModel

class DishAll(BaseModel):
    id: int
    name: str
    price: float


class DishesPacth(BaseModel):
    name: str | None = None
    price: float | None = None
    description: str | None = None

class DishesAddUp(BaseModel):
    name: str
    price: float
    description: str | None = None


class Dishes(DishAll):
    description: str | None = None
