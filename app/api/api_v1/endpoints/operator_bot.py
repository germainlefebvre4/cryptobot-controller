from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import json
import math

from typing import Any, List, Optional, Dict

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response

from app import crud, schemas
from app.api import deps

router = APIRouter()


@router.post("/")
def create_operator_bot(
    *,
    cryptobot_config_in: schemas.OperatorBotCreate,
) -> Any:
    """
    Create new operator bot.
    """
    bot_name, operator_bot = crud.operator_bot.create_bot(obj_in=cryptobot_config_in)
    # bot_name = f'{cryptobot_config_in.user_id}-{cryptobot_config_in.binance_config_base_currency}{cryptobot_config_in.binance_config_quote_currency}'
    
    return {"message": f"Operator '{bot_name}' created."}


@router.put("/{name}")
def update_cryptobot(
    *,
    name: str,
    cryptobot_config_in: schemas.OperatorBotUpdate,
) -> Any:
    """
    Update an operator bot.
    """
    crud.operator_bot.update_bot(bot_name=name, obj_in=cryptobot_config_in)
    
    return {"message": f"Operator '{name}' updated."}


@router.get("/{name}", response_model=schemas.OperatorBot)
def read_cryptobot(
    *,
    name: str,
) -> Any:
    """
    Get operator bot by name.
    """
    operator_bot = crud.operator_bot.get_bot(bot_name=name)
    
    return operator_bot


# @router.delete("/{name}", response_model=schemas.CryptobotDelete)
@router.delete("/{name}")
def delete_cryptobot(
    *,
    name: str,
) -> Any:
    """
    Delete an operator bot.
    """
    crud.operator_bot.delete_bot(bot_name=name)

    return {"message": f"Operator '{name}' deleted."}
