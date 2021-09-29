from typing import Optional

from pydantic import BaseModel


class BotBase(BaseModel):
    name: str
    status: str
    logs: str

class BotCreate(BotBase):
    pass

class BotUpdate(BotBase):
    pass

class BotDelete(BotBase):
    pass

class Bot(BotBase):
    name: str
    status: str
    logs: str

class BotStatus(BaseModel):
    status: str

class BotLogs(BaseModel):
    logs: str

class BotVersion(BaseModel):
    version: str
