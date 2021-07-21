from datetime import datetime
import json

from kubernetes import client, config
from kubernetes.client.rest import ApiException

from typing import List, Dict, Union, Any

from fastapi.encoders import jsonable_encoder

from app.crud.base import CRUDBase
from app.schemas import OperatorBot, OperatorBotCreate, OperatorBotUpdate, OperatorBotDelete


class CRUDOperatorBot(CRUDBase[OperatorBot, OperatorBotCreate, OperatorBotUpdate]):
    def create_bot(
        self, *,
        obj_in: Any,
    ) -> Any:
        obj_in_data = jsonable_encoder(obj_in)

        config.load_incluster_config()

        api = client.CustomObjectsApi()
        bot_name = f'{obj_in_data["user_id"]}-{obj_in_data["binance_config_base_currency"]}{obj_in_data["binance_config_quote_currency"]}'
        data = {
            "apiVersion": "cryptobot.com/v1",
            "kind": "Bot",
            "metadata": {
                "name": bot_name,
                "namespace": "cryptobot",
            },
            "spec": {
                "binance_api_key": obj_in_data["binance_api_key"],
                "binance_api_secret": obj_in_data["binance_api_secret"],
                "binance_api_url": obj_in_data["binance_api_url"],
                "binance_config_base_currency": obj_in_data["binance_config_base_currency"].upper(),
                "binance_config_quote_currency": obj_in_data["binance_config_quote_currency"].upper(),
                "binance_config_granularity": obj_in_data["binance_config_granularity"],
                "binance_config_live": int(obj_in_data["binance_config_live"]),
                "binance_config_verbose": int(obj_in_data["binance_config_verbose"]),
                "binance_config_graphs": int(obj_in_data["binance_config_graphs"]),
                "binance_config_buymaxsize": obj_in_data["binance_config_buymaxsize"],
                "binance_config_sellupperpcnt": float(obj_in_data["binance_config_sellupperpcnt"]),
                "binance_config_selllowerpcnt": float(obj_in_data["binance_config_selllowerpcnt"]),
                "logger_consoleloglevel": obj_in_data["logger_consoleloglevel"],
                "telegram_client_id": obj_in_data["telegram_client_id"],
                "telegram_token": obj_in_data["telegram_token"]
            }
        }
        
        try:
            operator_bot = api.create_namespaced_custom_object(
                group = "cryptobot.com",
                version = "v1",
                namespace = "cryptobot",
                plural = "bots",
                body = data,
            )
        except ApiException as e:
            print("Exception when calling CRUD->OperatorBot->create_bot: \n%s\n" % e)

        return obj_in_data


    def get_bot(
        self, *,
        bot_name: str,
    ) -> OperatorBot:
        config.load_incluster_config()

        api = client.CustomObjectsApi()

        try:
            operator_bot = api.get_namespaced_custom_object(
                group = "cryptobot.com",
                version = "v1",
                namespace = "cryptobot",
                plural = "bots",
                name = bot_name,
            )
            result = operator_bot["spec"]
            result["name"] = bot_name
            
            return OperatorBot(**result)
            
        except ApiException as e:
            print("Exception when calling CRUD->OperatorBot->get_bot: \n%s\n" % e)



    def update_bot(
        self, *,
        bot_name: str,
        obj_in: Union[OperatorBotUpdate, Dict[str, Any]]
    ) -> Any:
        obj_in_data = jsonable_encoder(obj_in)

        config.load_incluster_config()

        api = client.CustomObjectsApi()
        data = {
            "apiVersion": "cryptobot.com/v1",
            "kind": "Bot",
            "metadata": {
                "name": bot_name,
                "namespace": "cryptobot",
            },
            "spec": {
                "binance_api_key": obj_in_data["binance_api_key"],
                "binance_api_secret": obj_in_data["binance_api_secret"],
                "binance_api_url": obj_in_data["binance_api_url"],
                "binance_config_granularity": obj_in_data["binance_config_granularity"],
                "binance_config_live": int(obj_in_data["binance_config_live"]),
                "binance_config_verbose": int(obj_in_data["binance_config_verbose"]),
                "binance_config_graphs": int(obj_in_data["binance_config_graphs"]),
                "binance_config_buymaxsize": obj_in_data["binance_config_buymaxsize"],
                "binance_config_sellupperpcnt": float(obj_in_data["binance_config_sellupperpcnt"]),
                "binance_config_selllowerpcnt": float(obj_in_data["binance_config_selllowerpcnt"]),
                "logger_consoleloglevel": obj_in_data["logger_consoleloglevel"],
                "telegram_client_id": obj_in_data["telegram_client_id"],
                "telegram_token": obj_in_data["telegram_token"]
            }
        }
        
        try:
            operator_bot = api.patch_namespaced_custom_object(
                group = "cryptobot.com",
                version = "v1",
                namespace = "cryptobot",
                plural = "bots",
                name = bot_name,
                body = data,
            )
        except ApiException as e:
            print("Exception when calling CRUD->OperatorBot->create_bot: \n%s\n" % e)

        return obj_in_data

    def delete_bot(
        self, *,
        bot_name: str,
    ) -> Any:
        config.load_incluster_config()

        api = client.CustomObjectsApi()

        try:
            operator_bot = api.delete_namespaced_custom_object(
                group = "cryptobot.com",
                version = "v1",
                namespace = "cryptobot",
                plural = "bots",
                name = bot_name,
            )
        except ApiException as e:
            print("Exception when calling CRUD->OperatorBot->delete_bot: \n%s\n" % e)

        return bot_name


operator_bot = CRUDOperatorBot(OperatorBot)
