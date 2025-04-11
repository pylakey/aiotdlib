from __future__ import annotations

import asyncio
import logging
import typing
import uuid
from functools import partial, update_wrapper
from typing import AsyncIterator, Optional, Union

import pydantic.errors

from .api import (
    API,
    AddProxy,
    AioTDLibError,
    AuthorizationState,
    BaseObject,
    BasicGroup,
    BasicGroupFullInfo,
    Chat,
    ChatTypeBasicGroup,
    ChatTypePrivate,
    ChatTypeSecret,
    ChatTypeSupergroup,
    CheckAuthenticationBotToken,
    CheckAuthenticationCode,
    CheckAuthenticationEmailCode,
    CheckAuthenticationPassword,
    DisableProxy,
    EmailAddressAuthenticationCode,
    Error,
    FormattedText,
    GetAuthorizationState,
    GetCurrentState,
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageContent,
    InputMessageDocument,
    InputMessagePhoto,
    InputMessageReplyToMessage,
    InputMessageSticker,
    InputMessageText,
    InputMessageVideo,
    InputMessageVideoNote,
    InputMessageVoiceNote,
    InputThumbnail,
    LinkPreviewOptions,
    Message,
    Messages,
    MessageSchedulingStateSendAtDate,
    MessageSchedulingStateSendWhenOnline,
    MessageSelfDestructType,
    MessageSendingStatePending,
    MessageSendOptions,
    OptionValueBoolean,
    OptionValueEmpty,
    OptionValueInteger,
    OptionValueString,
    ParseTextEntities,
    PhoneNumberAuthenticationSettings,
    ProxyTypeHttp,
    ProxyTypeMtproto,
    ProxyTypeSocks5,
    RegisterUser,
    ReplyMarkup,
    SecretChat,
    SetAuthenticationEmailAddress,
    SetAuthenticationPhoneNumber,
    SetLogVerbosityLevel,
    SetOption,
    SetTdlibParameters,
    Supergroup,
    SupergroupFullInfo,
    TDLibObject,
    TextParseModeHTML,
    TextParseModeMarkdown,
    UpdateAuthorizationState,
    UpdateMessageSendFailed,
    UpdateMessageSendSucceeded,
    User,
    UserFullInfo,
)
from .client_cache import ClientCache
from .client_settings import ClientParseMode, ClientProxyType, ClientSettings
from .constants import TDLIB_MAX_INT
from .filters import Filters
from .handlers import FilterCallable, Handler, HandlerCallable
from .middlewares import MiddlewareCallable
from .tdjson import TDJsonClient
from .utils import PendingRequest, ainput, make_input_file, make_thumbnail, parse_tdlib_object

RequestResult = typing.TypeVar("RequestResult", bound=BaseObject, covariant=True)
ExecuteResult = typing.TypeVar("ExecuteResult", bound=BaseObject, covariant=True)
AuthActions = dict[Optional[str], typing.Callable[[], typing.Coroutine[None, None, None]]]
ChatInfo = Union[User, UserFullInfo, BasicGroup, BasicGroupFullInfo, Supergroup, SupergroupFullInfo, SecretChat]


