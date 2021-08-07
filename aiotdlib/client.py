from __future__ import annotations

import asyncio
import enum
import hashlib
import logging
import os
import signal
import sys
import typing
import uuid
from collections import AsyncIterator
from functools import (
    partial,
    update_wrapper,
)
from pathlib import Path
from typing import (
    Optional,
    TypeVar,
    Union,
)

import pydantic.errors
from pydantic import (
    BaseModel,
    validator,
)

from . import __version__
from .api import (
    API,
    AioTDLibError,
    AuthorizationStateClosed,
    BaseObject,
    BasicGroup,
    BasicGroupFullInfo,
    Chat,
    ChatTypeBasicGroup,
    ChatTypePrivate,
    ChatTypeSecret,
    ChatTypeSupergroup,
    Error,
    FormattedText,
    InputFileLocal,
    InputFileRemote,
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageContent,
    InputMessageDocument,
    InputMessagePhoto,
    InputMessageText,
    InputMessageVideo,
    InputMessageVideoNote,
    InputMessageVoiceNote,
    InputThumbnail,
    Message,
    MessageSchedulingStateSendAtDate,
    MessageSchedulingStateSendWhenOnline,
    MessageSendOptions,
    MessageSendingStatePending,
    Messages,
    ParseTextEntities,
    PhoneNumberAuthenticationSettings,
    ProxyType,
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
    UpdateMessageSendSucceeded,
    User,
    UserFullInfo,
)
from .client_cache import ClientCache
from .filters import Filters
from .handlers import (
    FilterCallable,
    Handler,
    HandlerCallable,
)
from .middlewares import MiddlewareCallable
from .tdjson import (
    TDJson,
    TDLibLogVerbosity,
)
from .utils import (
    PendingRequest,
    ainput,
    str_to_base64,
)

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
            Pass true if the proxy supports only HTTP requests
            and doesn't support transparent TCP connections via HTTP CONNECT method

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
            raise pydantic.errors.MissingError

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
                    Application identifier hash for Telegram API access,
                    which can be obtained at https://my.telegram.org

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
                    Version of the operating system the application is being run on.
                    If empty, the version is automatically detected by TDLib

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
                    Verbosity level of TDLib itself.
                    Default: 2 (WARNING) for more info look at (:class:`TDLibLogVerbosity`)

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

        self.__tdjson = TDJson(library_path=library_path, verbosity=tdlib_verbosity)
        self.__current_authorization_state = None
        self.__is_authorized = False
        self.__running = False
        self.__pending_requests: dict[str, PendingRequest] = {}
        # "{chat_id}_{message_id}" will be used as key
        self.__pending_messages: dict[str, Message] = {}

        # For handlers registration
        self.__updates_handlers: dict[str, set[Handler]] = {}
        self.__middlewares: list[MiddlewareCallable] = []
        self.__middlewares_handlers: list[MiddlewareCallable] = []

        self.api = API(self)
        self.cache = ClientCache(self)
        self.first_time_auth = False

    # Magic methods
    async def __aenter__(self) -> 'Client':
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

    async def __call_handler(self, handler: Handler, update: BaseObject):
        try:
            await handler(self, update)
        except Exception as e:
            self.logger.error(e, exc_info=True)

    async def __call_handlers(self, update: BaseObject):
        tasks = []
        tasks.extend(self.__call_handler(h, update) for h in self.__updates_handlers.get(update.ID, []))
        tasks.extend(self.__call_handler(h, update) for h in self.__updates_handlers.get('*', []))
        # Running all handlers concurrently and independently
        await asyncio.gather(*tasks, return_exceptions=True)

    async def __handle_update(self, update: BaseObject):
        if len(self.__middlewares_handlers) == 0:
            return await self.__call_handlers(update)

        async def __fn(*_, **__):
            return await self.__call_handlers(update)

        call_next = __fn

        for m in self.__middlewares_handlers:
            call_next = update_wrapper(partial(m, call_next=call_next), call_next)

        return await call_next(self, update)

    async def __handle_pending_request(self, update: BaseObject):
        request_id = update.EXTRA.get('request_id')

        if not bool(request_id) and update.ID in ['updateAuthorizationState']:
            request_id = update.ID

        if bool(request_id):
            pending_request = self.__pending_requests.get(request_id)

            if bool(pending_request):
                if isinstance(update, Message) and isinstance(update.sending_state, MessageSendingStatePending):
                    self.__pending_messages[f"{update.chat_id}_{update.id}"] = update
                else:
                    self.__pending_requests.pop(request_id)
                    pending_request.set_update(update)

        if isinstance(update, UpdateMessageSendSucceeded):
            pending_message = self.__pending_messages.pop(
                f"{update.message.chat_id}_{update.old_message_id}",
                None
            )

            if bool(pending_message):
                request_id = pending_message.EXTRA.get('request_id')
                pending_request = self.__pending_requests.get(request_id)

                if bool(pending_request):
                    update.message.EXTRA['request_id'] = request_id
                    self.__pending_requests.pop(request_id)
                    pending_request.set_update(update.message)

    async def __updates_loop(self):
        try:
            while self.__running:
                update = await self.receive()

                if not bool(update):
                    continue

                if isinstance(update, UpdateAuthorizationState):
                    if isinstance(update.authorization_state, AuthorizationStateClosed):
                        self.logger.warning('Session was terminated!')
                        self.loop.create_task(self.stop())
                        return

                self.loop.create_task(self.__handle_pending_request(update))
                self.loop.create_task(self.__handle_update(update))
        except (asyncio.CancelledError, KeyboardInterrupt):
            raise
        except Exception as e:
            self.logger.error(f'Unhandled exception occurred!. {e.__class__.__qualname__}. {e}', exc_info=True)

    async def __close(self):
        if not bool(self.__running):
            return

        if bool(self.__tdjson):
            self.logger.info('Gracefully closing TDLib connection')
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
        self.first_time_auth = True

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
        self.first_time_auth = True

        code = await self.__auth_get_code()
        self.logger.info(f'Sending code {code}')

        return await self.api.check_authentication_code(
            code=code,
            request_id="updateAuthorizationState"
        )

    async def __register_user(self) -> RequestResult:
        self.first_time_auth = True

        first_name = await self.__auth_get_first_name()
        last_name = await self.__auth_get_last_name()
        self.logger.info(f'Registering new user in telegram as {first_name} {last_name or ""}'.strip())

        return await self.api.register_user(
            first_name=first_name,
            last_name=last_name,
            request_id="updateAuthorizationState"
        )

    async def __check_authentication_password(self) -> RequestResult:
        self.first_time_auth = True

        password = await self.__auth_get_password()
        self.logger.info('Sending password')

        return await self.api.check_authentication_password(
            password=password,
            request_id="updateAuthorizationState"
        )

    async def __auth_completed(self):
        self.__pending_requests.pop('updateAuthorizationState', None)

        if not bool(self.bot_token) and self.first_time_auth:
            # Update chats list in cache after successful authorization
            await self.get_main_list_chats(limit=500)

        self.__is_authorized = True
        self.logger.info('Authorization is completed')

    async def __auth_logging_out(self):
        self.logger.info('Auth session is logging out')

    async def __auth_closing(self):
        self.logger.info('Auth session is closing')

    async def __auth_closed(self):
        self.logger.info('Auth session is closed')

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

        proxy_type_by_class: dict[typing.Type[ProxyType], str] = {
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
        Registers event handler with predefined filter Filters.text
        which allows only UpdateNewMessage with MessageText content

        Note: this method is universal and can be used directly or as decorator
        """
        if callable(function):
            self.add_event_handler(function, API.Types.UPDATE_NEW_MESSAGE, filters=Filters.text)
        else:
            return self.on_event(API.Types.UPDATE_NEW_MESSAGE, filters=Filters.text)

    def bot_command_handler(self, function: HandlerCallable = None, *, command: str = None):
        """
        Registers event handler with predefined filter Filters.bot_command
        which allows only UpdateNewMessage with MessageText content and text of message starts with "/"

        Note: this method is universal and can be used directly or as decorator
        """
        if callable(function):
            self.add_event_handler(function, API.Types.UPDATE_NEW_MESSAGE, filters=Filters.bot_command(command))
        else:
            return self.on_event(API.Types.UPDATE_NEW_MESSAGE, filters=Filters.bot_command(command))

    async def send(self, query: BaseObject):
        if not self.__running:
            raise RuntimeError('Client not started')

        if self.debug:
            self.logger.debug(f">>>>> {query.ID} {query.json(by_alias=True)}")

        await self.loop.run_in_executor(None, self.__tdjson.send, query.dict(by_alias=True))

    async def request(
            self,
            query: BaseObject,
            *,
            request_id: str = None,
            request_timeout: int = None
    ) -> Optional[RequestResult]:
        if not bool(request_id):
            request_id = query.EXTRA.get('request_id') or uuid.uuid4().hex

        if request_timeout is None:
            request_timeout = 10

        query.EXTRA['request_id'] = request_id
        pending_request = PendingRequest(self, query)
        self.__pending_requests[request_id] = pending_request

        try:
            await self.send(query)
            await pending_request.wait(raise_exc=True, timeout=request_timeout)
        finally:
            if self.debug and bool(pending_request.update):
                self.logger.debug(f"<<<<< {pending_request.update.ID} {pending_request.update.json(by_alias=True)}")

        return pending_request.update

    async def execute(self, query: BaseObject) -> ExecuteResult:
        if not self.__running:
            raise RuntimeError('Client not started')

        result = await self.loop.run_in_executor(None, self.__tdjson.execute, query.dict(by_alias=True))
        result_object = BaseObject.read(result)

        if isinstance(result_object, Error):
            raise AioTDLibError(
                code=result_object.code,
                message=result_object.message
            )

        return result_object

    async def receive(self, timeout: float = 1.0) -> Optional[BaseObject]:
        if not self.__running:
            raise RuntimeError('Client not started')

        data = await self.loop.run_in_executor(None, self.__tdjson.receive, timeout)

        if not bool(data):
            return None

        try:
            return BaseObject.read(data)
        except Exception as e:
            self.logger.error(f'Unable to parse incoming update! {e}', exc_info=True)
            return None

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
            API.Types.AUTHORIZATION_STATE_LOGGING_OUT: self.__auth_logging_out,
            API.Types.AUTHORIZATION_STATE_CLOSING: self.__auth_closing,
            API.Types.AUTHORIZATION_STATE_CLOSED: self.__auth_closed,
        }

        while not self.__is_authorized:
            result = None

            while True:
                try:
                    self.logger.debug('Current authorization state: %s', self.__current_authorization_state)
                    next_action = auth_actions.get(self.__current_authorization_state)

                    if bool(next_action):
                        result = await next_action()
                    else:
                        self.logger.error(f'Unhandled authorization state: {self.__current_authorization_state}')
                        break
                except AioTDLibError as e:
                    # Need to retry previous step
                    self.logger.error(e)
                    await asyncio.sleep(0.1)
                else:
                    break

            if isinstance(result, UpdateAuthorizationState):
                self.__current_authorization_state = result.authorization_state.ID

            await asyncio.sleep(0.1)

    # Cache related methods
    async def get_option_value(self, name: str) -> typing.Union[str, int, bool, None]:
        """
        Returns the value of an option by its name.
        (Check the list of available options on https://core.telegram.org/tdlib/options.)
        Can be called before authorization

        Params:
            name (:class:`str`)
                The name of the option
        """
        return await self.cache.get_option_value(name)

    async def get_main_list_chats(self, limit: int = 25) -> list[Chat]:
        """
        Returns an ordered list of chats in a main chat list.
        Chats are sorted by the pair (chat.position.order, chat.id) in descending order
        """
        return await self.cache.get_main_list_chats(limit)

    async def get_chat(self, chat_id: int, *, force_update: bool = False) -> Chat:
        """
        Returns information about a chat by its identifier, this is an offline request if the current user is not a bot
        """
        return await self.cache.get_chat(chat_id, force_update=force_update)

    async def get_user(self, user_id: int, *, force_update: bool = False) -> User:
        return await self.cache.get_user(user_id, force_update=force_update)

    async def get_user_full_info(self, user_id: int, *, force_update: bool = False) -> UserFullInfo:
        return await self.cache.get_user_full_info(user_id, force_update=force_update)

    async def get_basic_group(self, basic_group_id: int, *, force_update: bool = False) -> BasicGroup:
        return await self.cache.get_basic_group(basic_group_id, force_update=force_update)

    async def get_basic_group_full_info(self, basic_group_id: int, *, force_update: bool = False) -> BasicGroupFullInfo:
        return await self.cache.get_basic_group_full_info(basic_group_id, force_update=force_update)

    async def get_supergroup(self, supergroup_id: int, *, force_update: bool = False) -> Supergroup:
        return await self.cache.get_supergroup(supergroup_id, force_update=force_update)

    async def get_supergroup_full_info(self, supergroup_id: int, *, force_update: bool = False) -> SupergroupFullInfo:
        return await self.cache.get_supergroup_full_info(supergroup_id, force_update=force_update)

    async def get_secret_chat(self, secret_chat_id: int, *, force_update: bool = False) -> SecretChat:
        return await self.cache.get_secret_chat(secret_chat_id, force_update=force_update)

    async def get_chat_info(
            self, 
            chat: Union[int, Chat], 
            *, 
            full: bool = False, 
            force_update: bool = False
    ) -> Optional[ChatInfo]:
        chat = await self.get_chat(chat) if isinstance(chat, int) else chat

        if isinstance(chat.type_, ChatTypePrivate):
            if full:
                return await self.get_user_full_info(chat.type_.user_id, force_update=force_update)
            else:
                return await self.get_user(chat.type_.user_id, force_update=force_update)

        if isinstance(chat.type_, ChatTypeBasicGroup):
            if full:
                return await self.get_basic_group_full_info(chat.type_.basic_group_id, force_update=force_update)
            else:
                return await self.get_basic_group(chat.type_.basic_group_id, force_update=force_update)

        if isinstance(chat.type_, ChatTypeSupergroup):
            if full:
                return await self.get_supergroup_full_info(chat.type_.supergroup_id, force_update=force_update)
            else:
                return await self.get_supergroup(chat.type_.supergroup_id, force_update=force_update)

        if isinstance(chat.type_, ChatTypeSecret):
            return await self.get_secret_chat(chat.type_.secret_chat_id, force_update=force_update)

        raise ValueError(f'Unknown chat.type {chat.type_.__class__.__qualname__}')

    # API methods shorthands
    async def parse_text(self, text: str, *, parse_mode: str = None) -> Optional[FormattedText]:
        """
        Parses Bold, Italic, Underline, Strikethrough, Code, Pre, PreCode,
        TextUrl and MentionName entities contained in the text.
        """
        if text is None:
            return None

        # ParseTextEntities can be called synchronously
        if parse_mode is None:
            parse_mode = self.parse_mode
        else:
            parse_mode = parse_mode.lower()

        return await self.execute(
            ParseTextEntities(
                text=text,
                parse_mode=(
                    TextParseModeHTML()
                    if parse_mode == 'html' else
                    TextParseModeMarkdown(version=2)
                )
            )
        )

    async def __send_message(
            self,
            chat_id: int,
            content: InputMessageContent,
            *,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a text message. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            content (:class:`InputMessageContent`)
                The content of the message to be sent

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

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
            input_message_content=content,
            skip_validation=True,
            request_timeout=request_timeout
        )

    async def send_text(
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
            send_date: int = None,
            request_timeout: int = None
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
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageText.construct(
                text=(await self.parse_text(text)),
                disable_web_page_preview=disable_web_page_preview,
                clear_draft=clear_draft,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def edit_text(
            self,
            chat_id: int,
            message_id: int,
            text: str,
            *,
            reply_markup: ReplyMarkup = None,
            disable_web_page_preview: bool = False,
            clear_draft: bool = True,
            request_timeout: int = None
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
            skip_validation=True,
            request_timeout=request_timeout
        )

    async def send_photo(
            self,
            chat_id: int,
            photo: str,
            *,
            caption: str = None,
            added_sticker_file_ids: list[int] = None,
            photo_width: int = None,
            photo_height: int = None,
            ttl: int = None,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a photo with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            photo (:class:`str`)
                Photo to send. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Photo caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            photo_width (:class:`int`)
                Photo width

            photo_height (:class:`int`)
                Photo height

            ttl (:class:`int`)
                Photo TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats

            thumbnail (:class:`str`)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(photo):
            photo_input_file = InputFileLocal(path=photo)
        else:
            photo_input_file = InputFileRemote(id=photo)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessagePhoto.construct(
                caption=(await self.parse_text(caption)),
                photo=photo_input_file,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                width=photo_width,
                height=photo_height,
                ttl=ttl,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_video(
            self,
            chat_id: int,
            video: str,
            *,
            caption: str = None,
            added_sticker_file_ids: list[int] = None,
            duration: int = None,
            video_width: int = None,
            video_height: int = None,
            ttl: int = None,
            supports_streaming: bool = False,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a video with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            video (:class:`str`)
                Video to send. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Video caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            duration (:class:`int`)
                Duration of the video, in seconds

            video_width (:class:`int`)
                Video width

            video_height (:class:`int`)
                Video height

            ttl (:class:`int`)
                Video TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats

            supports_streaming (:class:`bool`)
                True, if the video should be tried to be streamed

            thumbnail (:class:`str`)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(video):
            video_input_file = InputFileLocal(path=video)
        else:
            video_input_file = InputFileRemote(id=video)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVideo.construct(
                caption=(await self.parse_text(caption)),
                video=video_input_file,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                duration=duration,
                width=video_width,
                height=video_height,
                ttl=ttl,
                supports_streaming=supports_streaming,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_animation(
            self,
            chat_id: int,
            animation: str,
            *,
            caption: str = None,
            added_sticker_file_ids: list[int] = None,
            duration: int = None,
            animation_width: int = None,
            animation_height: int = None,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends an animation with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            animation (:class:`str`)
                Animation to send. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Animation caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            duration (:class:`int`)
                Duration of the animation, in seconds

            animation_width (:class:`int`)
                Animation width

            animation_height (:class:`int`)
                Animation height

            thumbnail (:class:`str`)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(animation):
            animation_input_file = InputFileLocal(path=animation)
        else:
            animation_input_file = InputFileRemote(id=animation)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageAnimation.construct(
                caption=(await self.parse_text(caption)),
                animation=animation_input_file,
                thumbnail=thumbnail,
                added_sticker_file_ids=added_sticker_file_ids,
                duration=duration,
                width=animation_width,
                height=animation_height,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_document(
            self,
            chat_id: int,
            document: str,
            *,
            caption: str = None,
            disable_content_type_detection: bool = False,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a document with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            document (:class:`str`)
                Document to be sent. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Document caption

            disable_content_type_detection (:class:`bool`)
                If true, automatic file type detection will be disabled and the document will be always sent as file.
                Always true for files sent to secret chats

            thumbnail (:class:`str`)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(document):
            document_input_file = InputFileLocal(path=document)
        else:
            document_input_file = InputFileRemote(id=document)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageDocument.construct(
                document=document_input_file,
                caption=(await self.parse_text(caption)),
                thumbnail=thumbnail,
                disable_content_type_detection=disable_content_type_detection,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_audio(
            self,
            chat_id: int,
            audio: str,
            *,
            caption: str = None,
            duration: int = None,
            title: str = None,
            performer: str = None,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends an audio with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            audio (:class:`str`)
                Audio to be sent. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Audio caption

            duration (:class:`int`)
                Duration of the audio, in seconds; may be replaced by the server

            title (:class:`str`)
                Title of the audio; 0-64 characters; may be replaced by the server

            performer (:class:`str`)
                Performer of the audio; 0-64 characters, may be replaced by the server

            thumbnail (:class:`str`)
                Thumbnail of the cover for the album, if available.
                Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(audio):
            audio_input_file = InputFileLocal(path=audio)
        else:
            audio_input_file = InputFileRemote(id=audio)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageAudio.construct(
                audio=audio_input_file,
                caption=(await self.parse_text(caption)),
                album_cover_thumbnail=thumbnail,
                title=title,
                duration=duration,
                performer=performer
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_voice_note(
            self,
            chat_id: int,
            voice_note: str,
            *,
            caption: str = None,
            duration: int = None,
            waveform: str = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a voice note with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            voice_note (:class:`str`)
                Voice note to be sent. This parameter could be ether path to local file or remote file_id

            caption (:class:`str`)
                Voice note caption

            duration (:class:`int`)
                Duration of the audio, in seconds; may be replaced by the server

            waveform (:class:`str`)
                Waveform representation of the voice note, in 5-bit format

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(voice_note):
            voice_note_input_file = InputFileLocal(path=voice_note)
        else:
            voice_note_input_file = InputFileRemote(id=voice_note)

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVoiceNote.construct(
                voice_note=voice_note_input_file,
                caption=(await self.parse_text(caption)),
                duration=duration,
                waveform=waveform
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def send_video_note(
            self,
            chat_id: int,
            video_note: str,
            *,
            duration: int = None,
            length: int = None,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None
    ):
        """
        Sends a video note with caption to chat. Returns the sent message

        Params:
            chat_id (:class:`int`)
                Target chat

            video_note (:class:`str`)
                Video note to be sent. This parameter could be ether path to local file or remote file_id

            duration (:class:`int`)
                Duration of the video, in seconds

            length (:class:`int`)
                Video width and height; must be positive and not greater than 640

            thumbnail (:class:`str`)
                Video note thumbnail, if available
                Sending thumbnails by file_id is currently not supported

            thumbnail_width (:class:`int`)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (:class:`int`)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (:class:`int`)
                Identifier of the message to reply to or 0

            reply_markup (:class:`ReplyMarkup`)
                Markup for replying to the message; for bots only

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

            send_when_online: (:class:`bool`)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (:class:`int`)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

        """

        if os.path.exists(video_note):
            video_note_input_file = InputFileLocal(path=video_note)
        else:
            video_note_input_file = InputFileRemote(id=video_note)

        if isinstance(thumbnail, str):
            thumbnail = InputThumbnail.construct(
                # Sending thumbnails by file_id is currently not supported
                thumbnail=InputFileLocal(path=thumbnail),
                width=thumbnail_width,
                height=thumbnail_height,
            )

        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVideoNote.construct(
                video_note=video_note_input_file,
                thumbnail=thumbnail,
                length=length,
                duration=duration,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout
        )

    async def forward_messages(
            self,
            from_chat_id: int,
            chat_id: int,
            message_ids: list[int],
            *,
            send_copy: bool = False,
            remove_caption: bool = False,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None,
    ) -> Messages:
        """
        Forwards previously sent messages.
        Returns the forwarded messages in the same order as the message identifiers passed in message_ids.
        If a message can't be forwarded, null will be returned instead of the message

        Params:
            from_chat_id (:class:`int`)
                Identifier of the chat from which to forward messages

            chat_id (:class:`int`)
                Identifier of the chat to which to forward messages

            message_ids (:obj:`list[int]`)
                Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order.
                At most 100 messages can be forwarded simultaneously

            send_copy (:class:`bool`)
                True, if content of the messages needs to be copied without links to the original messages.
                Always true if the messages are forwarded to a secret chat

            remove_caption (:class:`bool`)
                True, if media caption of message copies needs to be removed. Ignored if send_copy is false

            disable_notification (:class:`bool`)
                Pass true to disable notification for the message

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

        return await self.api.forward_messages(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_ids=message_ids,
            options=MessageSendOptions.construct(
                disable_notification=disable_notification,
                from_background=False,
                scheduling_state=scheduling_state
            ),
            send_copy=send_copy,
            remove_caption=remove_caption,
            request_timeout=request_timeout,
            skip_validation=True
        )

    async def iter_chat_history(
            self,
            chat_id: int,
            from_message_id: int = 0,
            limit: int = None,
            only_local: bool = False
    ) -> AsyncIterator[Message]:
        """
        Iterates over messages in a chat.
        The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id).
        Number of messages are limited by limit parameter

        Params:
            chat_id (:class:`int`)
                Chat identifier

            from_message_id (:class:`int`)
                Identifier of the message starting from which history must be fetched;
                use 0 to get results from the last message

            limit (:class:`int`)
                The maximum number of messages to be returned; must be positive
                If chat contains less than limit messages all of them would be returned

            only_local (:class:`bool`)
                If true, returns only messages that are available locally without sending network requests

        """

        if limit is None:
            limit = 100

        yielded_messages_count = 0
        need_finish = False
        request_limit = min(100, limit)

        while not need_finish:
            history = await self.api.get_chat_history(
                chat_id=chat_id,
                from_message_id=from_message_id,
                limit=request_limit,
                offset=0,
                only_local=only_local
            )

            if len(history.messages) == 0:
                break

            from_message_id = history.messages[-1].id

            for message in history.messages:
                yield message
                yielded_messages_count += 1

                if yielded_messages_count >= limit:
                    need_finish = True
                    break

            request_limit = min(100, limit - yielded_messages_count)

    async def _run(self):
        async with self:
            await self.idle()

    def run(self):
        asyncio.run(self._run())
