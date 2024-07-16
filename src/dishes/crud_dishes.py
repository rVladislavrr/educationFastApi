from base import session_factory
from dishes.models import DicheOrm
from sqlalchemy import select


class CRUDDish:
    @staticmethod
    async def get_all_dishes():
        async with session_factory() as session:
            query = select(DicheOrm)
            res = await session.execute(query)
            dishes = res.scalars().all()
            return dishes

    @staticmethod
    async def add(dish):
        async with session_factory() as session:
            dish_in_orm = DicheOrm(**dish.dict())
            session.add(dish_in_orm)
            await session.flush()
            id = dish_in_orm.id
            await session.commit()
            return id

    @staticmethod
    async def get_one(dish_id):
        async with session_factory() as session:
            query = select(DicheOrm).filter_by(id=dish_id)
            stmt = await session.execute(query)
            return stmt.scalars().one_or_none()

    @staticmethod
    async def update(dish_id, dish):
        async with session_factory() as session:
            query = select(DicheOrm).filter_by(id=dish_id)
            stmt = await session.execute(query)
            dish_orm = stmt.scalars().one_or_none()
            if dish_orm:
                for k,v in dish.dict().items():
                    if v is not None:
                        setattr(dish_orm, k, v)
                await session.commit()
                return 200
            return 404

    @staticmethod
    async def delete(dish_id):
        async with session_factory() as session:
            query = select(DicheOrm).filter_by(id=dish_id)
            stmt = await session.execute(query)
            dish = stmt.scalars().one_or_none()
            if dish:
                await session.delete(dish)
                await session.commit()
                return 200
            else:
                return 404