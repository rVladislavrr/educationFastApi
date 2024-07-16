from fastapi import APIRouter, status, Response, Depends
from dishes.crud_dishes import CRUDDish
from dishes.schemas import Dishes, DishesAddUp, DishAll, DishesPacth
from auth.router import fastapi_users

router = APIRouter(
    tags=['Меню и блюда'],
    prefix='/m',
)


@router.get('/one/{dish_id}', response_model=Dishes, status_code=status.HTTP_200_OK, )
async def get_one_dish(dish_id: int):
    dish = await CRUDDish.get_one(dish_id)
    if dish:
        return Dishes.model_validate(dish, from_attributes=True)
    else:
        return Response(status_code=404)


@router.get('/')
async def get_all_menu() -> list[DishAll]:
    return await CRUDDish.get_all_dishes()


@router.post('/add', status_code=status.HTTP_201_CREATED)
async def add_one_dish(dish: DishesAddUp, super_user=Depends(fastapi_users.current_user(active=True, superuser=True))):
    index = await CRUDDish.add(dish)
    return {"id": index}


@router.patch('/{dish_id}', responses={404: {"message": "Not found"}},)
async def update_one_dish(dish_id: int, dish: DishesPacth, super_user=Depends(fastapi_users.current_user(active=True,
    superuser=True))):
    status_crud = await CRUDDish.update(dish_id, dish)
    return Response(status_code=status_crud)


@router.delete('/{dish_id}', responses={404: {"message": "Not found"}})
async def delete_one_dish(dish_id: int, super_user=Depends(fastapi_users.current_user(active=True, superuser=True))):
    status_crud = await CRUDDish.delete(dish_id)
    return Response(status_code=status_crud)
