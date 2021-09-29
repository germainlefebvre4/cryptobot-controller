from time import sleep
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


def test_read_bot_status() -> None:
    bot_name, operator_bot = create_random_operator_bot()

    bot_status = crud.bot.get_status(bot_name=bot_name)

    assert bot_status
    assert bot_status.status
    assert bot_status.status in ["RUNNING", "NOT_RUNNING"]


def test_read_bot_logs() -> None:
    bot_name, operator_bot = create_random_operator_bot()

    bot_logs = crud.bot.get_logs(bot_name=bot_name)

    assert bot_logs
    assert bot_logs.logs
    assert bot_logs.logs == "No logs available."


# def test_read_bot_version() -> None:
#     bot_name, operator_bot = create_random_operator_bot()
#     sleep(10)

#     bot_version = crud.bot.get_version(bot_name=bot_name)

#     assert bot_version
#     assert bot_version.version
#     assert bot_version.version == r"v.*"
