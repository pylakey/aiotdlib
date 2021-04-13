from __future__ import annotations

import asyncio
import enum
import hashlib
import json
import logging
import os
import signal
import sys
from functools import partial, update_wrapper
from pathlib import Path
from typing import Optional, TypeVar, Union

from pydantic import BaseModel, MissingError, validator

from . import __version__
from .api import (
    AioTDLibError,
    API,
    BaseObject,
    BasicGroup,
    BasicGroupFullInfo,
    Chat,
    ChatTypeBasicGroup,
    ChatTypePrivate,
    ChatTypeSecret,
    ChatTypeSupergroup,
    Close,
    Error, FormattedText,
    InputMessageText,
    Message,
    MessageSchedulingStateSendAtDate,
    MessageSchedulingStateSendWhenOnline,
    MessageSendOptions,
    ParseTextEntities,
    PhoneNumberAuthenticationSettings,
    ProxyTypeHttp,
    ProxyTypeMtproto,
    ProxyTypeSocks5,
    ReplyMarkup,
    SecretChat,
    Supergroup,
    SupergroupFullInfo,
    TdlibParameters,
    TextParseModeHTML,
    TextParseModeMarkdown,
    UpdateAuthorizationState,
    User,
    UserFullInfo,
)
from .client_cache import ClientCache
from .filters import create_bot_command_filter, text_message_filter
from .handlers import FilterCallable, Handler, HandlerCallable
from .middlewares import MiddlewareCallable
from .tdjson import TDJson, TDLibLogVerbosity
from .utils import ainput, AsyncResult, str_to_base64

RequestResult = TypeVar('RequestResult', bound=BaseObject)
ExecuteResult = TypeVar('ExecuteResult', bound=BaseObject)

ChatInfo = Union[
    User,
    UserFullInfo,
    BasicGroup,
    BasicGroupFullInfo,
    Supergroup,
    SupergroupFullInfo,
    SecretChat
]


class ClientProxyType(str, enum.Enum):
    MTPROTO = 'mtproto'
    HTTP = 'http'
    SOCKS5 = 'socks5'


class ClientProxySettings(BaseModel):
    """
    Universal proxy settings object for all proxy types

    Params:
        host (:class:`str`)
            Proxy server IP address

        port (:class:`int`)
            Proxy server port

        type (:class:`ClientProxySettingsType`)
            Proxy type

        username (:class:`str`)
            Username for logging in; may be empty

        password (:class:`str`)
            Password for logging in; may be empty

        http_only (:class:`bool`)
            Pass true if the proxy supports only HTTP requests and doesn't support transparent TCP connections via HTTP CONNECT method

        secret (:class:`str`)
            The proxy's secret in hexadecimal encoding

    """

    host: str
    port: int
    type: ClientProxyType = ClientProxyType.SOCKS5
    username: Optional[str] = None
    password: Optional[str] = None
    http_only: bool = False
    secret: Optional[str] = None

    @validator('secret', pre=True, always=True)
    def validate_secret(cls, secret: str, values):
        if values.get('type') == ClientProxyType.MTPROTO and secret is None:
            raise MissingError

        return secret


