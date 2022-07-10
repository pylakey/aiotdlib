from __future__ import annotations

import asyncio
import enum
import hashlib
import logging
import os
import sys
import typing
import uuid
from functools import (
    partial,
    update_wrapper,
)
from pathlib import Path
from typing import (
    AsyncIterator,
    Optional,
    Union,
)

import pydantic.errors
from pydantic import (
    BaseModel,
    root_validator,
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
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageContent,
    InputMessageDocument,
    InputMessagePhoto,
    InputMessageSticker,
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
from .api import (
    BadRequest,
    OptionValueBoolean,
    OptionValueEmpty,
    OptionValueInteger,
    OptionValueString,
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
    TDLIB_MAX_INT,
    TDLibLogVerbosity,
)
from .utils import (
    PendingRequest,
    ainput,
    make_input_file,
    make_thumbnail,
    str_to_base64,
    strip_phone_number_symbols,
)

RequestResult = typing.TypeVar('RequestResult', bound=BaseObject)
ExecuteResult = typing.TypeVar('ExecuteResult', bound=BaseObject)
ChatInfo = Union[
    User,
    UserFullInfo,
    BasicGroup,
    BasicGroupFullInfo,
    Supergroup,
    SupergroupFullInfo,
    SecretChat
]
AuthActionsDict = dict[Optional[str], typing.Callable[[], typing.Coroutine[typing.Any, typing.Any, RequestResult]]]


class ClientProxyType(str, enum.Enum):
    MTPROTO = 'mtproto'
    HTTP = 'http'
    SOCKS5 = 'socks5'


# noinspection PyUnresolvedReferences
class ClientProxySettings(BaseModel):
    """
    Universal proxy settings object for all proxy types

    :param host: Proxy server IP address
    :type host: str

    :param port: Proxy server port
    :type port: int

    :param type: Proxy type
    :type type: ClientProxySettingsType

    :param username: Username for logging in; may be empty
    :type username: str

    :param password: Password for logging in; may be empty
    :type password: str

    :param http_only: Pass true if the proxy supports only HTTP requests and doesn't support
    transparent TCP connections via HTTP CONNECT method
    :type http_only: bool

    :param secret: The proxy's secret in hexadecimal encoding
    :type secret: str
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


class ClientParseMode(str, enum.Enum):
    HTML = 'html'
    MARKDOWN = 'markdown'


class ClientOptions(pydantic.BaseModel):
    always_parse_markdown: Optional[bool]
    """
    If true, text entities will be automatically parsed in all inputMessageText objects
    """

    archive_and_mute_new_chats_from_unknown_users: Optional[bool]
    """
    If true, new chats from non-contacts will be automatically archived and muted. 
    The option can be set only if the option “can_archive_and_mute_new_chats_from_unknown_users” is true. 
    getOption needs to be called explicitly to fetch the latest value of the option, changed from another device
    """

    disable_contact_registered_notifications: Optional[bool]
    """
    If true, notifications about the user's contacts who have joined Telegram will be disabled. 
    User will still receive the corresponding message in the private chat. 
    getOption needs to be called explicitly to fetch the latest value of the option, changed from another device
    """

    disable_persistent_network_statistics: Optional[bool] = True
    """
    If true, persistent network statistics will be disabled, which significantly reduces disk usage
    """

    disable_sent_scheduled_message_notifications: Optional[bool] = True
    """
    If true, notifications about outgoing scheduled messages that were sent will be disabled
    """

    disable_time_adjustment_protection: Optional[bool] = True
    """
    If true, protection from external time adjustment will be disabled, which significantly reduces disk usage
    """

    disable_top_chats: Optional[bool]
    """
    If true, support for top chats and statistics collection is disabled
    """

    ignore_background_updates: Optional[bool]
    """
    If true, allows to skip all updates received while the TDLib instance was not running. 
    The option does nothing if the database or secret chats are used
    """

    ignore_default_disable_notification: Optional[bool]
    """
    If true, the disable_notification value specified in the request will be always used instead of the default value
    """

    ignore_inline_thumbnails: Optional[bool] = True
    """
    If true, prevents file thumbnails sent by the server along with messages from being saved on the disk
    """

    ignore_platform_restrictions: Optional[bool] = True
    """
    If true, chat and message reictions specific to the currently used operating system will be ignored
    """

    is_location_visible: Optional[bool] = False
    """
    If true, other users will be allowed to see the current user's location
    """

    # language_pack_database_path: Optional[str]
    # """
    # Path to a database for storing language pack strs, so that this database can be shared between different accounts.
    # By default, language pack Optional[str]s are stored only in memory.
    # Changes of value of this option will be applied only after TDLib restart,
    # so it should be set before call to setTdlibParameters.
    # """

    language_pack_id: Optional[str]
    """
    Identifier of the currently used language pack from the current localization target
    """

    localization_target: Optional[str]
    """
    Name for the current localization target (currently supported: “android”,“android_x”,“ios”,“macos” and “tdesktop”)
    """

    message_unload_delay: Optional[int]
    """
    The maximum time messages are stored in memory before they are unloaded, 60-86400; in seconds. 
    Defaults to 60 for users and 1800 for bots
    """

    notification_group_count_max: Optional[int]
    """
    Maximum number of notification groups to be shown simultaneously, 0-25
    """

    notification_group_size_max: Optional[int]
    """
    Maximum number of simultaneously shown notifications in a group, 1-25. Defaults to 10
    """

    online: Optional[bool]
    """
    Online status of the current user
    """

    prefer_ipv6: Optional[bool]
    """
    If true, IPv6 addresses will be preferred over IPv4 addresses
    """

    use_pfs: Optional[bool]
    """
    If true, Perfect Forward Secrecy will be enabled for interaction with the Telegram servers for cloud chats
    """

    use_quick_ack: Optional[bool]
    """
    If true, quick acknowledgement will be enabled for outgoing messages
    """

    use_storage_optimizer: Optional[bool] = True
    """
    If true, the background storage optimizer will be enabled
    """


# noinspection PyUnresolvedReferences
class ClientSettings(pydantic.BaseSettings):
    """
    :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
    :type api_id: int

    :param api_hash: Application identifier hash for Telegram API access,
    which can be obtained at https://my.telegram.org
    :type api_hash: str

    :param database_encryption_key: Encryption key of local session database. Default: aiotdlib
    :type database_encryption_key: str

    :param phone_number: The phone number of the user, in international format.
    Either phone_number or bot_token MUST be passed. ValueError would be raised otherwise
    :type phone_number: str

    :param bot_token: The bot token. Either phone_number or bot_token MUST be passed.
    ValueError would be raised otherwise
    :type bot_token: str

    :param use_test_dc: If set to true, the Telegram test environment will be used instead of the production environment
    :type use_test_dc: bool

    :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
    :type system_language_code: str

    :param device_model: Model of the device the application is being run on; must be non-empty
    :type device_model: str

    :param system_version: Version of the operating system the application is being run on.
    If empty, the version is automatically detected by TDLib
    :type system_version: str

    :param application_version: Application version; must be non-empty
    :type application_version: str

    :param files_directory: The path to the directory for storing files. Default: .aiotdlib/
    :type files_directory: str

    :param first_name: First name of new account if account with passed phone_number does not exist
    :type first_name: str

    :param last_name: Last name of new account if account with passed phone_number does not exist
    :type last_name: str

    :param library_path: Path to TDLib binary. By default binary included in package is used
    :type library_path: str

    :param tdlib_verbosity: Verbosity level of TDLib itself.
    Default: 2 (WARNING) for more info look at (TDLibLogVerbosity)
    :type tdlib_verbosity: str

    :param debug: When set to true all request and responses would be logged in console with DEBUG level
    :type debug: bool

    :param parse_mode: Default parse mode for high-level methods like send_message. Default: html
    :type parse_mode: str

    :param proxy_settings: Settings for proxying telegram connection
    :type proxy_settings: aiotdlib.ClientProxySettings

    """
    api_id: int
    api_hash: pydantic.SecretStr
    database_encryption_key: Union[str, bytes] = 'aiotdlib'
    phone_number: str = None
    bot_token: pydantic.SecretStr = None
    use_test_dc: bool = False
    system_language_code: str = 'en'
    device_model: str = 'aiotdlib'
    system_version: str = ""
    application_version: str = __version__
    files_directory: Path = Path(sys.argv[0]).parent
    first_name: str = None
    last_name: str = None
    password: pydantic.SecretStr = None
    library_path: str = None
    tdlib_verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR
    debug: bool = False
    parse_mode: ClientParseMode = ClientParseMode.HTML
    proxy_settings: ClientProxySettings = None
    use_file_database: bool = True
    use_chat_info_database: bool = True
    use_message_database: bool = True
    use_secret_chats: bool = True
    enable_storage_optimizer: bool = True
    ignore_file_names: bool = True
    ignore_background_updates: bool = False
    options: ClientOptions = ClientOptions()

    @root_validator(pre=True)
    def check_phone_and_bot_token(cls, values):
        if not bool(values.get('phone_number')) and not bool(values.get('bot_token')):
            raise ValueError('Either phone_number or bot_token should be specified')

        return values

    @validator('parse_mode', pre=True)
    def validator_parse_mode(cls, value):
        if isinstance(value, str):
            return value.lower()

        return value

    @validator('phone_number')
    def validator_phone_number(cls, value):
        if bool(value):
            return strip_phone_number_symbols(value)

        return value

    @validator('database_encryption_key', pre=True)
    def validator_database_encryption_key(cls, value):
        if not bool(value):
            return value

        return str_to_base64(value)

    @validator('files_directory', always=True)
    def validator_files_directory(cls, value, values):
        if not bool(value):
            value = Path(sys.argv[0]).parent

        md5_hash = hashlib.md5()
        phone_number = values.get('phone_number')
        bot_token = values.get('bot_token')

        if bool(phone_number):
            session_name = str(phone_number)
        elif bool(bot_token):
            session_name = str(bot_token)
        else:
            raise ValueError

        md5_hash.update(session_name.encode('utf-8'))
        directory_name = md5_hash.hexdigest()

        return value / '.aiotdlib' / directory_name

    class Config:
        env_prefix = 'aiotdlib_'
        use_enum_values = True
        allow_population_by_field_name = True


Undefined = object()


class Client:
    loop: asyncio.AbstractEventLoop = None
    __current_authorization_state = None
    __is_authorized = False
    __running = False
    __pending_requests: dict[str, PendingRequest] = {}
    __pending_messages: dict[str, Message] = {}
    __updates_handlers: dict[str, set[Handler]] = {}
    __middlewares: list[MiddlewareCallable] = []
    __middlewares_handlers: list[MiddlewareCallable] = []

    def __init__(
            self,
            api_id: int = Undefined,
            api_hash: pydantic.SecretStr = Undefined,
            database_encryption_key: Union[str, bytes] = Undefined,
            phone_number: str = Undefined,
            bot_token: pydantic.SecretStr = Undefined,
            use_test_dc: bool = Undefined,
            system_language_code: str = Undefined,
            device_model: str = Undefined,
            system_version: str = Undefined,
            application_version: str = Undefined,
            files_directory: Path = Undefined,
            first_name: str = Undefined,
            last_name: str = Undefined,
            password: pydantic.SecretStr = Undefined,
            library_path: str = Undefined,
            tdlib_verbosity: TDLibLogVerbosity = Undefined,
            debug: bool = Undefined,
            parse_mode: ClientParseMode = Undefined,
            proxy_settings: ClientProxySettings = Undefined,
            use_file_database: bool = Undefined,
            use_chat_info_database: bool = Undefined,
            use_message_database: bool = Undefined,
            use_secret_chats: bool = Undefined,
            enable_storage_optimizer: bool = Undefined,
            ignore_file_names: bool = Undefined,
            options: ClientOptions = Undefined
    ):
        """
        :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
        :type api_id: int

        :param api_hash: Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
        :type api_hash: str

        :param database_encryption_key: Encryption key of local session database. Default: aiotdlib
        :type database_encryption_key: str

        :param phone_number: The phone number of the user, in international format.
        :type phone_number: str Either phone_number or bot_token MUST be passed. ValueError would be raised otherwise

        :param bot_token: The bot token. Either phone_number or bot_token MUST be passed. ValueError would be raised otherwise
        :type bot_token: str

        :param use_test_dc: If set to true, the Telegram test environment will be used instead of the production environment
        :type use_test_dc: bool

        :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
        :type system_language_code: str

        :param device_model: Model of the device the application is being run on; must be non-empty
        :type device_model: str

        :param system_version: Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
        :type system_version: str

        :param application_version: Application version; must be non-empty
        :type application_version: str

        :param files_directory: The path to the directory for storing files. Default: .aiotdlib/
        :type files_directory: str

        :param first_name: First name of new account if account with passed phone_number does not exist
        :type first_name: str

        :param last_name: Last name of new account if account with passed phone_number does not exist
        :type last_name: str

        :param library_path: Path to TDLib binary. By default, binary included in package is used
        :type library_path: str

        :param tdlib_verbosity: Verbosity level of TDLib itself. Default: 2 (WARNING) for more info look at (TDLibLogVerbosity)
        :type tdlib_verbosity: str

        :param debug: When set to true all request and responses would be logged in console with DEBUG level
        :type debug: bool

        :param parse_mode: Default parse mode for high-level methods like send_message. Default: html
        :type parse_mode: str

        :param proxy_settings: Settings for proxying telegram connection
        :type proxy_settings: ClientProxySettings

        :param use_file_database: If set to true, information about downloaded and uploaded files will be saved between application restarts
        :type use_file_database: bool

        :param use_chat_info_database: If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies use_file_database
        :type use_chat_info_database: bool

        :param use_message_database: If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database
        :type use_message_database: bool

        :param use_secret_chats: If set to true, support for secret chats will be enabled
        :type use_secret_chats: bool

        :param enable_storage_optimizer: If set to true, old files will automatically be deleted
        :type enable_storage_optimizer: bool

        :param ignore_file_names: If set to true, original file names will be ignored. Otherwise, downloaded files will be saved under names as close as possible to the original name
        :type ignore_file_names: bool

        :param options: Writable TDLib options (Check the list of available options on https://core.telegram.org/tdlib/options.)
        :type options: ClientOptions

        """
        settings = {
            'api_id': api_id,
            'api_hash': api_hash,
            'database_encryption_key': database_encryption_key,
            'phone_number': phone_number,
            'bot_token': bot_token,
            'use_test_dc': use_test_dc,
            'system_language_code': system_language_code,
            'device_model': device_model,
            'system_version': system_version,
            'application_version': application_version,
            'files_directory': files_directory,
            'first_name': first_name,
            'last_name': last_name,
            'password': password,
            'library_path': library_path,
            'tdlib_verbosity': tdlib_verbosity,
            'debug': debug,
            'parse_mode': parse_mode,
            'proxy_settings': proxy_settings,
            'use_file_database': use_file_database,
            'use_chat_info_database': use_chat_info_database,
            'use_message_database': use_message_database,
            'use_secret_chats': use_secret_chats,
            'enable_storage_optimizer': enable_storage_optimizer,
            'ignore_file_names': ignore_file_names,
            'options': options,
        }
        settings = {k: v for k, v in settings.items() if v is not Undefined}
        self.settings = ClientSettings(**settings)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG if self.settings.debug else logging.INFO)
        self.__tdjson = TDJson(library_path=self.settings.library_path, verbosity=self.settings.tdlib_verbosity)
        self.api = API(self)
        self.cache = ClientCache(self)

    @property
    def is_bot(self) -> bool:
        return bool(self.settings.bot_token)

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
            pending_message_key = f"{update.message.chat_id}_{update.old_message_id}"
            pending_message = self.__pending_messages.pop(pending_message_key, None)

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

    async def _setup_proxy(self):
        if not bool(self.settings.proxy_settings):
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

        if self.settings.debug:
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
                    p.server == self.settings.proxy_settings.host and
                    p.port == self.settings.proxy_settings.port and
                    proxy_type_by_class.get(p.type_.__class__) == self.settings.proxy_settings.type
            ):
                if not p.is_enabled:
                    await self.api.enable_proxy(p.id)

                return

        if self.settings.proxy_settings.type == ClientProxyType.HTTP:
            proxy_type = ProxyTypeHttp.construct(
                username=self.settings.proxy_settings.username,
                password=self.settings.proxy_settings.password,
                http_only=self.settings.proxy_settings.http_only
            )
        elif self.settings.proxy_settings.type == ClientProxyType.MTPROTO:
            proxy_type = ProxyTypeMtproto.construct(secret=self.settings.proxy_settings.secret)
        elif self.settings.proxy_settings.type == ClientProxyType.SOCKS5:
            proxy_type = ProxyTypeSocks5.construct(
                username=self.settings.proxy_settings.username,
                password=self.settings.proxy_settings.password,
            )
        else:
            raise ValueError(f'Unknown proxy type {self.settings.proxy_settings.type}')

        self.logger.info(
            f"Configuring PROXY of type {self.settings.proxy_settings.type.value}. "
            f"Server: {self.settings.proxy_settings.host}:{self.settings.proxy_settings.port}"
        )

        await self.api.add_proxy(
            enable=True,
            server=self.settings.proxy_settings.host,
            port=self.settings.proxy_settings.port,
            type_=proxy_type,
        )

    async def _setup_options(self):
        for k, v in self.settings.options.dict(exclude_none=True).items():
            if isinstance(v, bool):
                option_value = OptionValueBoolean(value=v)
            elif isinstance(v, str):
                option_value = OptionValueString(value=v)
            elif isinstance(v, int):
                option_value = OptionValueInteger(value=v)
            elif v is None:
                option_value = OptionValueEmpty()
            else:
                self.logger.warning(f"Option {k} has unsupported value of type {v.__class__.__name__}: {v}")
                continue

            self.logger.info(f'Setting up option {k} = {v}')

            try:
                await self.api.set_option(k, option_value, skip_validation=True)
            except BadRequest as e:
                self.logger.error(f'Unable to setup option {k} = {v}: {e}!')

    async def _auth_start(self) -> RequestResult:
        return await self.api.get_authorization_state(request_id="updateAuthorizationState")

    async def _set_tdlib_parameters(self) -> RequestResult:
        return await self.api.set_tdlib_parameters(
            parameters=TdlibParameters(
                use_test_dc=self.settings.use_test_dc,
                database_directory=os.path.join(f"{self.settings.files_directory}", "database"),
                files_directory=os.path.join(f"{self.settings.files_directory}", "files"),
                use_file_database=self.settings.use_file_database,
                use_chat_info_database=self.settings.use_chat_info_database,
                use_message_database=self.settings.use_message_database,
                use_secret_chats=self.settings.use_secret_chats,
                api_id=self.settings.api_id,
                api_hash=self.settings.api_hash.get_secret_value(),
                system_language_code=self.settings.system_language_code,
                device_model=self.settings.device_model,
                system_version=self.settings.system_version,
                application_version=self.settings.application_version,
                enable_storage_optimizer=self.settings.enable_storage_optimizer,
                ignore_file_names=self.settings.ignore_file_names
            ),
            request_id="updateAuthorizationState"
        )

    async def _check_database_encryption_key(self) -> RequestResult:
        self.logger.info('Sending encryption key')
        result = await self.api.check_database_encryption_key(
            encryption_key=self.settings.database_encryption_key,
            request_id="updateAuthorizationState"
        )

        await self._setup_options()
        await self._setup_proxy()

        return result

    async def _set_authentication_phone_number_or_check_bot_token(self) -> RequestResult:
        if self.is_bot:
            return await self._check_authentication_bot_token()

        return await self._set_authentication_phone_number()

    async def _set_authentication_phone_number(self) -> RequestResult:
        self.logger.info('Sending phone number')
        return await self.api.set_authentication_phone_number(
            phone_number=self.settings.phone_number,
            settings=PhoneNumberAuthenticationSettings(
                allow_flash_call=False,
                allow_missed_call=False,
                is_current_phone_number=True,
                allow_sms_retriever_api=False,
                authentication_tokens=[]
            ),
            request_id="updateAuthorizationState"
        )

    async def _check_authentication_bot_token(self) -> RequestResult:
        self.logger.info('Sending bot token')
        return await self.api.check_authentication_bot_token(
            self.settings.bot_token.get_secret_value(),
            request_id="updateAuthorizationState"
        )

    async def _check_authentication_code(self) -> RequestResult:
        code = await self._auth_get_code()
        self.logger.info(f'Sending code {code}')

        return await self.api.check_authentication_code(
            code=code,
            request_id="updateAuthorizationState"
        )

    async def _register_user(self) -> RequestResult:
        first_name = await self._auth_get_first_name()
        last_name = await self._auth_get_last_name()
        self.logger.info(f'Registering new user in telegram as {first_name} {last_name or ""}'.strip())

        return await self.api.register_user(
            first_name=first_name,
            last_name=last_name,
            request_id="updateAuthorizationState"
        )

    async def _check_authentication_password(self) -> RequestResult:
        password = await self._auth_get_password()
        self.logger.info('Sending password')

        return await self.api.check_authentication_password(
            password=password,
            request_id="updateAuthorizationState"
        )

    # noinspection PyMethodMayBeStatic
    async def _auth_get_code(self) -> str:
        code = ""

        while len(code) != 5 or not code.isdigit():
            code = await ainput('Enter code:')

        return code

    async def _auth_get_password(self) -> str:
        password = self.settings.password

        if not bool(password):
            password = await ainput('Enter 2FA password:', secured=True)
        else:
            password = password.get_secret_value()

        return password

    async def _auth_get_first_name(self) -> str:
        first_name = self.settings.first_name or ""

        while not bool(first_name) or len(first_name) > 64:
            first_name = await ainput('Enter first name:')

        return first_name

    async def _auth_get_last_name(self) -> str:
        last_name = self.settings.last_name or ""

        if not bool(last_name):
            last_name = await ainput('Enter last name:')

        return last_name

    async def _auth_completed(self):
        self.__pending_requests.pop('updateAuthorizationState', None)

        if not self.is_bot:
            # Preload main list chats
            await self.get_main_list_chats()

        self.__is_authorized = True
        self.logger.info('Authorization is completed')

    async def _auth_logging_out(self):
        self.__is_authorized = False
        self.logger.info('Auth session is logging out')

    async def _auth_closing(self):
        self.__is_authorized = False
        self.logger.info('Auth session is closing')

    async def _auth_closed(self):
        self.logger.info('Auth session is closed')

    async def send(self, query: BaseObject):
        if not self.__running:
            raise RuntimeError('Client not started')

        if self.settings.debug:
            self.logger.debug(f">>>>> {query.ID} {query.json(by_alias=True)}")

        await self.loop.run_in_executor(None, self.__tdjson.send, query.dict(by_alias=True))

    async def request(
            self,
            query: BaseObject,
            *,
            request_id: str = None,
            request_timeout: int = None
    ) -> Optional[RequestResult]:
        if request_id is None:
            request_id = query.EXTRA.get('request_id') or uuid.uuid4().hex

        if request_timeout is None:
            request_timeout = 10

        query.EXTRA['request_id'] = request_id
        pending_request = PendingRequest(self, query)
        self.__pending_requests[request_id] = pending_request

        try:
            await self.send(query)
            await pending_request.wait(raise_exc=True, timeout=request_timeout)
        except asyncio.TimeoutError:
            self.__pending_requests.pop(request_id, None)
            raise
        finally:
            if self.settings.debug and bool(pending_request.update):
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

    async def authorize(self):
        if self.is_bot:
            self.logger.info('Authorization process has been started with bot token')
        else:
            self.logger.info('Authorization process has been started with phone')

        auth_actions: AuthActionsDict = {
            None: self._auth_start,
            API.Types.AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS: self._set_tdlib_parameters,
            API.Types.AUTHORIZATION_STATE_WAIT_ENCRYPTION_KEY: self._check_database_encryption_key,
            API.Types.AUTHORIZATION_STATE_WAIT_PHONE_NUMBER: self._set_authentication_phone_number_or_check_bot_token,
            API.Types.AUTHORIZATION_STATE_WAIT_CODE: self._check_authentication_code,
            API.Types.AUTHORIZATION_STATE_WAIT_REGISTRATION: self._register_user,
            API.Types.AUTHORIZATION_STATE_WAIT_PASSWORD: self._check_authentication_password,
            API.Types.AUTHORIZATION_STATE_READY: self._auth_completed,
            API.Types.AUTHORIZATION_STATE_LOGGING_OUT: self._auth_logging_out,
            API.Types.AUTHORIZATION_STATE_CLOSING: self._auth_closing,
            API.Types.AUTHORIZATION_STATE_CLOSED: self._auth_closed,
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

    async def start(self) -> 'Client':
        self.logger.info('Starting client')
        self.logger.info(f'Session workdir: {self.settings.files_directory.absolute()}')

        # Preparing middlewares handlers
        self.__middlewares_handlers = list(reversed(self.__middlewares))

        # Setting up asyncio stuff
        self.loop = asyncio.get_running_loop()

        # Starting updates loop
        self.__running = True
        self.loop.create_task(self.__updates_loop())

        # Initialize authorization process
        await self.authorize()
        return self

    async def idle(self):
        try:
            while True:
                await asyncio.sleep(0.1)
        finally:
            self.logger.info('Stop Idling...')

    async def stop(self):
        self.logger.info('Stopping telegram client...')
        await self.__close()
        self.__running = False

    async def _run(self):
        async with self:
            await self.idle()

    def run(self):
        asyncio.run(self._run())

    # Cache related methods
    async def get_option_value(self, name: str) -> typing.Union[str, int, bool, None]:
        """
        Returns the value of an option by its name.
        (Check the list of available options on https://core.telegram.org/tdlib/options.)
        Can be called before authorization

        :param name: The name of the option
        :type name: str

        """
        return await self.cache.get_option_value(name)

    async def get_main_list_chats(self, limit: int = 100) -> list[Chat]:
        """
        Returns an ordered list of chats in a main chat list.
        Chats are sorted by the pair (chat.position.order, chat.id) in descending order

        :param limit: Maximum amount of chats to be returned
        :type limit: int

        """
        return await self.cache.get_main_list_chats(limit)

    async def get_main_list_chats_all(self) -> list[Chat]:
        return await self.get_main_list_chats(limit=TDLIB_MAX_INT)

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
            parse_mode = self.settings.parse_mode
        else:
            parse_mode = parse_mode.lower()

        return await self.execute(
            ParseTextEntities(
                text=text,
                parse_mode=(
                    TextParseModeHTML()
                    if parse_mode == ClientParseMode.HTML else
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a text message. Returns the sent message

        Args:
        :param chat_id: Target chat
        :type chat_id: :class:`int`

        :param content: The content of the message to be sent
        :type content: :class:`InputMessageContent`

        :param reply_to_message_id: Identifier of the message to reply to or 0
        :type reply_to_message_id: :class:`int`

        :param reply_markup: Markup for replying to the message; for bots only
        :type reply_markup: :class:`ReplyMarkup`

        :param disable_notification: Pass true to disable notification for the message
        :type disable_notification: :class:`bool`

        :param send_when_online: When True, the message will be sent when the peer will be online. Applicable to private chats only and when the exact online status of the peer is known
        :type send_when_online: :class:`bool`

        :param send_date: Date the message will be sent. The date must be within 367 days in the future. If send_date passed send_when_online will be ignored
        :type send_date: :class:`int`

        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving; for bots only
        :type protect_content: :class:`bool`

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
                protect_content=protect_content,
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
            request_timeout: int = None,
            protect_content: bool = False,
    ) -> Message:
        """
        Sends a text message. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            text (str)
                The text

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            disable_web_page_preview (bool)
                True, if rich web page previews for URLs in the message text should be disabled

            clear_draft (bool)
                True, if a chat message draft should be deleted

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

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
            request_timeout=request_timeout,
            protect_content=protect_content
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

        Args:
            chat_id (int)
                The chat the message belongs to

            message_id (int)
                Identifier of the message

            text (str)
                New text of the message

            reply_markup (ReplyMarkup)
                The new message reply markup; for bots only

            disable_web_page_preview (bool)
                True, if rich web page previews for URLs in the message text should be disabled

            clear_draft (bool)
                True, if a chat message draft should be deleted

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a photo with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            photo (str)
                Photo to send. This parameter could be ether path to local file or remote file_id

            caption (str)
                Photo caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            photo_width (int)
                Photo width

            photo_height (int)
                Photo height

            ttl (int)
                Photo TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats

            thumbnail (str)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessagePhoto.construct(
                caption=(await self.parse_text(caption)),
                photo=make_input_file(photo),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
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
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a video with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            video (str)
                Video to send. This parameter could be ether path to local file or remote file_id

            caption (str)
                Video caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            duration (int)
                Duration of the video, in seconds

            video_width (int)
                Video width

            video_height (int)
                Video height

            ttl (int)
                Video TTL (Time To Live), in seconds (0-60). A non-zero TTL can be specified only in private chats

            supports_streaming (bool)
                True, if the video should be tried to be streamed

            thumbnail (str)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVideo.construct(
                caption=(await self.parse_text(caption)),
                video=make_input_file(video),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
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
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends an animation with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            animation (str)
                Animation to send. This parameter could be ether path to local file or remote file_id

            caption (str)
                Animation caption

            added_sticker_file_ids (:obj:`list[int]`)
                File identifiers of the stickers added to the photo, if applicable

            duration (int)
                Duration of the animation, in seconds

            animation_width (int)
                Animation width

            animation_height (int)
                Animation height

            thumbnail (str)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageAnimation.construct(
                caption=(await self.parse_text(caption)),
                animation=make_input_file(animation),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
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
            request_timeout=request_timeout,
            protect_content=protect_content
        )

    async def send_sticker(
            self,
            chat_id: int,
            sticker: str,
            *,
            sticker_width: int = None,
            sticker_height: int = None,
            thumbnail: Union[str, InputThumbnail] = None,
            thumbnail_width: int = None,
            thumbnail_height: int = None,
            emoji: str = None,
            reply_to_message_id: int = None,
            reply_markup: ReplyMarkup = None,
            disable_notification: bool = False,
            send_when_online: bool = False,
            send_date: int = None,
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends an sticker to chat. Returns the sent message
        Args:
            chat_id (int)
                Target chat

            sticker(str)
                Sticker to send. This parameter could be ether path to local file or remote file_id

            sticker_width (int)
                Sticker width

            sticker_height (int)
                Sticker height

            emoji (str)
                Emoji used to choose the sticker

            thumbnail (str)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only
        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageSticker.construct(
                sticker=make_input_file(sticker),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                width=sticker_width,
                height=sticker_height,
                emoji=emoji
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a document with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            document (str)
                Document to be sent. This parameter could be ether path to local file or remote file_id

            caption (str)
                Document caption

            disable_content_type_detection (bool)
                If true, automatic file type detection will be disabled and the document will be always sent as file.
                Always true for files sent to secret chats

            thumbnail (str)
                Thumbnail file to send. Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageDocument.construct(
                document=make_input_file(document),
                caption=(await self.parse_text(caption)),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                disable_content_type_detection=disable_content_type_detection,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends an audio with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            audio (str)
                Audio to be sent. This parameter could be ether path to local file or remote file_id

            caption (str)
                Audio caption

            duration (int)
                Duration of the audio, in seconds; may be replaced by the server

            title (str)
                Title of the audio; 0-64 characters; may be replaced by the server

            performer (str)
                Performer of the audio; 0-64 characters, may be replaced by the server

            thumbnail (str)
                Thumbnail of the cover for the album, if available.
                Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageAudio.construct(
                audio=make_input_file(audio),
                caption=(await self.parse_text(caption)),
                album_cover_thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                title=title,
                duration=duration,
                performer=performer
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a voice note with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            voice_note (str)
                Voice note to be sent. This parameter could be ether path to local file or remote file_id

            caption (str)
                Voice note caption

            duration (int)
                Duration of the audio, in seconds; may be replaced by the server

            waveform (str)
                Waveform representation of the voice note, in 5-bit format

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVoiceNote.construct(
                voice_note=make_input_file(voice_note),
                caption=(await self.parse_text(caption)),
                duration=duration,
                waveform=waveform
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content
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
            request_timeout: int = None,
            protect_content: bool = False,
    ):
        """
        Sends a video note with caption to chat. Returns the sent message

        Args:
            chat_id (int)
                Target chat

            video_note (str)
                Video note to be sent. This parameter could be ether path to local file or remote file_id

            duration (int)
                Duration of the video, in seconds

            length (int)
                Video width and height; must be positive and not greater than 640

            thumbnail (str)
                Video note thumbnail, if available
                Sending thumbnails by file_id is currently not supported

            thumbnail_width (int)
                Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown

            thumbnail_height (int)
                Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown

            reply_to_message_id (int)
                Identifier of the message to reply to or 0

            reply_markup (ReplyMarkup)
                Markup for replying to the message; for bots only

            disable_notification (bool)
                Pass true to disable notification for the message

            send_when_online: (bool)
                When True, the message will be sent when the peer will be online.
                Applicable to private chats only and when the exact online status of the peer is known

            send_date: (int)
                Date the message will be sent. The date must be within 367 days in the future.
                If send_date passed send_when_online will be ignored

            request_timeout: (int)
                amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`) will be be raised
                if request lasts more than `request_timeout` seconds, defaults to None

            protect_content: (bool)
                Pass true if the content of the message must be protected from forwarding and saving; for bots only

        """
        return await self.__send_message(
            chat_id=chat_id,
            content=InputMessageVideoNote.construct(
                video_note=make_input_file(video_note),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                length=length,
                duration=duration,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content
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
            only_preview: bool = False,
            from_background: bool = False,
            send_date: int = None,
            request_timeout: int = None,
            protect_content: bool = False,
    ) -> Messages:
        """
        Forwards previously sent messages.
        Returns the forwarded messages in the same order as the message identifiers passed in message_ids.
        If a message can't be forwarded, null will be returned instead of the message

        :param chat_id: Identifier of the chat to which to forward messages
        :type chat_id: int

        :param from_chat_id: Identifier of the chat from which to forward messages
        :type from_chat_id: int

        :param message_ids: Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
        :type message_ids: list[int]

        :param send_copy: If true, content of the messages will be copied without reference to the original sender. Always true if the messages are forwarded to a secret chat or are local
        :type send_copy: bool

        :param remove_caption: If true, media caption of message copies will be removed. Ignored if send_copy is false
        :type remove_caption: bool

        :param only_preview: If true, messages will not be forwarded and instead fake messages will be returned
        :type only_preview: bool

        :param disable_notification: Pass true to disable notification for the message
        :type disable_notification: bool

        :param from_background: Pass true if the message is sent from the background
        :type from_background: bool

        :param send_date: Date the message will be sent. The date must be within 367 days in the future
        :type send_date: int

        :param send_when_online: When True, the message will be sent when the peer will be online. Applicable to private chats only and when the exact online status of the peer is known
        :type send_when_online: bool

        :param request_timeout: amounts of seconds to wait of response, (asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout seconds, defaults to None
        :type request_timeout: int

        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving; for bots only
        :type protect_content: :class:`bool`

        :return: response from TDLib
        :rtype: aiotdlib.api.types.Messages
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
                from_background=from_background,
                protect_content=protect_content,
                scheduling_state=scheduling_state
            ),
            send_copy=send_copy,
            remove_caption=remove_caption,
            only_preview=only_preview,
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

        :param chat_id: Chat identifier
        :type chat_id: int

        :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        :type from_message_id: int

        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
        :type limit: int

        :param only_local: If true, returns only messages that are available locally without sending network requests
        :type only_local: bool

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

    async def get_my_id(self) -> int:
        return await self.get_option_value('my_id')

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

    # Decorators
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
