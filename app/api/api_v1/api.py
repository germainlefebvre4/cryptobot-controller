from fastapi import APIRouter

from app.api.api_v1.endpoints import (
    operator_bot,
    bot,
)

api_router = APIRouter()
api_router.include_router(operator_bot.router, prefix="/operator/bot", tags=["operator"])
api_router.include_router(bot.router, prefix="/bot", tags=["bot"])
