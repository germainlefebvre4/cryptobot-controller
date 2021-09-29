from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import random
import json

from kubernetes import client, config
from kubernetes.client.rest import ApiException

from app import crud
from app.schemas.operator_bot import OperatorBotCreate, OperatorBotUpdate
from app.tests.utils.utils import (
    random_int_range, random_float_range,
    random_lower_string)
from app.tests.utils.operator_bot import (
    create_random_operator_bot)


def test_create_operator_bot() -> None:
    user_id = random_int_range(1000, 2000)
    binance_api_key = random_lower_string()
    binance_api_secret = random_lower_string()
    binance_config_base_currency = "BTC"
    binance_config_quote_currency = "EUR"
    binance_config_granularity = "15m"
    binance_config_live = False
    binance_config_verbose = True
    binance_config_graphs = False
    binance_config_buymaxsize = 0.0004
    binance_config_sellupperpcnt = 10
    binance_config_selllowerpcnt = -10
    binance_config_disablebullonly = False
    binance_config_disablebuynearhigh = False
    binance_config_disablebuymacd = False
    binance_config_disablebuyema = False
    binance_config_disablebuyobv = False
    binance_config_disablebuyelderray = False
    binance_config_disablefailsafefibonaccilow = False
    binance_config_disablefailsafelowerpcnt = False
    binance_config_disableprofitbankupperpcnt = False
    binance_config_disableprofitbankfibonaccihigh = False
    binance_config_disableprofitbankreversal = False
    logger_filelog = True
    logger_logfile = "pycryptobot.log"
    logger_fileloglevel = "DEBUG"
    logger_consolelog = True
    logger_consoleloglevel = "INFO"
    telegram_client_id = random_lower_string()
    telegram_token = random_lower_string()
    bot_name_expected = f'{user_id}-{binance_config_base_currency}{binance_config_quote_currency}'

    cryptobot_config_in = OperatorBotCreate(
        user_id=user_id,
        binance_api_key=binance_api_key,
        binance_api_secret=binance_api_secret,
        binance_config_base_currency=binance_config_base_currency,
        binance_config_quote_currency=binance_config_quote_currency,
        binance_config_granularity=binance_config_granularity,
        binance_config_live=binance_config_live,
        binance_config_verbose=binance_config_verbose,
        binance_config_graphs=binance_config_graphs,
        binance_config_buymaxsize=binance_config_buymaxsize,
        binance_config_sellupperpcnt=binance_config_sellupperpcnt,
        binance_config_selllowerpcnt=binance_config_selllowerpcnt,
        binance_config_disablebullonly=binance_config_disablebullonly,
        binance_config_disablebuynearhigh=binance_config_disablebuynearhigh,
        binance_config_disablebuymacd=binance_config_disablebuymacd,
        binance_config_disablebuyema=binance_config_disablebuyema,
        binance_config_disablebuyobv=binance_config_disablebuyobv,
        binance_config_disablebuyelderray=binance_config_disablebuyelderray,
        binance_config_disablefailsafefibonaccilow=binance_config_disablefailsafefibonaccilow,
        binance_config_disablefailsafelowerpcnt=binance_config_disablefailsafelowerpcnt,
        binance_config_disableprofitbankupperpcnt=binance_config_disableprofitbankupperpcnt,
        binance_config_disableprofitbankfibonaccihigh=binance_config_disableprofitbankfibonaccihigh,
        binance_config_disableprofitbankreversal=binance_config_disableprofitbankreversal,
        logger_filelog=logger_filelog, logger_logfile=logger_logfile, logger_fileloglevel=logger_fileloglevel,
        logger_consolelog=logger_consolelog, logger_consoleloglevel=logger_consoleloglevel,
        telegram_client_id=telegram_client_id,
        telegram_token=telegram_token,
    )

    operator_bot__bot_name, operator_bot = crud.operator_bot.create_bot(obj_in=cryptobot_config_in)

    assert operator_bot
    assert operator_bot["user_id"] == user_id
    assert operator_bot__bot_name == bot_name_expected
    assert operator_bot["binance_api_key"] == binance_api_key
    assert operator_bot["binance_api_secret"] == binance_api_secret
    assert operator_bot["binance_config_base_currency"] == binance_config_base_currency
    assert operator_bot["binance_config_quote_currency"] == binance_config_quote_currency
    assert operator_bot["binance_config_granularity"] == binance_config_granularity
    assert operator_bot["binance_config_live"] == binance_config_live
    assert operator_bot["binance_config_verbose"] == binance_config_verbose
    assert operator_bot["binance_config_graphs"] == binance_config_graphs
    assert operator_bot["binance_config_buymaxsize"] == binance_config_buymaxsize
    assert operator_bot["binance_config_sellupperpcnt"] == binance_config_sellupperpcnt
    assert operator_bot["binance_config_selllowerpcnt"] == binance_config_selllowerpcnt
    assert operator_bot["binance_config_disablebullonly"] == binance_config_disablebullonly
    assert operator_bot["binance_config_disablebuynearhigh"] == binance_config_disablebuynearhigh
    assert operator_bot["binance_config_disablebuymacd"] == binance_config_disablebuymacd
    assert operator_bot["binance_config_disablebuyema"] == binance_config_disablebuyema
    assert operator_bot["binance_config_disablebuyobv"] == binance_config_disablebuyobv
    assert operator_bot["binance_config_disablebuyelderray"] == binance_config_disablebuyelderray
    assert operator_bot["binance_config_disablefailsafefibonaccilow"] == binance_config_disablefailsafefibonaccilow
    assert operator_bot["binance_config_disablefailsafelowerpcnt"] == binance_config_disablefailsafelowerpcnt
    assert operator_bot["binance_config_disableprofitbankupperpcnt"] == binance_config_disableprofitbankupperpcnt
    assert operator_bot["binance_config_disableprofitbankfibonaccihigh"] == binance_config_disableprofitbankfibonaccihigh
    assert operator_bot["binance_config_disableprofitbankreversal"] == binance_config_disableprofitbankreversal
    assert operator_bot["logger_filelog"] == logger_filelog
    assert operator_bot["logger_logfile"] == logger_logfile
    assert operator_bot["logger_fileloglevel"] == logger_fileloglevel
    assert operator_bot["logger_consolelog"] == logger_consolelog
    assert operator_bot["logger_consoleloglevel"] == logger_consoleloglevel
    assert operator_bot["telegram_client_id"] == telegram_client_id
    assert operator_bot["telegram_token"] == telegram_token


