import asyncio
import os

import pytest_asyncio
from pydantic import SecretStr

from aiotdlib import Client, ClientSettings
from aiotdlib.authorization import CliAuthorizationHandler

CODE_RECEIVE_TIMEOUT_SECS = 60
TEST_API_ID = os.environ.get("AIOTDLIB_API_ID")
TEST_API_HASH = os.environ.get("AIOTDLIB_API_HASH")
TEST_PHONE_NUMBER = os.environ.get("AIOTDLIB_PHONE_NUMBER")

if not TEST_API_ID or not TEST_API_HASH or not TEST_PHONE_NUMBER:
    raise ValueError("Missing environment variables")


class TestAuthorizationHandler(CliAuthorizationHandler):
    def __init__(self):
        super().__init__()

    async def _auth_get_code(self, *, code_type: str = 'SMS', expected_length: int = 5) -> str:
        self.logger.info("Waiting for code...")
        for _ in range(CODE_RECEIVE_TIMEOUT_SECS):
            with open('code.txt', 'r') as f:
                code = f.read()
            if len(code) != 0:
                with open('code.txt', 'w'):
                    pass  # truncate file for next run
                return code.strip()
            await asyncio.sleep(1)
        raise ValueError("Code was not provided")

    async def _auth_get_password(self) -> str:
        raise NotImplemented

    async def _auth_get_first_name(self) -> str:
        raise NotImplemented

    async def _auth_get_last_name(self) -> str:
        raise NotImplemented

    async def _auth_get_email(self) -> str:
        raise NotImplemented


@pytest_asyncio.fixture(loop_scope="session")
async def authorizer() -> TestAuthorizationHandler:
    return TestAuthorizationHandler()


@pytest_asyncio.fixture(loop_scope="session")
async def client(authorizer: TestAuthorizationHandler) -> Client:
    async with Client(settings=ClientSettings(
        authorization_handler=authorizer,
        api_id=int(TEST_API_ID),
        api_hash=SecretStr(TEST_API_HASH),
        phone_number=TEST_PHONE_NUMBER,
        session_name="aiotdlib-test",
        #tdlib_verbosity=TDLibLogVerbosity.VERBOSE
    )) as client:
        yield client
