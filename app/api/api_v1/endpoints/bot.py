from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import json
import math

from typing import Any, List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.get("/{name}", response_model=schemas.Bot)
def read_bot(
    *,
    name: str,
) -> Any:
    """
    Get bot by name.
    """
    bot = crud.bot.get(bot_name=name)
    
    return bot


@router.get("/{name}/status", response_model=schemas.BotStatus)
def read_bot_status(
    *,
    name: str,
) -> Any:
    """
    Get bot status by name.
    """
    bot_status = crud.bot.get_status(bot_name=name)
    
    return bot_status


@router.get("/{name}/logs", response_model=schemas.BotLogs)
def read_bot_logs(
    *,
    name: str,
) -> Any:
    """
    Get bot logs by name.
    """
    bot_logs = crud.bot.get_logs(bot_name=name)
    
    return bot_logs



@router.get("/{name}/version", response_model=schemas.BotVersion)
def read_bot_version(
    *,
    name: str,
) -> Any:
    """
    Get bot version by name.
    """
    bot_version = crud.bot.get_version(bot_name=name)
    
    return bot_version
