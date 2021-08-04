from typing import Optional
from datetime import date, datetime

from pydantic import BaseModel


class OperatorBotBase(BaseModel):
    user_id: int
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
    binance_config_disablebullonly: bool
    binance_config_disablebuynearhigh: bool
    binance_config_disablebuymacd: bool
    binance_config_disablebuyema: bool
    binance_config_disablebuyobv: bool
    binance_config_disablebuyelderray: bool
    binance_config_disablefailsafefibonaccilow: bool
    binance_config_disablefailsafelowerpcnt: bool
    binance_config_disableprofitbankupperpcnt: bool
    binance_config_disableprofitbankfibonaccihigh: bool
    binance_config_disableprofitbankreversal: bool
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: Optional[str]
    telegram_token: Optional[str]


class OperatorBotCreate(BaseModel):
    user_id: int
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
    binance_config_disablebullonly: bool
    binance_config_disablebuynearhigh: bool
    binance_config_disablebuymacd: bool
    binance_config_disablebuyema: bool
    binance_config_disablebuyobv: bool
    binance_config_disablebuyelderray: bool
    binance_config_disablefailsafefibonaccilow: bool
    binance_config_disablefailsafelowerpcnt: bool
    binance_config_disableprofitbankupperpcnt: bool
    binance_config_disableprofitbankfibonaccihigh: bool
    binance_config_disableprofitbankreversal: bool
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: Optional[str]
    telegram_token: Optional[str]


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
    binance_config_disablebullonly: Optional[bool] = False
    binance_config_disablebuynearhigh: Optional[bool] = False
    binance_config_disablebuymacd: Optional[bool] = False
    binance_config_disablebuyema: Optional[bool] = False
    binance_config_disablebuyobv: Optional[bool] = False
    binance_config_disablebuyelderray: Optional[bool] = False
    binance_config_disablefailsafefibonaccilow: Optional[bool] = False
    binance_config_disablefailsafelowerpcnt: Optional[bool] = False
    binance_config_disableprofitbankupperpcnt: Optional[bool] = False
    binance_config_disableprofitbankfibonaccihigh: Optional[bool] = False
    binance_config_disableprofitbankreversal: Optional[bool] = False
    logger_filelog: bool = False
    logger_logfile: str = "pycryptobot.log"
    logger_fileloglevel: str = "INFO"
    logger_consolelog: bool = True
    logger_consoleloglevel: str
    telegram_client_id: Optional[str]
    telegram_token: Optional[str]


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
