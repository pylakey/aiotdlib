import asyncio
import logging
from abc import ABC, abstractmethod

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aiotdlib import Client, Handler
    from aiotdlib.client import AuthActions
    from aiotdlib.api import AuthorizationState

from aiotdlib.api import SetOption, OptionValueBoolean, CheckAuthenticationBotToken, \
    PhoneNumberAuthenticationSettings, SetAuthenticationPhoneNumber, CheckAuthenticationPassword, RegisterUser, \
    EmailAddressAuthenticationCode, CheckAuthenticationEmailCode, SetAuthenticationEmailAddress, \
    CheckAuthenticationCode, API, GetAuthorizationState, Error
from aiotdlib.utils import ainput


class AuthorizationHandler(ABC):
    def __init__(self):
        self.client: 'Client | None' = None

    def set_client(self, client: 'Client'):
        self.client = client

    async def authorize(self):
        await self.client.send(
            GetAuthorizationState()
        )

    @abstractmethod
    async def on_authorization_update(self, authorization_state: 'AuthorizationState'):
        pass


class NoOpAuthorizationHandler(AuthorizationHandler):
    async def on_authorization_update(self, authorization_state: 'AuthorizationState'):
        pass


class CliAuthorizationHandler(AuthorizationHandler):
    def __init__(self):
        super().__init__()
        self._authorized_future: asyncio.Future | None = None
        self.logger = logging.getLogger(__name__)
        self.error_handler: Handler | None = None

    async def authorize(self):
        if not bool(self.client.settings.phone_number) and not bool(self.client.settings.bot_token):
            raise ValueError('Either phone_number or bot_token should be specified')

        if self.client.is_bot:
            self.logger.info('Authorization process has been started with bot token')
        elif self.client.settings.phone_number:
            self.logger.info('Authorization process has been started with phone')

        self._authorized_future = asyncio.get_running_loop().create_future()
        self.error_handler = self.client.add_event_handler(self.on_error, update_type=API.Types.ERROR)

        await super().authorize()

        self.logger.info('Waiting for authorization to be completed')
        await self._authorized_future

    async def on_error(self, _: 'Client', update: Error):
        # These can be ignored
        if update.message == "Option can't be set":
            return
        if self.error_handler is not None:
            self.client.remove_event_handler(self.error_handler, update_type=API.Types.ERROR)
            self.error_handler = None
        if self._authorized_future is not None:
            self._authorized_future.set_exception(ValueError(update.message))

    async def on_authorization_update(self, authorization_state: 'AuthorizationState'):
        auth_actions: 'AuthActions' = {
            API.Types.AUTHORIZATION_STATE_WAIT_PHONE_NUMBER: self._set_authentication_phone_number_or_check_bot_token,
            API.Types.AUTHORIZATION_STATE_WAIT_CODE: self._check_authentication_code,
            API.Types.AUTHORIZATION_STATE_WAIT_EMAIL_ADDRESS: self._set_authentication_email_address,
            API.Types.AUTHORIZATION_STATE_WAIT_EMAIL_CODE: self._check_authentication_email_code,
            API.Types.AUTHORIZATION_STATE_WAIT_REGISTRATION: self._register_user,
            API.Types.AUTHORIZATION_STATE_WAIT_PASSWORD: self._check_authentication_password,
            API.Types.AUTHORIZATION_STATE_READY: self._auth_completed,
            # TODO: QR Login support
            # API.Types.AUTHORIZATION_STATE_WAIT_OTHER_DEVICE_CONFIRMATION: None,
        }
        action = auth_actions.get(authorization_state.ID)
        if bool(action):
            await action(authorization_state)

    async def _set_authentication_phone_number_or_check_bot_token(self, *_):
        await self.client.send(SetOption(name='online', value=OptionValueBoolean(value=True)))

        if self.client.is_bot:
            return await self._check_authentication_bot_token()

        return await self._set_authentication_phone_number()

    async def _set_authentication_phone_number(self, *_):
        self.logger.info('Sending phone number')
        await self.client.send(
            SetAuthenticationPhoneNumber(
                phone_number=self.client.settings.phone_number,
                settings=PhoneNumberAuthenticationSettings(
                    allow_flash_call=False,
                    allow_missed_call=False,
                    is_current_phone_number=True,
                    allow_sms_retriever_api=False,
                    authentication_tokens=[]
                ),
            )
        )

    async def _check_authentication_bot_token(self, *_):
        self.logger.info('Sending bot token')
        await self.client.send(
            CheckAuthenticationBotToken(
                token=self.client.settings.bot_token.get_secret_value(),
            )
        )

    async def _check_authentication_code(self, authorization_state: 'AuthorizationState'):
        code = await self._auth_get_code(code_type='SMS', expected_length=authorization_state.code_info.type_.length)
        self.logger.info(f'Sending code {code}')
        await self.client.send(
            CheckAuthenticationCode(
                code=code,
            )
        )

    async def _set_authentication_email_address(self, *_):
        email_address = await self._auth_get_email()
        await self.client.send(
            SetAuthenticationEmailAddress(
                email_address=email_address,
            )
        )

    async def _check_authentication_email_code(self, *_):
        code = await self._auth_get_code(code_type='EMail')
        self.logger.info(f'Sending email code {code}')
        return await self.client.send(
            CheckAuthenticationEmailCode(
                code=EmailAddressAuthenticationCode(
                    code=code
                ),
            )
        )

    async def _register_user(self, *_):
        first_name = await self._auth_get_first_name()
        last_name = await self._auth_get_last_name()
        self.logger.info(f'Registering new user in telegram as {first_name} {last_name or ""}'.strip())
        await self.client.send(
            RegisterUser(
                first_name=first_name,
                last_name=last_name,
            )
        )

    async def _check_authentication_password(self, *_):
        password = await self._auth_get_password()
        self.logger.info('Sending password')
        await self.client.send(
            CheckAuthenticationPassword(
                password=password,
            )
        )

    async def _auth_completed(self, *_):
        if self._authorized_future is None:
            self.logger.warning('Authorization finished before it was initiated')
        elif not self._authorized_future.done():
            if self.error_handler is not None:
                self.client.remove_event_handler(self.error_handler, update_type=API.Types.ERROR)
                self.error_handler = None
            self._authorized_future.set_result(None)

        # if not self.client.is_bot:
        #     # Preload main list chats
        #     await self.client.get_main_list_chats()

    # noinspection PyMethodMayBeStatic
    async def _auth_get_code(self, *, code_type: str = 'SMS', expected_length: int = 5) -> str:
        code = ""

        while len(code) != expected_length or not code.isdigit():
            code = await ainput(f'Enter {code_type} code of length {expected_length}:')

        return code

    async def _auth_get_password(self) -> str:
        password = self.client.settings.password

        if not bool(password):
            password = await ainput('Enter 2FA password:', secured=True)
        else:
            password = password.get_secret_value()

        return password

    async def _auth_get_first_name(self) -> str:
        first_name = self.client.settings.first_name or ""

        while not bool(first_name) or len(first_name) > 64:
            first_name = await ainput('Enter first name:')

        return first_name

    async def _auth_get_last_name(self) -> str:
        last_name = self.client.settings.last_name or ""

        if not bool(last_name):
            last_name = await ainput('Enter last name:')

        return last_name

    async def _auth_get_email(self) -> str:
        email = self.client.settings.email or ""

        if not bool(email):
            email = await ainput('Enter your email:')

        return email
