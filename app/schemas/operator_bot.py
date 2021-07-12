from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel


class OperatorBotBase(BaseModel):
    customer: str
    binance_api_url: str = "https://api.binance.com"
    binance_api_key: str
    binance_api_secret: str
    binance_config_base_currency: str
    binance_config_quote_currency: str
    binance_config_granularity: str = "15m"
    binance_config_live: bool = False
    binance_config_verbose : bool = True
    binance_config_graphs: bool = False
    binance_config_buymaxsize: float
    binance_config_sellupperpcnt: float
    binance_config_selllowerpcnt: float
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: str
    telegram_token: str


class OperatorBotCreate(BaseModel):
    customer: str
    binance_api_url: str = "https://api.binance.com"
    binance_api_key: str
    binance_api_secret: str
    binance_config_base_currency: str
    binance_config_quote_currency: str
    binance_config_granularity: str = "15m"
    binance_config_live: bool = False
    binance_config_verbose : bool = True
    binance_config_graphs: bool = False
    binance_config_buymaxsize: float
    binance_config_sellupperpcnt: float
    binance_config_selllowerpcnt: float
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: str
    telegram_token: str


class OperatorBotUpdate(BaseModel):
    binance_api_url: str = "https://api.binance.com"
    binance_api_key: str
    binance_api_secret: str
    binance_config_granularity: str = "15m"
    binance_config_live: bool = False
    binance_config_verbose : bool = True
    binance_config_graphs: bool = False
    binance_config_buymaxsize: float
    binance_config_sellupperpcnt: float
    binance_config_selllowerpcnt: float
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: str
    telegram_token: str


class OperatorBotDelete(BaseModel):
    name: str
    pass

class OperatorBot(BaseModel):
    name: str
    binance_config_granularity: str = "15m"
    binance_config_live: bool = False
    binance_config_verbose : bool = True
    binance_config_graphs: bool = False
    binance_config_buymaxsize: float
    binance_config_sellupperpcnt: float
    binance_config_selllowerpcnt: float
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
