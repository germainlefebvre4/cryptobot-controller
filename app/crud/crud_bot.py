from datetime import datetime
import json

from kubernetes import client, config
from kubernetes.client.rest import ApiException

from typing import List, Dict, Union, Any

from fastapi.encoders import jsonable_encoder

from app.core.config import settings
from app.crud.base import CRUDBase
from app.schemas import Bot, BotCreate, BotUpdate, BotStatus, BotLogs, BotVersion


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
            if len(pods_list.items) > 0:
                pod = pods_list.items[0]
                if pod.status.container_statuses[0].ready & pod.status.container_statuses[0].ready:
                    return BotStatus(
                        name=bot_name,
                        status="RUNNING",
                    )
                else:
                    return BotStatus(
                        name=bot_name,
                        status="NOT_RUNNING"
                    )
            else:
                return BotStatus(
                    name=bot_name,
                    status="NOT_RUNNING",
                )
            
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
            if len(pods_list.items) > 0:
                pod = pods_list.items[0]
                try:
                    pod_logs = api_corev1.read_namespaced_pod_log(name=pod.metadata.name, namespace="cryptobot", tail_lines=50)
                except ApiException as e:
                    pod_logs = ""
                return BotLogs(logs=pod_logs)
            else:
                return BotLogs(logs="No logs available.")
            
        except ApiException as e:
            print("Exception when calling CRUD->Bot->get_logs: \n%s\n" % e)


    def get_version(
        self, *,
        bot_name: str,
    ) -> str:
        if settings.ENV == "dev":
            config.load_kube_config()
        else:
            config.load_incluster_config()

        api_appsv1 = client.AppsV1Api()

        try:
            deployment_desc = api_appsv1.read_namespaced_deployment(name=bot_name, namespace="cryptobot")
            bot_version = deployment_desc.spec.template.spec.containers[0].image.split(":")[1]
            return BotVersion(version=bot_version)
        except ApiException as e:
            print("Exception when calling CRUD->Bot->get_version: \n%s\n" % e)


bot = CRUDBot(Bot)