class Client:
    logger: logging.Logger = None
    loop: asyncio.AbstractEventLoop = None
    __stop_idle_event: asyncio.Event = None

    def __init__(
            self,
            api_id: int,
            api_hash: str,
            database_encryption_key: Union[str, bytes] = 'aiotdlib',
            phone_number: str = None,
            bot_token: str = None,
            use_test_dc: bool = False,
            system_language_code: str = 'en',
            device_model: str = 'aiotdlib',
            system_version: str = "",
            application_version: str = __version__,
            files_directory: str = None,
            first_name: str = None,
            last_name: str = None,
            library_path: str = None,
            tdlib_verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR,
            debug: bool = False,
            parse_mode: str = 'html',
            proxy_settings: ClientProxySettings = None
    ):
        """
            Params:
                api_id (:class:`int`)
                    Application identifier for Telegram API access, which can be obtained at https://my.telegram.org

                api_hash (:class:`str`)
                    Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org

                database_encryption_key (:class:`str`)
                    Encryption key of local session database. Default: aiotdlib

                phone_number (:class:`str`)
                    The phone number of the user, in international format.
                    Either phone_number or bot_token MUST be passed. ValueError would be raised otherwise

                bot_token (:class:`str`)
                    The bot token.
                    Either phone_number or bot_token MUST be passed. ValueError would be raised otherwise

                use_test_dc (:class:`bool`)
                    If set to true, the Telegram test environment will be used instead of the production environment

                system_language_code (:class:`str`)
                    IETF language tag of the user's operating system language; must be non-empty

                device_model (:class:`str`)
                    Model of the device the application is being run on; must be non-empty

                system_version (:class:`str`)
                    Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib

                application_version (:class:`str`)
                    Application version; must be non-empty

                files_directory (:class:`str`)
                    The path to the directory for storing files. Default: .aiotdlib/

                first_name (:class:`str`)
                    First name of new account if account with passed phone_number does not exist

                last_name (:class:`str`)
                    Last name of new account if account with passed phone_number does not exist

                library_path (:class:`str`)
                    Path to TDLib binary. By default binary included in package is used

                tdlib_verbosity (:class:`str`)
                    Verbosity level of TDLib itself. Default: 2 (WARNING) for more info look at (:class:`TDLibLogVerbosity`)

                debug (:class:`bool`)
                    When set to true all request and responses would be logged in console with DEBUG level

                parse_mode (:class:`str`)
                    Default parse mode for high-level methods like send_message. Default: html

                proxy_settings (:class:`ClientProxySettings`)
                    Settings for proxying telegram connection

        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG if debug else logging.INFO)

        if not bool(bot_token) and not bool(phone_number):
            raise ValueError('Either phone_number or bot_token should be specified')

        self.api_id = api_id
        self.api_hash = api_hash
        self.database_encryption_key = database_encryption_key
        self.phone_number = phone_number
        self.bot_token = bot_token
        self.use_test_dc = use_test_dc
        self.device_model = device_model
        self.application_version = application_version
        self.system_version = system_version
        self.system_language_code = system_language_code
        self.first_name = first_name
        self.last_name = last_name
        self.parse_mode = 'markdown' if (bool(parse_mode) and parse_mode.lower() == 'markdown') else 'html'
        self.proxy_settings = proxy_settings

        md5_hash = hashlib.md5()
        md5_hash.update((self.phone_number or self.bot_token).encode('utf-8'))
        directory_name = md5_hash.hexdigest()

        self.debug = debug

        if bool(files_directory):
            self.files_directory = str(os.path.join(files_directory, '.aiotdlib', directory_name))
        else:
            self.files_directory = str(os.path.join(Path(sys.argv[0]).parent, '.aiotdlib', directory_name))

        self.api = API(self)

        self.__tdjson = TDJson(library_path=library_path, verbosity=tdlib_verbosity)
        self.__current_authorization_state = None
        self.__is_authorized = False
        self.__running = False
        self.__request_results: dict[str, AsyncResult] = {}

        # For handlers registration
        self.__updates_handlers: dict[str, set[Handler]] = {}
        self.__middlewares: list[MiddlewareCallable] = []
        self.__middlewares_handlers: list[MiddlewareCallable] = []

        self.cache = ClientCache(self)

    # Magic methods
    async def __aenter__(self) -> 'Client':
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

    async def __handle_pending_request(self, update: BaseObject, *, request_id: str = None):
        _special_types = ['updateAuthorizationState']

        if update.ID in _special_types:
            request_id = update.ID

        if bool(request_id):
            async_result = self.__request_results.get(request_id)

            if bool(async_result):
                async_result.set_update(update)
                self.__request_results.pop(request_id, None)

    async def __call_handlers(self, update: BaseObject):
        # TODO: Maybe need to call updates concurrently with asyncio.gather (???)

        # Call update handlers for current update ID
        for handler in self.__updates_handlers.get(update.ID, []):
            try:
                await handler(self, update)
            except Exception as e:
                self.logger.error(e, exc_info=True)

        # Call wildcard update handlers
        for handler in self.__updates_handlers.get('*', []):
            try:
                await handler(self, update)
            except Exception as e:
                self.logger.error(e, exc_info=True)

    async def __handle_update(self, update: BaseObject):
        if len(self.__middlewares_handlers) == 0:
            return await self.__call_handlers(update)

        async def __fn(*_, **__):
            return await self.__call_handlers(update)

        call_next = __fn

        for m in self.__middlewares_handlers:
            call_next = update_wrapper(
                partial(m, call_next=call_next),
                call_next
            )

        return await call_next(self, update)

    async def __updates_loop(self):
        try:
            while self.__running:
                update: dict = await self.receive()

                if not bool(update):
                    continue

                if update.get('@type') == 'updateAuthorizationState':
                    if update.get('authorization_state', {}).get('@type') == 'authorizationStateClosed':
                        self.logger.warning('Session was terminated!')
                        self.loop.create_task(self.stop())
                        return

                try:
                    parsed_update = BaseObject.read(update)
                except Exception as e:
                    self.logger.error(f'Unable to parse incoming update! {e}', exc_info=True)
                    continue

                request_id = update.get("@extra", {}).get('request_id')
                self.loop.create_task(
                    self.__handle_pending_request(
                        parsed_update,
                        request_id=request_id
                    )
                )
                self.loop.create_task(self.__handle_update(parsed_update))
        except (asyncio.CancelledError, KeyboardInterrupt):
            raise
        except Exception as e:
            self.logger.error(f'Unhandled exception occurred!. {e.__class__.__qualname__}. {e}', exc_info=True)

    async def __close(self):
        if not bool(self.__running):
            return

        self.logger.info('Gracefully closing TDLib connection')
        await self.send(Close())

        if bool(self.__tdjson):
            self.__tdjson.stop()

    async def __auth_start(self) -> RequestResult:
        return await self.api.get_authorization_state(request_id="updateAuthorizationState")

    async def __set_tdlib_parameters(self) -> RequestResult:
        return await self.api.set_tdlib_parameters(
            parameters=TdlibParameters(
                use_test_dc=self.use_test_dc,
                database_directory=str(f"{self.files_directory}/database"),
                files_directory=str(f"{self.files_directory}/files"),
                use_file_database=True,
                use_chat_info_database=True,
                use_message_database=True,
                use_secret_chats=True,
                api_id=self.api_id,
                api_hash=self.api_hash,
                system_language_code=self.system_language_code,
                device_model=self.device_model,
                system_version=self.system_version,
                application_version=self.application_version,
                enable_storage_optimizer=True,
                ignore_file_names=True
            ),
            request_id="updateAuthorizationState"
        )

    async def __check_database_encryption_key(self) -> RequestResult:
        self.logger.info('Sending encryption key')
        result = await self.api.check_database_encryption_key(
            encryption_key=str_to_base64(self.database_encryption_key),
            request_id="updateAuthorizationState"
        )

        await self.__setup_proxy()

        return result

    async def __set_authentication_phone_number_or_check_bot_token(self) -> RequestResult:
        if self.phone_number:
            return await self.__set_authentication_phone_number()
        elif self.bot_token:
            return await self.__check_authentication_bot_token()
        else:
            raise RuntimeError('Unknown mode: both bot_token and phone_number are None')

    async def __set_authentication_phone_number(self) -> RequestResult:
        self.logger.info('Sending phone number')
        return await self.api.set_authentication_phone_number(
            phone_number=self.phone_number,
            settings=PhoneNumberAuthenticationSettings(
                is_current_phone_number=True,
                allow_flash_call=False,
                allow_sms_retriever_api=False
            ),
            request_id="updateAuthorizationState"
        )

    async def __check_authentication_bot_token(self) -> RequestResult:
        self.logger.info('Sending bot token')
        return await self.api.check_authentication_bot_token(
            self.bot_token,
            request_id="updateAuthorizationState"
        )

    async def __auth_get_code(self) -> str:
        code = ""

        while len(code) != 5 or not code.isdigit():
            code = await ainput('Enter code:')

        return code

    async def __auth_get_password(self) -> str:
        password = ""

        if not bool(password):
            password = await ainput('Enter 2FA password:', secured=True)

        return password

    async def __auth_get_first_name(self) -> str:
        first_name = self.first_name or ""

        while not bool(first_name) or len(first_name) > 64:
            first_name = await ainput('Enter first name:')

        return first_name

    async def __auth_get_last_name(self) -> str:
        last_name = self.last_name or ""

        if not bool(last_name):
            last_name = await ainput('Enter last name:')

        return last_name

    async def __check_authentication_code(self) -> RequestResult:
        code = await self.__auth_get_code()
        self.logger.info(f'Sending code {code}')

        return await self.api.check_authentication_code(
            code=code,
            request_id="updateAuthorizationState"
        )

    async def __register_user(self) -> RequestResult:
        first_name = await self.__auth_get_first_name()
        last_name = await self.__auth_get_last_name()
        self.logger.info(f'Registering new user in telegram as {first_name} {last_name or ""}'.strip())

        return await self.api.register_user(
            first_name=first_name,
            last_name=last_name,
            request_id="updateAuthorizationState"
        )

    async def __check_authentication_password(self) -> RequestResult:
        password = await self.__auth_get_password()
        self.logger.info('Sending password')

        return await self.api.check_authentication_password(
            password=password,
            request_id="updateAuthorizationState"
        )

    async def __auth_completed(self):
        self.logger.info('Authorization is completed')
        self.__request_results.pop('updateAuthorizationState', None)
        self.__is_authorized = True

    async def __stop_signal_handler(self, signum: int) -> None:
        self.logger.info('Signal %s received!', signum)
        await self.stop()

    async def __setup_proxy(self):
        if not bool(self.proxy_settings):
            # If proxy is not set disabling all configured proxy
            await self.api.disable_proxy()
            return

        self.logger.info('Retrieving all proxies list')
        result = await self.api.get_proxies()

        proxy_type_by_class = {
            ProxyTypeSocks5: 'socks5',
            ProxyTypeMtproto: 'mtproto',
            ProxyTypeHttp: 'http',
        }

        if self.debug:
            proxies_list_string = "\n".join(
                f"{'* ' if p.is_enabled else ''}[{proxy_type_by_class.get(p.type_.__class__)}] {p.server}:{p.port}"
                for p in result.proxies
            )
            self.logger.info(
                f'{len(result.proxies)} proxies already set up:\n'
                f'{proxies_list_string}'
                f'\n'
            )

        for p in result.proxies:
            if (
                    p.server == self.proxy_settings.host and
                    p.port == self.proxy_settings.port and
                    proxy_type_by_class.get(p.type_.__class__) == self.proxy_settings.type
            ):
                if not p.is_enabled:
                    await self.api.enable_proxy(p.id)

                return

        if self.proxy_settings.type == ClientProxyType.HTTP:
            proxy_type = ProxyTypeHttp.construct(
                username=self.proxy_settings.username,
                password=self.proxy_settings.password,
                http_only=self.proxy_settings.http_only
            )
        elif self.proxy_settings.type == ClientProxyType.MTPROTO:
            proxy_type = ProxyTypeMtproto.construct(secret=self.proxy_settings.secret)
        elif self.proxy_settings.type == ClientProxyType.SOCKS5:
            proxy_type = ProxyTypeSocks5.construct(
                username=self.proxy_settings.username,
                password=self.proxy_settings.password,
            )
        else:
            raise ValueError(f'Unknown proxy type {self.proxy_settings.type}')

        self.logger.info(
            f"Configuring PROXY of type {self.proxy_settings.type.value}. "
            f"Server: {self.proxy_settings.host}:{self.proxy_settings.port}"
        )

        await self.api.add_proxy(
            enable=True,
            server=self.proxy_settings.host,
            port=self.proxy_settings.port,
            type_=proxy_type,
        )

    def add_event_handler(
            self,
            handler: HandlerCallable,
            update_type: str = API.Types.ANY,
            *,
            filters: FilterCallable = None
    ):
        """
            Registering event handler
            You can register many handlers for certain event type
        """
        if self.__updates_handlers.get(update_type) is None:
            self.__updates_handlers[update_type] = set()

        if handler not in self.__updates_handlers[update_type]:
            self.__updates_handlers[update_type].add(
                handler
                if isinstance(handler, Handler)
                else Handler(handler, filters=filters)
            )

    def on_event(self, update_type: str = API.Types.ANY, *, filters: FilterCallable = None):
        def decorator(function: HandlerCallable) -> HandlerCallable:
            self.add_event_handler(function, update_type, filters=filters)
            return function

        return decorator

    def remove_event_handler(self, handler: Handler, update_type: str = API.Types.ANY):
        if self.__updates_handlers.get(update_type) is None:
            return

        self.__updates_handlers.get(update_type).remove(handler)

    def add_middleware(self, middleware: MiddlewareCallable):
        """
            Register middleware.
            Note that middleware would be called for EVERY EVENT.
            Do not use them for long-running tasks as it could be heavy performance hit
            You can add as much middlewares as you want.
            They would be called in order you've added them
        """

        self.__middlewares.append(middleware)
        return middleware

    def text_message_handler(self, function: HandlerCallable = None):
        """
        Registers event handler with predefined filter text_message_filter
        which allows only UpdateNewMessage with MessageText content

        Note: this method is universal and can be used directly or as decorator
        """
        if callable(function):
            self.add_event_handler(
                function,
                API.Types.UPDATE_NEW_MESSAGE,
                filters=text_message_filter
            )
        else:
            return self.on_event(
                API.Types.UPDATE_NEW_MESSAGE,
                filters=text_message_filter
            )

    def bot_command_handler(self, function: HandlerCallable = None, *, command: str = None):
        """
        Registers event handler with predefined filter bot_command_handler
        which allows only UpdateNewMessage with MessageText content and text of message starts with "/"

        Note: this method is universal and can be used directly or as decorator
        """
        if callable(function):
            self.add_event_handler(
                function,
                API.Types.UPDATE_NEW_MESSAGE,
                filters=create_bot_command_filter(command=command)
            )
        else:
            return self.on_event(
                API.Types.UPDATE_NEW_MESSAGE,
                filters=create_bot_command_filter(command=command)
            )

    async def send(self, query: Union[dict, BaseObject], *, request_id: str = None) -> AsyncResult:
        if not self.__running:
            raise RuntimeError('Client not started')

        if isinstance(query, BaseObject):
            query_type = query.ID
            query = query.dict(by_alias=True, exclude={'ID'})
            query['@type'] = query_type

        if query.get('@extra', None) is None:
            query['@extra'] = {}

        if not request_id and query['@extra'].get('request_id') is not None:
            request_id = query['@extra']['request_id']

        async_result = AsyncResult(self, request_id=request_id)
        query['@extra']['request_id'] = async_result.id
        async_result.request = query

        if self.debug:
            self.logger.debug(f">>>>> {query['@type']} {json.dumps(query)}")

        self.__request_results[async_result.id] = async_result
        await self.loop.run_in_executor(None, self.__tdjson.send, query)

        return async_result

    async def request(self, query: BaseObject, *, request_id: str = None, timeout: int = 5) -> Optional[RequestResult]:
        result = await self.send(query, request_id=request_id)
        await result.wait(raise_exc=True, timeout=timeout)

        if self.debug:
            self.logger.debug(f"<<<<< {result.update.ID} {result.update.dict(by_alias=True, exclude={'ID'})}")

        return result.update

    async def receive(self, timeout: float = 1.0) -> Optional[dict]:
        if not self.__running:
            raise RuntimeError('Client not started')

        return await self.loop.run_in_executor(None, self.__tdjson.receive, timeout)

    async def execute(self, query: BaseObject) -> ExecuteResult:
        if not self.__running:
            raise RuntimeError('Client not started')

        if isinstance(query, BaseObject):
            query_type = query.ID
            query = query.dict(by_alias=True, exclude={'ID'})
            query['@type'] = query_type

        result = await self.loop.run_in_executor(None, self.__tdjson.execute, query)
        result_object = BaseObject.read(result)

        if isinstance(result_object, Error):
            raise AioTDLibError(
                code=result_object.code,
                message=result_object.message
            )

        return result_object

    async def start(self) -> 'Client':
        self.logger.info('Starting client')
        self.logger.info(f'Session workdir: {self.files_directory}')

        # Preparing middlewares handlers
        self.__middlewares_handlers = list(reversed(self.__middlewares))

        # Setting up asyncio stuff
        self.loop = asyncio.get_running_loop()
        self.__stop_idle_event = asyncio.Event()

        # Starting updates loop
        self.__running = True
        self.loop.create_task(self.__updates_loop())

        # Initialize authorization process
        await self.authorize()
        return self

    async def idle(self, stop_signals: tuple = (signal.SIGINT, signal.SIGTERM, signal.SIGABRT, signal.SIGQUIT)):
        if not self.__running:
            raise ValueError('Client is already stopped')

        self.logger.info('Started Idling...')

        # Registering signals handlers for graceful shutdown
        for sig in stop_signals:
            self.loop.add_signal_handler(sig, lambda _s=sig: asyncio.create_task(self.__stop_signal_handler(sig)))

        try:
            await self.__stop_idle_event.wait()
        except asyncio.CancelledError:
            pass

        self.logger.info('Stop Idling...')

    async def stop(self):
        self.logger.info('Stopping telegram client...')
        await self.__close()

        self.__running = False
        self.__stop_idle_event.set()

    async def authorize(self):
        if bool(self.phone_number):
            self.logger.info('Authorization process has been started with phone')
        else:
            self.logger.info('Authorization process has been started with bot token')

        auth_actions = {
            None: self.__auth_start,
            API.Types.AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS: self.__set_tdlib_parameters,
            API.Types.AUTHORIZATION_STATE_WAIT_ENCRYPTION_KEY: self.__check_database_encryption_key,
            API.Types.AUTHORIZATION_STATE_WAIT_PHONE_NUMBER: self.__set_authentication_phone_number_or_check_bot_token,
            API.Types.AUTHORIZATION_STATE_WAIT_CODE: self.__check_authentication_code,
            API.Types.AUTHORIZATION_STATE_WAIT_REGISTRATION: self.__register_user,
            API.Types.AUTHORIZATION_STATE_WAIT_PASSWORD: self.__check_authentication_password,
            API.Types.AUTHORIZATION_STATE_READY: self.__auth_completed,
        }

        while not self.__is_authorized:
            while True:
                try:
                    self.logger.debug('Current authorization state: %s', self.__current_authorization_state)
                    next_action = auth_actions.get(self.__current_authorization_state)

                    if bool(next_action):
                        result = await next_action()
                    else:
                        raise RuntimeError(f'Unknown current authorization state: {self.__current_authorization_state}')
                except AioTDLibError as e:
                    # Need to retry previous step
                    self.logger.error(e)
                else:
                    break

            if isinstance(result, UpdateAuthorizationState):
                self.__current_authorization_state = result.authorization_state.ID

            await asyncio.sleep(0.1)

    async def parse_text(self, text: str, *, parse_mode: str = None) -> FormattedText:
        """
        Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode,
        TextUrl and MentionName entities contained in the text.
        """
        # ParseTextEntities can be called synchronously
        if parse_mode is None:
            parse_mode = self.parse_mode
        else:
            parse_mode = parse_mode.lower()

        return await self.execute(ParseTextEntities(
            text=text,
            parse_mode=(
                TextParseModeHTML()
                if parse_mode == 'html' else
                TextParseModeMarkdown(version=2)
            )
        ))

    # API methods shorthands
    async def send_message(
            self,
            chat_id: int,
            text: str,
            *,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            disable_web_page_preview: bool = False,
            clear_draft: bool = True,
            send_when_online: bool = False,
            send_date: int = None
    ) -> Message:
        """
        Sends a text message. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            text (:class:`str`)
                The text

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            disable_web_page_preview (:class:`bool`)
                True, if rich web page previews for URLs in the message text should be disabled

            clear_draft (:class:`bool`)
                True, if a chat message draft should be deleted

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if bool(send_date):
            scheduling_state = MessageSchedulingStateSendAtDate(send_date=send_date)
        elif send_when_online:
            scheduling_state = MessageSchedulingStateSendWhenOnline()
        else:
            scheduling_state = None

        formatted_text = await self.parse_text(text)

        return await self.api.send_message(
            chat_id=chat_id,
            message_thread_id=0,
            reply_to_message_id=reply_to_message_id,
            options=MessageSendOptions.construct(
                disable_notification=disable_notification,
                from_background=False,
                scheduling_state=scheduling_state
            ),
            reply_markup=reply_markup,
            input_message_content=InputMessageText.construct(
                text=formatted_text,
                disable_web_page_preview=disable_web_page_preview,
                clear_draft=clear_draft,
            ),
            skip_validation=True
        )

    async def edit_message(
            self,
            chat_id: int,
            message_id: int,
            text: str,
            *,
            reply_markup: ReplyMarkup = None,
            disable_web_page_preview: bool = False,
            clear_draft: bool = True,
    ):
        """
        Edits the text of a message (or a text of a game message).
        Returns the edited message after the edit is completed on the server side

        Params:
            chat_id (:class:`int`)
                The chat the message belongs to

            message_id (:class:`int`)
                Identifier of the message

            text (:class:`str`)
                New text of the message

            reply_markup (:class:`ReplyMarkup`)
                The new message reply markup; for bots only

            disable_web_page_preview (:class:`bool`)
                True, if rich web page previews for URLs in the message text should be disabled

            clear_draft (:class:`bool`)
                True, if a chat message draft should be deleted

        """
        formatted_text = await self.parse_text(text)

        return await self.api.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            reply_markup=reply_markup,
            input_message_content=InputMessageText.construct(
                text=formatted_text,
                disable_web_page_preview=disable_web_page_preview,
                clear_draft=clear_draft,
            ),
            skip_validation=True
        )

    async def get_main_list_chats(self, limit: int = 25) -> list[Chat]:
        """
        Returns an ordered list of chats in a main chat list.
        Chats are sorted by the pair (chat.position.order, chat.id) in descending order
        """
        return await self.cache.get_main_list_chats(limit)

    async def get_chat(self, chat_id: int) -> Chat:
        """
        Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
        """
        return await self.cache.get_chat(chat_id)

    async def get_user(self, user_id: int) -> User:
        return await self.cache.get_user(user_id)

    async def get_user_full_info(self, user_id: int) -> UserFullInfo:
        return await self.cache.get_user_full_info(user_id)

    async def get_basic_group(self, basic_group_id: int) -> BasicGroup:
        return await self.cache.get_basic_group(basic_group_id)

    async def get_basic_group_full_info(self, basic_group_id: int) -> BasicGroupFullInfo:
        return await self.cache.get_basic_group_full_info(basic_group_id)

    async def get_supergroup(self, supergroup_id: int) -> BasicGroup:
        return await self.cache.get_basic_group(supergroup_id)

    async def get_supergroup_full_info(self, supergroup_id: int) -> BasicGroupFullInfo:
        return await self.cache.get_basic_group_full_info(supergroup_id)

    async def get_secret_chat(self, secret_chat_id: int) -> SecretChat:
        return await self.cache.get_secret_chat(secret_chat_id)

    async def get_chat_info(self, chat: Union[int, Chat], *, full: bool = False) -> Optional[ChatInfo]:
        chat = await self.get_chat(chat) if isinstance(chat, int) else chat

        if isinstance(chat.type_, ChatTypePrivate):
            if full:
                return await self.get_user_full_info(chat.type_.user_id)
            else:
                return await self.get_user(chat.type_.user_id)

        if isinstance(chat.type_, ChatTypeBasicGroup):
            if full:
                return await self.get_basic_group_full_info(chat.type_.basic_group_id)
            else:
                return await self.get_basic_group(chat.type_.basic_group_id)

        if isinstance(chat.type_, ChatTypeSupergroup):
            if full:
                return await self.get_supergroup_full_info(chat.type_.supergroup_id)
            else:
                return await self.get_supergroup(chat.type_.supergroup_id)

        if isinstance(chat.type_, ChatTypeSecret):
            return await self.get_secret_chat(chat.type_.secret_chat_id)

        raise ValueError(f'Unknown chat.type {chat.type_.__class__.__qualname__}')