def test_update_operator_bot() -> None:
    bot_name, operator_bot = create_random_operator_bot()
    user_id = random_int_range(2000, 3000)
    binance_api_key = random_lower_string()
    binance_api_secret = random_lower_string()
    binance_config_base_currency = "USD"
    binance_config_quote_currency = "ETH"
    binance_config_granularity = "60m"
    binance_config_live = False
    binance_config_verbose = False
    binance_config_graphs = True
    binance_config_buymaxsize = 1
    binance_config_sellupperpcnt = 20
    binance_config_selllowerpcnt = -20
    binance_config_disablebullonly = True
    binance_config_disablebuynearhigh = True
    binance_config_disablebuymacd = True
    binance_config_disablebuyema = True
    binance_config_disablebuyobv = True
    binance_config_disablebuyelderray = True
    binance_config_disablefailsafefibonaccilow = True
    binance_config_disablefailsafelowerpcnt = True
    binance_config_disableprofitbankupperpcnt = True
    binance_config_disableprofitbankfibonaccihigh = True
    binance_config_disableprofitbankreversal = True
    logger_filelog = False
    logger_logfile = "pycryptobot-updated.log"
    logger_fileloglevel = "INFO"
    logger_consolelog = False
    logger_consoleloglevel = "DEBUG"
    telegram_client_id = random_lower_string()
    telegram_token = random_lower_string()

    cryptobot_config_in = OperatorBotUpdate(
        binance_api_key=binance_api_key,
        binance_api_secret=binance_api_secret,
        binance_config_granularity=binance_config_granularity,
        binance_config_live=binance_config_live,
        binance_config_verbose=binance_config_verbose,
        binance_config_graphs=binance_config_graphs,
        binance_config_buymaxsize=binance_config_buymaxsize,
        binance_config_sellupperpcnt=binance_config_sellupperpcnt,
        binance_config_selllowerpcnt=binance_config_selllowerpcnt,
        binance_config_disablebullonly=binance_config_disablebullonly,
        binance_config_disablebuynearhigh=binance_config_disablebuynearhigh,
        binance_config_disablebuymacd=binance_config_disablebuymacd,
        binance_config_disablebuyema=binance_config_disablebuyema,
        binance_config_disablebuyobv=binance_config_disablebuyobv,
        binance_config_disablebuyelderray=binance_config_disablebuyelderray,
        binance_config_disablefailsafefibonaccilow=binance_config_disablefailsafefibonaccilow,
        binance_config_disablefailsafelowerpcnt=binance_config_disablefailsafelowerpcnt,
        binance_config_disableprofitbankupperpcnt=binance_config_disableprofitbankupperpcnt,
        binance_config_disableprofitbankfibonaccihigh=binance_config_disableprofitbankfibonaccihigh,
        binance_config_disableprofitbankreversal=binance_config_disableprofitbankreversal,
        logger_filelog=logger_filelog, logger_logfile=logger_logfile, logger_fileloglevel=logger_fileloglevel,
        logger_consolelog=logger_consolelog, logger_consoleloglevel=logger_consoleloglevel,
        telegram_client_id=telegram_client_id,
        telegram_token=telegram_token,
    )

    operator_bot_updated = crud.operator_bot.update_bot(bot_name=bot_name, obj_in=cryptobot_config_in)

    assert operator_bot_updated
    assert operator_bot_updated["binance_api_key"] == binance_api_key
    assert operator_bot_updated["binance_api_secret"] == binance_api_secret
    assert operator_bot_updated["binance_config_granularity"] == binance_config_granularity
    assert operator_bot_updated["binance_config_live"] == binance_config_live
    assert operator_bot_updated["binance_config_verbose"] == binance_config_verbose
    assert operator_bot_updated["binance_config_graphs"] == binance_config_graphs
    assert operator_bot_updated["binance_config_buymaxsize"] == binance_config_buymaxsize
    assert operator_bot_updated["binance_config_sellupperpcnt"] == binance_config_sellupperpcnt
    assert operator_bot_updated["binance_config_selllowerpcnt"] == binance_config_selllowerpcnt
    assert operator_bot_updated["binance_config_disablebullonly"] == binance_config_disablebullonly
    assert operator_bot_updated["binance_config_disablebuynearhigh"] == binance_config_disablebuynearhigh
    assert operator_bot_updated["binance_config_disablebuymacd"] == binance_config_disablebuymacd
    assert operator_bot_updated["binance_config_disablebuyema"] == binance_config_disablebuyema
    assert operator_bot_updated["binance_config_disablebuyobv"] == binance_config_disablebuyobv
    assert operator_bot_updated["binance_config_disablebuyelderray"] == binance_config_disablebuyelderray
    assert operator_bot_updated["binance_config_disablefailsafefibonaccilow"] == binance_config_disablefailsafefibonaccilow
    assert operator_bot_updated["binance_config_disablefailsafelowerpcnt"] == binance_config_disablefailsafelowerpcnt
    assert operator_bot_updated["binance_config_disableprofitbankupperpcnt"] == binance_config_disableprofitbankupperpcnt
    assert operator_bot_updated["binance_config_disableprofitbankfibonaccihigh"] == binance_config_disableprofitbankfibonaccihigh
    assert operator_bot_updated["binance_config_disableprofitbankreversal"] == binance_config_disableprofitbankreversal
    assert operator_bot_updated["logger_filelog"] == logger_filelog
    assert operator_bot_updated["logger_logfile"] == logger_logfile
    assert operator_bot_updated["logger_fileloglevel"] == logger_fileloglevel
    assert operator_bot_updated["logger_consolelog"] == logger_consolelog
    assert operator_bot_updated["logger_consoleloglevel"] == logger_consoleloglevel
    assert operator_bot_updated["telegram_client_id"] == telegram_client_id
    assert operator_bot_updated["telegram_token"] == telegram_token


def test_delete_operator_bot() -> None:
    config.load_kube_config()
    api_customeobjects = client.CustomObjectsApi()
    
    try:
        bots_list = api_customeobjects.list_namespaced_custom_object(group="cryptobot.com", version="v1", namespace="cryptobot", plural="bots", limit=10)
        for bot in bots_list["items"]:
            bot_name = bot["metadata"]["name"]
            if int(bot_name.split("-")[0]) >= 1000:
                api_customeobjects.delete_namespaced_custom_object(group="cryptobot.com", version="v1", namespace="cryptobot", plural="bots", name=bot_name)
    except ApiException as e:
        print("Exception when calling CustomObjectsApi->list_namespaced_custom_object: %s\n" % e)