class Client:
    def __init__(self, settings: Optional[ClientSettings] = None):
        """
        Create new instance of TDLib client

        Args:
            settings (ClientSettings): Settings for client,
             if not provided default settings will be used, including environment variables
        """
        self._authorized_event = asyncio.Event()
        self._running = False
        self._pending_requests: dict[str, PendingRequest] = {}
        self._pending_messages: dict[str, Message] = {}
        self._updates_handlers: dict[str, set[Handler]] = {}
        self._middlewares: list[MiddlewareCallable] = []
        self._middlewares_handlers: list[MiddlewareCallable] = []
        self._update_task: typing.Optional[asyncio.Task[None]] = None
        self._handlers_tasks: set[asyncio.Task] = set()
        self.settings = settings or ClientSettings()
        self.tdjson_client = TDJsonClient.create(self.settings.library_path)
        self.logger = logging.getLogger(f"{self.__class__.__name__}_{self.tdjson_client.client_id}")
        self.api = API(self)
        self.cache = ClientCache(self)

    @property
    def is_bot(self) -> bool:
        return bool(self.settings.bot_token)

    def add_event_handler(
        self,
        handler: HandlerCallable,
        update_type: str = API.Types.ANY,
        *,
        filters: FilterCallable = None,
    ) -> Handler:
        """
        Registering event handler
        You can register many handlers for certain event type
        """
        if self._updates_handlers.get(update_type) is None:
            self._updates_handlers[update_type] = set()

        handler = Handler(handler, filters=filters)
        self._updates_handlers[update_type].add(handler)
        return handler

    def on_event(self, update_type: str = API.Types.ANY, *, filters: FilterCallable = None):
        def decorator(function: HandlerCallable) -> HandlerCallable:
            self.add_event_handler(function, update_type, filters=filters)
            return function

        return decorator

    def remove_event_handler(self, handler: Handler, update_type: str = API.Types.ANY):
        if self._updates_handlers.get(update_type) is None:
            return

        self._updates_handlers.get(update_type).discard(handler)

    def add_middleware(self, middleware: MiddlewareCallable):
        """
        Register middleware.
        Note that middleware would be called for EVERY EVENT.
        Do not use them for long-running tasks as it could be heavy performance hit
        You can add as much middlewares as you want.
        They would be called in order you've added them
        """

        self._middlewares.append(middleware)
        return middleware

    def text_message_handler(self, function: HandlerCallable = None):
        """
        Registers event handler with predefined filter `Filters.text`
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

    # Magic methods
    async def __aenter__(self) -> "Client":
        return await self.start()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

        if bool(exc_val):
            raise exc_val

    async def _call_handler(self, handler: Handler, update: TDLibObject):
        try:
            await handler(self, update)
        except Exception as e:
            self.logger.error(e, exc_info=True)

    async def _call_handlers(self, update: TDLibObject):
        tasks = []
        tasks.extend(self._call_handler(h, update) for h in self._updates_handlers.get(update.ID, []))
        tasks.extend(self._call_handler(h, update) for h in self._updates_handlers.get("*", []))
        # Running all handlers concurrently and independently
        await asyncio.gather(*tasks, return_exceptions=True)

    def _create_handler_task(self, coro):
        task: asyncio.Task = asyncio.create_task(coro)
        self._handlers_tasks.add(task)
        task.add_done_callback(self._handlers_tasks.discard)

    async def _handle_update(self, update: TDLibObject):
        if len(self._middlewares_handlers) == 0:
            return await self._call_handlers(update)

        async def _fn(*_, **__):
            return await self._call_handlers(update)

        call_next = _fn

        for m in self._middlewares_handlers:
            call_next = update_wrapper(partial(m, call_next=call_next), call_next)

        try:
            return await call_next(self, update)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            self.logger.error(f"Unable to handle update {update}! {e}", exc_info=True)

    async def _handle_pending_request(self, update: TDLibObject):
        request_id = update.EXTRA.get("request_id")

        if isinstance(update, Message) and isinstance(update.sending_state, MessageSendingStatePending):
            # MessageSendingStateFailed will be set as an error to pending request, no need to handle it here
            sending_id = f"{update.chat_id}_{update.id}"
            self.logger.debug(f"Put message to pending messages: {sending_id}")
            self._pending_messages[sending_id] = update
            return

        if isinstance(update, (UpdateMessageSendSucceeded, UpdateMessageSendFailed)):
            sending_id = f"{update.message.chat_id}_{update.old_message_id}"
            pending_message = self._pending_messages.pop(sending_id, None)

            if bool(pending_message):
                request_id = pending_message.EXTRA.get("request_id")

                if isinstance(update, UpdateMessageSendFailed):
                    self.logger.debug(f"Message {sending_id} sending failed")
                    update = update.error
                else:
                    self.logger.debug(f"Message {sending_id} sending succeeded")
                    update = update.message

        pending_request = self._pending_requests.pop(request_id, None)

        if bool(pending_request):
            pending_request.set_update(update)
            self.logger.debug(
                f"Pending request {request_id} is successfully processed.Total pending: {len(self._pending_requests)}"
            )

    async def _updates_loop(self):
        async for packet in self.tdjson_client.receive():
            if not bool(packet):
                continue

            try:
                update = parse_tdlib_object(packet)
            except pydantic.ValidationError as e:
                self.logger.error(f"Unable to parse incoming update: {packet}! {e}", exc_info=True)
                continue

            if isinstance(update, UpdateAuthorizationState):
                try:
                    await self._on_authorization_state_update(update.authorization_state)
                except asyncio.CancelledError:
                    self.logger.info("Authorization process has been cancelled")
                    raise
                except Exception as e:
                    self.logger.error(
                        f"Unable to handle authorization state update {update.model_dump_json()}! {e}",
                        exc_info=True,
                    )
                    raise
                else:
                    continue

            try:
                await self._handle_pending_request(update)
            except asyncio.CancelledError:
                raise
            except Exception as e:
                self.logger.error(f"Unable to handle pending request {update}! {e}", exc_info=True)

            self._create_handler_task(self._handle_update(update))

    async def _setup_proxy(self):
        if not bool(self.settings.proxy_settings):
            # If proxy is not set disabling all configured proxy
            self.logger.info("Proxy is not set. Disabling all proxy settings.")
            await self.send(DisableProxy())
            return

        self.logger.info(
            f"Configuring PROXY of type {self.settings.proxy_settings.type.value}. "
            f"Server: {self.settings.proxy_settings.host}:{self.settings.proxy_settings.port}"
        )

        if self.settings.proxy_settings.type == ClientProxyType.SOCKS5:
            proxy_type = ProxyTypeSocks5(
                username=self.settings.proxy_settings.username,
                password=self.settings.proxy_settings.password,
            )
        elif self.settings.proxy_settings.type == ClientProxyType.HTTP:
            proxy_type = ProxyTypeHttp(
                username=self.settings.proxy_settings.username,
                password=self.settings.proxy_settings.password,
                http_only=self.settings.proxy_settings.http_only,
            )
        elif self.settings.proxy_settings.type == ClientProxyType.MTPROTO:
            proxy_type = ProxyTypeMtproto(
                secret=self.settings.proxy_settings.secret,
            )
        else:
            raise ValueError(f"Unknown proxy type {self.settings.proxy_settings.type}")

        await self.send(
            AddProxy(
                enable=True,
                server=self.settings.proxy_settings.host,
                port=self.settings.proxy_settings.port,
                type=proxy_type,
            )
        )

    async def _setup_options(self):
        if not bool(self.settings.options):
            return

        for k, v in self.settings.options.model_dump(by_alias=True).items():
            if v is None:
                option_value = OptionValueEmpty()
            elif isinstance(v, bool):
                option_value = OptionValueBoolean(value=v)
            elif isinstance(v, str):
                option_value = OptionValueString(value=v)
            elif isinstance(v, int):
                option_value = OptionValueInteger(value=v)
            else:
                self.logger.warning(f"Option {k} has unsupported value of type {v.__class__.__name__}: {v}")
                continue

            self.logger.info(f"Setting up option {k} = {v if v is not None else '<empty or default>'}")
            try:
                query = SetOption(name=k, value=option_value)
            except pydantic.ValidationError:
                self.logger.warning(f"Option {k} has unsupported value of type {v.__class__.__name__}: {v}")
                continue

            await self.send(query)

    async def _auth_start(self):
        await self.send(GetAuthorizationState())
        # return await self.api.get_authorization_state(request_id=AUTHORIZATION_REQUEST_ID)

    async def _set_tdlib_parameters(self):
        await self.send(
            SetTdlibParameters(
                database_encryption_key=self.settings.database_encryption_key,
                api_id=self.settings.api_id,
                api_hash=self.settings.api_hash.get_secret_value(),
                system_language_code=self.settings.system_language_code,
                device_model=self.settings.device_model,
                application_version=self.settings.application_version,
                use_test_dc=self.settings.use_test_dc,
                database_directory=str(self.settings.files_directory / "database"),
                files_directory=str(self.settings.files_directory / "files"),
                use_file_database=self.settings.use_file_database,
                use_chat_info_database=self.settings.use_chat_info_database,
                use_message_database=self.settings.use_message_database,
                use_secret_chats=self.settings.use_secret_chats,
                system_version=self.settings.system_version,
            )
        )

    async def _set_authentication_phone_number_or_check_bot_token(self):
        await self.send(SetOption(name="online", value=OptionValueBoolean(value=True)))

        if self.is_bot:
            return await self._check_authentication_bot_token()

        return await self._set_authentication_phone_number()

    async def _set_authentication_phone_number(self):
        self.logger.info("Sending phone number")
        await self.send(
            SetAuthenticationPhoneNumber(
                phone_number=self.settings.phone_number,
                settings=PhoneNumberAuthenticationSettings(
                    allow_flash_call=False,
                    allow_missed_call=False,
                    is_current_phone_number=True,
                    allow_sms_retriever_api=False,
                    authentication_tokens=[],
                ),
            )
        )

    async def _check_authentication_bot_token(self):
        self.logger.info("Sending bot token")
        await self.send(
            CheckAuthenticationBotToken(
                token=self.settings.bot_token.get_secret_value(),
            )
        )

    async def _check_authentication_code(self):
        code = await self._auth_get_code(code_type="SMS")
        self.logger.info(f"Sending code {code}")
        await self.send(
            CheckAuthenticationCode(
                code=code,
            )
        )

    async def _set_authentication_email_address(self):
        email_address = await self._auth_get_email()
        await self.send(
            SetAuthenticationEmailAddress(
                email_address=email_address,
            )
        )

    async def _check_authentication_email_code(self):
        code = await self._auth_get_code(code_type="EMail")
        self.logger.info(f"Sending email code {code}")
        return await self.send(
            CheckAuthenticationEmailCode(
                code=EmailAddressAuthenticationCode(code=code),
            )
        )

    async def _register_user(self):
        first_name = await self._auth_get_first_name()
        last_name = await self._auth_get_last_name()
        self.logger.info(f"Registering new user in telegram as {first_name} {last_name or ''}".strip())
        await self.send(
            RegisterUser(
                first_name=first_name,
                last_name=last_name,
            )
        )

    async def _check_authentication_password(self):
        password = await self._auth_get_password()
        self.logger.info("Sending password")
        await self.send(
            CheckAuthenticationPassword(
                password=password,
            )
        )

    # noinspection PyMethodMayBeStatic
    async def _auth_get_code(self, *, code_type: str = "SMS") -> str:
        code = ""

        while len(code) != 5 or not code.isdigit():
            code = await ainput(f"Enter {code_type} code:")

        return code

    async def _auth_get_password(self) -> str:
        password = self.settings.password

        if not bool(password):
            password = await ainput("Enter 2FA password:", secured=True)
        else:
            password = password.get_secret_value()

        return password

    async def _auth_get_first_name(self) -> str:
        first_name = self.settings.first_name or ""

        while not bool(first_name) or len(first_name) > 64:
            first_name = await ainput("Enter first name:")

        return first_name

    async def _auth_get_last_name(self) -> str:
        last_name = self.settings.last_name or ""

        if not bool(last_name):
            last_name = await ainput("Enter last name:")

        return last_name

    async def _auth_get_email(self) -> str:
        email = self.settings.email or ""

        if not bool(email):
            email = await ainput("Enter your email:")

        return email

    async def _auth_completed(self):
        self._authorized_event.set()

        # if not self.is_bot:
        #     # Preload main list chats
        #     await self.get_main_list_chats()

    async def _auth_logging_out(self):
        self.logger.info("Auth session is logging out")

    async def _auth_closing(self):
        self.logger.info("Auth session is closing")

    async def _auth_closed(self):
        self.logger.info("Auth session is closed")

    async def _on_authorization_state_update(self, authorization_state: AuthorizationState):
        auth_actions: AuthActions = {
            None: self._auth_start,
            API.Types.AUTHORIZATION_STATE_WAIT_TDLIB_PARAMETERS: self._set_tdlib_parameters,
            API.Types.AUTHORIZATION_STATE_WAIT_PHONE_NUMBER: self._set_authentication_phone_number_or_check_bot_token,
            API.Types.AUTHORIZATION_STATE_WAIT_CODE: self._check_authentication_code,
            API.Types.AUTHORIZATION_STATE_WAIT_EMAIL_ADDRESS: self._set_authentication_email_address,
            API.Types.AUTHORIZATION_STATE_WAIT_EMAIL_CODE: self._check_authentication_email_code,
            API.Types.AUTHORIZATION_STATE_WAIT_REGISTRATION: self._register_user,
            API.Types.AUTHORIZATION_STATE_WAIT_PASSWORD: self._check_authentication_password,
            API.Types.AUTHORIZATION_STATE_READY: self._auth_completed,
            API.Types.AUTHORIZATION_STATE_LOGGING_OUT: self._auth_logging_out,
            API.Types.AUTHORIZATION_STATE_CLOSING: self._auth_closing,
            API.Types.AUTHORIZATION_STATE_CLOSED: self._auth_closed,
            # TODO: QR Login support
            # API.Types.AUTHORIZATION_STATE_WAIT_OTHER_DEVICE_CONFIRMATION: None,
        }

        action = auth_actions.get(authorization_state.ID)

        if bool(action):
            await action()

    async def _cleanup(self):
        self._pending_requests.clear()
        self._pending_messages.clear()

        if bool(self._update_task) and not self._update_task.cancelled():
            self.logger.info("Cancelling updates loop task")
            self._update_task.cancel()
            await self._update_task

        # Cancel all background handlers tasks
        if bool(self._handlers_tasks):
            self.logger.info(f"Cancelling {len(self._handlers_tasks)} background handlers tasks")

            for task in self._handlers_tasks:
                # noinspection PyBroadException
                try:
                    task.cancel()
                except Exception:
                    pass

            # Wait for all tasks to be cancelled
            await asyncio.wait(self._handlers_tasks, return_when=asyncio.ALL_COMPLETED)

        if bool(self.cache):
            self.cache.clear()

        if bool(self.tdjson_client):
            # TODO: gracefully close current tdjson client
            self.logger.info("Gracefully closing TDLib connection")
            await self.tdjson_client.close()

        self._running = False

    async def _run(self):
        async with self:
            await self.idle()

    def run(self):
        asyncio.run(self._run())

    # Core methods
    async def send(self, query: TDLibObject):
        if not self._running:
            raise RuntimeError("Client not started")

        query_json = query.model_dump_json(by_alias=True)  # Exclude unset??
        self.logger.debug(f">>>>> {query.ID} %s", query_json)
        await self.tdjson_client.send(query_json)

    async def request(
        self,
        query: TDLibObject,
        *,
        request_id: str = None,
        request_timeout: int = None,
    ) -> Optional[RequestResult]:
        if request_id is None:
            request_id = query.EXTRA.get("request_id") or uuid.uuid4().hex

        if request_timeout is None:
            request_timeout = 10

        query.EXTRA["request_id"] = request_id
        pending_request = PendingRequest(self, query)
        self._pending_requests[request_id] = pending_request
        self.logger.debug(
            f"Pending request {query.ID} with request_id {request_id} created."
            f"Total pending: {len(self._pending_requests)}"
        )

        try:
            await self.send(query)
            await pending_request.wait(raise_exc=True, timeout=request_timeout)
        except (asyncio.TimeoutError, TimeoutError):
            self.logger.debug(
                f"Request {query.ID} with request_id {request_id} has been timed out. "
                f"Total pending: {len(self._pending_requests)}"
            )
            self._pending_requests.pop(request_id, None)
            raise
        finally:
            if bool(pending_request.update):
                self.logger.debug(
                    f"<<<<< {pending_request.update.ID} %s",
                    pending_request.update.model_dump_json(by_alias=True),
                )

        return pending_request.update

    async def execute(self, query: TDLibObject) -> ExecuteResult:
        if not self._running:
            raise RuntimeError("Client not started")

        result = await self.tdjson_client.execute(query.model_dump(by_alias=True))
        result_object = parse_tdlib_object(result)

        if isinstance(result_object, Error):
            raise AioTDLibError(code=result_object.code, message=result_object.message)

        return result_object

    async def authorize(self):
        if self.is_bot:
            self.logger.info("Authorization process has been started with bot token")
        else:
            self.logger.info("Authorization process has been started with phone")

        await self.send(GetAuthorizationState())

        self.logger.info("Waiting for authorization to be completed")
        await self._authorized_event.wait()

    async def start(self) -> "Client":
        self.logger.info("Starting client")
        self.logger.info(f"Session workdir: {self.settings.files_directory.absolute()}")

        # Preparing middlewares handlers
        self._middlewares_handlers = list(reversed(self._middlewares))

        # Starting updates loop
        self._update_task = asyncio.create_task(self._updates_loop())
        self._running = True

        try:
            self.logger.info("Setting log verbosity level")
            await self.execute(SetLogVerbosityLevel(new_verbosity_level=self.settings.tdlib_verbosity))
            self.logger.info("Setting up proxy")
            await self._setup_proxy()
            self.logger.info("Setting up options")
            await self._setup_options()
            self.logger.info("Initialize authorization process")
            await self.authorize()
        except asyncio.CancelledError:
            await self._cleanup()
            raise
        else:
            self.logger.info("Authorization is completed")

        return self

    async def idle(self):
        while True:
            try:
                await asyncio.sleep(0.1)
            except asyncio.CancelledError:
                self.logger.info("Stop Idling")
                raise

    async def stop(self):
        self.logger.info("Stopping telegram client")
        await self._cleanup()

    # Cache related methods
    async def get_my_id(self) -> int:
        return await self.get_option_value("my_id")

    async def load_current_state(self):
        # All current state will be received via updates
        await self.send(GetCurrentState())

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
        return await self.cache.get_main_chat_list(limit)

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
        self, chat: Union[int, Chat], *, full: bool = False, force_update: bool = False
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

        raise ValueError(f"Unknown chat.type {chat.type_.__class__.__qualname__}")

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
                    TextParseModeHTML() if parse_mode == ClientParseMode.HTML else TextParseModeMarkdown(version=2)
                ),
            )
        )

    async def _send_message(
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
        update_order_of_installed_sticker_sets: bool = False,
        sending_id: int = 0,
        effect_id: Optional[int] = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
    ):
        """
        Sends a message. Returns the sent message

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

        :param send_when_online: When True, the message will be sent when the peer will be online.
          Applicable to private chats only and when the exact online status of the peer is known
        :type send_when_online: :class:`bool`

        :param send_date: Date the message will be sent. The date must be within 367 days in the future.
          If send_date passed send_when_online will be ignored
        :type send_date: :class:`int`

        :param request_timeout: amounts of seconds to wait of response, (:class:`asyncio.TimeoutError`)
          will be raised if request lasts more than `request_timeout` seconds, defaults to None
        :type request_timeout: :class:`int`

        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving;
          for bots only
        :type protect_content: :class:`bool`

        :param update_order_of_installed_sticker_sets: Pass true if the user explicitly chosen a sticker
          or a custom emoji from an installed sticker set; applicable only to sendMessage and sendMessageAlbum
        :type update_order_of_installed_sticker_sets: :class:`bool`

        :param sending_id: Non-persistent identifier, which will be returned back in messageSendingStatePending object
          and can be used to match sent messages and corresponding updateNewMessage updates
        :type sending_id: :class:`int`

        :param effect_id: Identifier of the effect to apply to the message; applicable only to sendMessage
          and sendMessageAlbum in private chats, defaults to None
        :type effect_id: :class:`int`

        :param only_preview: Pass true to get a fake message instead of actually sending them
        :type only_preview: bool

        :param paid_message_star_count: The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0
        :type paid_message_star_count: :class:`int`

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
            reply_to=InputMessageReplyToMessage(message_id=reply_to_message_id) if bool(reply_to_message_id) else None,
            options=MessageSendOptions(
                disable_notification=disable_notification,
                from_background=False,
                protect_content=protect_content,
                scheduling_state=scheduling_state,
                update_order_of_installed_sticker_sets=update_order_of_installed_sticker_sets,
                sending_id=sending_id,
                effect_id=effect_id,
                only_preview=only_preview,
                paid_message_star_count=paid_message_star_count,
            ),
            reply_markup=reply_markup,
            input_message_content=content,
            request_timeout=request_timeout,
        )

    async def send_text(
        self,
        chat_id: int,
        text: str,
        *,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        clear_draft: bool = True,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            link_preview_options (LinkPreviewOptions)
                Options to be used for generation of a link preview

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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object
                and can be used to match sent messages and corresponding updateNewMessage updates

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageText(
                text=(await self.parse_text(text)),
                clear_draft=clear_draft,
                link_preview_options=link_preview_options,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def edit_text(
        self,
        chat_id: int,
        message_id: int,
        text: str,
        *,
        reply_markup: ReplyMarkup = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        clear_draft: bool = True,
        request_timeout: int = None,
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

            link_preview_options (LinkPreviewOptions)
                Options to be used for generation of a link preview

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
            input_message_content=InputMessageText(
                text=formatted_text,
                clear_draft=clear_draft,
                link_preview_options=link_preview_options,
            ),
            request_timeout=request_timeout,
        )

    async def send_photo(
        self,
        chat_id: int,
        photo: str,
        *,
        caption: str = None,
        added_sticker_file_ids: list[int] = None,
        photo_width: int = 0,
        photo_height: int = 0,
        self_destruct_type: Optional[MessageSelfDestructType] = None,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            self_destruct_type (MessageSelfDestructType)
                Photo self-destruct type; pass null if none; private chats only, defaults to None

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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object
                and can be used to match sent messages and corresponding updateNewMessage updates

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0
        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessagePhoto(
                caption=(await self.parse_text(caption)),
                photo=make_input_file(photo),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                added_sticker_file_ids=added_sticker_file_ids or [],
                width=photo_width,
                height=photo_height,
                self_destruct_type=self_destruct_type,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_video(
        self,
        chat_id: int,
        video: str,
        *,
        caption: str = None,
        added_sticker_file_ids: list[int] = None,
        duration: int = 0,
        video_width: int = 0,
        video_height: int = 0,
        self_destruct_type: Optional[MessageSelfDestructType] = None,
        supports_streaming: bool = False,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            self_destruct_type (MessageSelfDestructType)
                Photo self-destruct type; pass null if none; private chats only, defaults to None

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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object
                and can be used to match sent messages and corresponding updateNewMessage updates

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageVideo(
                caption=(await self.parse_text(caption)),
                video=make_input_file(video),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                added_sticker_file_ids=added_sticker_file_ids or [],
                duration=duration,
                width=video_width,
                height=video_height,
                self_destruct_type=self_destruct_type,
                supports_streaming=supports_streaming,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_animation(
        self,
        chat_id: int,
        animation: str,
        *,
        caption: str = None,
        added_sticker_file_ids: list[int] = None,
        duration: int = 0,
        animation_width: int = 0,
        animation_height: int = 0,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object
                and can be used to match sent messages and corresponding updateNewMessage updates

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageAnimation(
                caption=(await self.parse_text(caption)),
                animation=make_input_file(animation),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                added_sticker_file_ids=added_sticker_file_ids or [],
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
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_sticker(
        self,
        chat_id: int,
        sticker: str,
        *,
        sticker_width: int = 0,
        sticker_height: int = 0,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        emoji: str = None,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object
                and can be used to match sent messages and corresponding updateNewMessage updates

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0
        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageSticker(
                sticker=make_input_file(sticker),
                thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                width=sticker_width,
                height=sticker_height,
                emoji=emoji,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_document(
        self,
        chat_id: int,
        document: str,
        *,
        caption: str = None,
        disable_content_type_detection: bool = False,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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
                If true, automatic file type detection will be disabled and the document will always be sent as file.
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageDocument(
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
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_audio(
        self,
        chat_id: int,
        audio: str,
        *,
        caption: str = None,
        duration: int = 0,
        title: str = None,
        performer: str = None,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageAudio(
                audio=make_input_file(audio),
                caption=(await self.parse_text(caption)),
                album_cover_thumbnail=make_thumbnail(thumbnail, width=thumbnail_width, height=thumbnail_height),
                title=title,
                duration=duration,
                performer=performer,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_voice_note(
        self,
        chat_id: int,
        voice_note: str,
        *,
        caption: str = None,
        duration: int = 0,
        waveform: str = None,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageVoiceNote(
                voice_note=make_input_file(voice_note),
                caption=(await self.parse_text(caption)),
                duration=duration,
                waveform=waveform,
            ),
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup,
            disable_notification=disable_notification,
            send_when_online=send_when_online,
            send_date=send_date,
            request_timeout=request_timeout,
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def send_video_note(
        self,
        chat_id: int,
        video_note: str,
        *,
        duration: int = 0,
        length: int = 0,
        thumbnail: Union[str, InputThumbnail] = None,
        thumbnail_width: int = 0,
        thumbnail_height: int = 0,
        reply_to_message_id: int = None,
        reply_markup: ReplyMarkup = None,
        disable_notification: bool = False,
        send_when_online: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
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

            sending_id: (int)
                Non-persistent identifier, which will be returned back in messageSendingStatePending object

            only_preview: (bool)
                Pass true to get a fake message instead of actually sending them

            paid_message_star_count: (int)
                The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0

        """
        return await self._send_message(
            chat_id=chat_id,
            content=InputMessageVideoNote(
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
            protect_content=protect_content,
            sending_id=sending_id,
            only_preview=only_preview,
            paid_message_star_count=paid_message_star_count,
        )

    async def iter_chat_history(
        self,
        chat_id: int,
        from_message_id: int = 0,
        limit: int = None,
        only_local: bool = False,
    ) -> AsyncIterator[Message]:
        """
        Iterates over messages in a chat.
        The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id).
        Number of messages are limited by limit parameter

        :param chat_id: Chat identifier
        :type chat_id: int

        :param from_message_id: Identifier of the message starting from which history must be fetched;
          use 0 to get results from the last message
        :type from_message_id: int

        :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100.
          If the offset is negative, the limit must be greater than or equal to -offset.
          For optimal performance, the number of returned messages is chosen by TDLib
          and can be smaller than the specified limit
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
                only_local=only_local,
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
        from_background: bool = False,
        send_date: int = None,
        request_timeout: int = None,
        protect_content: bool = False,
        sending_id: int = 0,
        only_preview: bool = False,
        paid_message_star_count: int = 0,
    ) -> Messages:
        """
        Forwards previously sent messages.
        Returns the forwarded messages in the same order as the message identifiers passed in message_ids.
        If a message can't be forwarded, null will be returned instead of the message

        :param chat_id: Identifier of the chat to which to forward messages
        :type chat_id: int

        :param from_chat_id: Identifier of the chat from which to forward messages
        :type from_chat_id: int

        :param message_ids: Identifiers of the messages to forward.
          Message identifiers must be in a strictly increasing order.
          At most 100 messages can be forwarded simultaneously
        :type message_ids: list[int]

        :param send_copy: If true, content of the messages will be copied without reference to the original sender.
          Always true if the messages are forwarded to a secret chat or are local
        :type send_copy: bool

        :param remove_caption: If true, media caption of message copies will be removed. Ignored if send_copy is false
        :type remove_caption: bool

        :param disable_notification: Pass true to disable notification for the message
        :type disable_notification: bool

        :param from_background: Pass true if the message is sent from the background
        :type from_background: bool

        :param send_date: Date the message will be sent. The date must be within 367 days in the future
        :type send_date: int

        :param send_when_online: When True, the message will be sent when the peer will be online.
          Applicable to private chats only and when the exact online status of the peer is known
        :type send_when_online: bool

        :param request_timeout: amounts of seconds to wait of response,
          (asyncio.TimeoutError`) will be be raised if request lasts more than `request_timeout seconds,
          defaults to None
        :type request_timeout: int

        :param protect_content: Pass true if the content of the message must be protected from forwarding and saving;
          for bots only
        :type protect_content: :class:`bool`

        :param sending_id: Non-persistent identifier, which will be returned back in messageSendingStatePending object
          and can be used to match sent messages and corresponding updateNewMessage updates
        :type sending_id: :class:`int`

        :param only_preview: Pass true to get a fake message instead of actually sending them
        :type only_preview: bool

        :param paid_message_star_count: The number of Telegram Stars the user agreed to pay to send the messages, defaults to 0
        :type paid_message_star_count: :class:`int`

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
            options=MessageSendOptions(
                disable_notification=disable_notification,
                from_background=from_background,
                protect_content=protect_content,
                scheduling_state=scheduling_state,
                update_order_of_installed_sticker_sets=False,
                only_preview=only_preview,
                sending_id=sending_id,
                paid_message_star_count=paid_message_star_count,
            ),
            send_copy=send_copy,
            remove_caption=remove_caption,
            request_timeout=request_timeout,
        )
