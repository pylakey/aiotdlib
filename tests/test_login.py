import asyncio
import os
import pathlib

import pytest
import pytest_asyncio
from pydantic import SecretStr

from aiotdlib import Client, ClientSettings
from aiotdlib.authorization import CliAuthorizationHandler

CODE_RECEIVE_TIMEOUT_SECS = 60
TEST_DC_NUMBER = 2
TEST_DC_PHONE_NUMBER = "9996629845"

TEST_DO_REAL_LOGIN = os.environ.get("AIOTDLIB_TEST_DO_REAL_LOGIN")
TEST_API_ID = os.environ.get("AIOTDLIB_API_ID")
TEST_API_HASH = os.environ.get("AIOTDLIB_API_HASH")
TEST_PHONE_NUMBER = os.environ.get("AIOTDLIB_PHONE_NUMBER")

if not TEST_API_ID or not TEST_API_HASH or not TEST_PHONE_NUMBER:
    raise ValueError("Missing environment variables")


# https://core.telegram.org/api/auth#test-accounts
class TestDcAuthorizationHandler(CliAuthorizationHandler):
    def __init__(self, code: str | None):
        super().__init__()
        self.code_was_sent = False
        self.code = code

    async def _auth_get_code(self, *, code_type: str = 'SMS', expected_length: int = 5) -> str:
        if self.code is not None:
            return self.code if len(self.code) > 1 else self.code * expected_length
        else:
            self.logger.info("Waiting for code...")
            for _ in range(CODE_RECEIVE_TIMEOUT_SECS):
                with open('code.txt', 'r') as f:
                    code = f.read()
                if len(code) != 0:
                    with open('code.txt', 'w'):
                        pass  # truncate file for next run
                    return code.strip()
                self.code_was_sent = True
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


@pytest_asyncio.fixture(scope='function')
async def authorizer_real() -> TestDcAuthorizationHandler:
    return TestDcAuthorizationHandler(code=None)


@pytest_asyncio.fixture(scope='function')
async def client_real(authorizer_real: TestDcAuthorizationHandler, tmp_path: pathlib.Path) -> Client:
    async with Client(settings=ClientSettings(
            authorization_handler=authorizer_real,
            api_id=int(TEST_API_ID),
            api_hash=SecretStr(TEST_API_HASH),
            phone_number=TEST_PHONE_NUMBER,
            use_test_dc=False,
            # Ensure session info is cleaned up after tests finish
            files_directory=tmp_path,
    )) as client:
        yield client


@pytest_asyncio.fixture(scope='function')
async def authorizer_test() -> TestDcAuthorizationHandler:
    return TestDcAuthorizationHandler(code=str(TEST_DC_NUMBER))


@pytest_asyncio.fixture(scope='function')
async def client_test_dc(authorizer_test: TestDcAuthorizationHandler, tmp_path: pathlib.Path) -> Client:
    async with Client(settings=ClientSettings(
            authorization_handler=authorizer_test,
            api_id=int(TEST_API_ID),
            api_hash=SecretStr(TEST_API_HASH),
            phone_number=TEST_DC_PHONE_NUMBER,
            use_test_dc=True,
            # Ensure session info is cleaned up after tests finish
            files_directory=tmp_path,
    )) as client:
        yield client


@pytest_asyncio.fixture(scope='function')
async def authorizer_test_wrong_code() -> TestDcAuthorizationHandler:
    return TestDcAuthorizationHandler(code='00000')


@pytest.mark.skipif(not bool(TEST_DO_REAL_LOGIN),
                    reason="Telegram rate limits logins to a small number per day. "
                           "Skip this test unless the environment variable TEST_DO_REAL_LOGIN "
                           "is set to a non-empty value.")
@pytest.mark.asyncio(scope='function')
async def test_client_real_login(client_real: Client) -> None:
    assert getattr(client_real.settings.authorization_handler, 'code_was_sent', False)
    assert client_real.is_authorized


@pytest.mark.skip(reason="Test DC login not working https://github.com/tdlib/td/issues/3083")
@pytest.mark.asyncio(scope='function')
async def test_test_dc_login(client_test_dc: Client) -> None:
    assert client_test_dc.is_authorized


@pytest.mark.asyncio(scope='function')
async def test_test_dc_wrong_code(authorizer_test_wrong_code: TestDcAuthorizationHandler,
                                  tmp_path: pathlib.Path) -> None:
    with pytest.raises(ValueError, match="PHONE_CODE_INVALID"):
        async with Client(settings=ClientSettings(
                authorization_handler=authorizer_test_wrong_code,
                api_id=int(TEST_API_ID),
                api_hash=SecretStr(TEST_API_HASH),
                phone_number=TEST_DC_PHONE_NUMBER,
                use_test_dc=True,
                # Ensure session info is cleaned up after tests finish
                files_directory=tmp_path
        )):
            assert False
