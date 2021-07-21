from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient

import logging
import alembic.config
import alembic.command

from app.core.config import settings
from app.main import app
from app.tests.utils.user import authentication_token_from_email
from app.tests.utils.utils import get_superuser_token_headers

logging.getLogger('alembic').setLevel(logging.CRITICAL)


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
