from datetime import datetime
import json

from kubernetes import client, config
from kubernetes.client.rest import ApiException

from typing import List, Dict, Union, Any

from fastapi.encoders import jsonable_encoder

from app.core.config import settings
from app.crud.base import CRUDBase
from app.schemas import Bot, BotCreate, BotUpdate, BotStatus, BotLogs


class CRUDBot(CRUDBase[Bot, BotCreate, BotUpdate]):
    def get(
        self, *,
        bot_name: str,
    ) -> Bot:
        if settings.ENV == "dev":
            config.load_kube_config()
        else:
            config.load_incluster_config()

        api_corev1 = client.CoreV1Api()

        try:
            pods_list = api_corev1.list_namespaced_pod(label_selector=f"app={bot_name}", namespace="cryptobot")
            pod = pods_list.items[0]
            try:
                pod_logs = api_corev1.read_namespaced_pod_log(name=pod.metadata.name, namespace="cryptobot", pretty=True, tail_lines=50)
            except:
                pod_logs = ""
            return Bot(
                name=bot_name,
                status=pod.status.phase,
                logs=pod_logs,
            )
                
        except ApiException as e:
            print("Exception when calling CRUD->Bot->get: \n%s\n" % e)


    def get_status(
        self, *,
        bot_name: str,
    ) -> BotStatus:
        if settings.ENV == "dev":
            config.load_kube_config()
        else:
            config.load_incluster_config()

        api_corev1 = client.CoreV1Api()

        try:
            pods_list = api_corev1.list_namespaced_pod(label_selector=f"app={bot_name}", namespace="cryptobot")
            pod = pods_list.items[0]
            return BotStatus(status=pod.status.phase)
            
        except ApiException as e:
            print("Exception when calling CRUD->Bot->get_status: \n%s\n" % e)


    def get_logs(
        self, *,
        bot_name: str,
    ) -> str:
        if settings.ENV == "dev":
            config.load_kube_config()
        else:
            config.load_incluster_config()

        api_corev1 = client.CoreV1Api()

        try:
            pods_list = api_corev1.list_namespaced_pod(label_selector=f"app={bot_name}", namespace="cryptobot")
            pod = pods_list.items[0]
            try:
                pod_logs = api_corev1.read_namespaced_pod_log(name=pod.metadata.name, namespace="cryptobot", pretty=True, tail_lines=50)
            except:
                pod_logs = ""
            return BotLogs(logs=pod_logs)
            
        except ApiException as e:
            print("Exception when calling CRUD->Bot->get_logs: \n%s\n" % e)


bot = CRUDBot(Bot)
