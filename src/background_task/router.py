from fastapi import APIRouter, Depends
from background_task.tasks import send_email
from auth.router import fastapi_users


router = APIRouter(
    prefix='/report',
    tags=['Сообщение на почту']
)

@router.get("/")
async def root(user=Depends(fastapi_users.current_user())):
    try:
        send_email.delay(user.username, user.email)
        return {
            'status': 'ok'
        }
    except Exception as e:
        return {
            'status': 'fail',
            'message': str(e)
        }