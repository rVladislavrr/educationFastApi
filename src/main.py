from redis import asyncio as aioredis
from fastapi import FastAPI
from fastapi_cache.backends.redis import RedisBackend
from background_task.router import router as router_background
from config import settings
from dishes.router_menu import router as router_auth
from auth.router import router as router_menu
from fastapi_cache import FastAPICache
from chat_online.router import router as router_chat

app = FastAPI()
app.include_router(router_menu)
app.include_router(router_auth)
app.include_router(router_chat)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


app.include_router(router_background)
