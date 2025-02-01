from __future__ import annotations

import enum
import hashlib
import sys
from pathlib import Path
from typing import Optional, Union

import pydantic
import pydantic_settings
from pydantic import field_validator, model_validator

from . import __version__
from .tdjson import TDLibLogVerbosity
from .utils import str_to_base64, strip_phone_number_symbols


class ClientProxyType(str, enum.Enum):
    MTPROTO = "mtproto"
    HTTP = "http"
    SOCKS5 = "socks5"


class ClientParseMode(str, enum.Enum):
    HTML = "html"
    MARKDOWN = "markdown"


class ClientProxySettings(pydantic.BaseModel):
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

    @field_validator("secret")
    @classmethod
    def validate_secret(cls, secret: str, info: pydantic.ValidationInfo):
        values = info.data

        if values.get("type") == ClientProxyType.MTPROTO and secret is None:
            raise ValueError("Proxy secret is required for MTPROTO proxy")

        return secret


class ClientOptions(pydantic.BaseModel):
    always_parse_markdown: Optional[bool] = False
    """
    If true, text entities will be automatically parsed in all inputMessageText objects
    """

    archive_and_mute_new_chats_from_unknown_users: Optional[bool] = None
    """
    If true, new chats from non-contacts will be automatically archived and muted.
    The option can be set only if the option “can_archive_and_mute_new_chats_from_unknown_users” is true.
    getOption needs to be called explicitly to fetch the latest value of the option, changed from another device
    """

    disable_contact_registered_notifications: Optional[bool] = True
    """
    If true, notifications about the user's contacts who have joined Telegram will be disabled.
    User will still receive the corresponding message in the private chat.
    getOption needs to be called explicitly to fetch the latest value of the option, changed from another device
    """

    disable_persistent_network_statistics: Optional[bool] = True
    """
    If true, persistent network statistics will be disabled, which significantly reduces disk usage
    """

    disable_sent_scheduled_message_notifications: Optional[bool] = None
    """
    If true, notifications about outgoing scheduled messages that were sent will be disabled
    """

    disable_time_adjustment_protection: Optional[bool] = True
    """
    If true, protection from external time adjustment will be disabled, which significantly reduces disk usage
    """

    disable_top_chats: Optional[bool] = True
    """
    If true, support for top chats and statistics collection is disabled
    """

    ignore_background_updates: Optional[bool] = True
    """
    If true, allows to skip all updates received while the TDLib instance was not running.
    The option does nothing if the database or secret chats are used
    """

    ignore_default_disable_notification: Optional[bool] = None
    """
    If true, the disable_notification value specified in the request will be always used instead of the default value
    """

    ignore_inline_thumbnails: Optional[bool] = True
    """
    If true, prevents file thumbnails sent by the server along with messages from being saved on the disk
    """

    ignore_platform_restrictions: Optional[bool] = None
    """
    If true, chat and message restrictions specific to the currently used operating system will be ignored
    """

    is_location_visible: Optional[bool] = None
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

    language_pack_id: Optional[str] = None
    """
    Identifier of the currently used language pack from the current localization target
    """

    localization_target: Optional[str] = None
    """
    Name for the current localization target (currently supported: “android”,“android_x”,“ios”,“macos” and “tdesktop”)
    """

    message_unload_delay: Optional[int] = None
    """
    The maximum time messages are stored in memory before they are unloaded, 60-86400; in seconds.
    Defaults to 60 for users and 1800 for bots
    """

    notification_group_count_max: Optional[int] = None
    """
    Maximum number of notification groups to be shown simultaneously, 0-25
    """

    notification_group_size_max: Optional[int] = None
    """
    Maximum number of simultaneously shown notifications in a group, 1-25. Defaults to 10
    """

    online: Optional[bool] = None
    """
    Online status of the current user
    """

    prefer_ipv6: Optional[bool] = None
    """
    If true, IPv6 addresses will be preferred over IPv4 addresses
    """

    use_pfs: Optional[bool] = None
    """
    If true, Perfect Forward Secrecy will be enabled for interaction with the Telegram servers for cloud chats
    """

    use_quick_ack: Optional[bool] = None
    """
    If true, quick acknowledgement will be enabled for outgoing messages
    """

    use_storage_optimizer: Optional[bool] = True
    """
    If true, the background storage optimizer will be enabled
    """

    disable_network_statistics: Optional[bool] = True

    reuse_uploaded_photos_by_hash: Optional[bool] = True


class ClientSettings(pydantic_settings.BaseSettings):
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

    :param email: email address of new account if account with passed phone_number does not exist
    :type email: str

    :param library_path: Path to TDLib binary. By default binary included in package is used
    :type library_path: str

    :param tdlib_verbosity: Verbosity level of TDLib itself.
    Default: 2 (WARNING) for more info look at (TDLibLogVerbosity)
    :type tdlib_verbosity: str

    :param parse_mode: Default parse mode for high-level methods like send_message. Default: html
    :type parse_mode: str

    :param proxy_settings: Settings for proxying telegram connection
    :type proxy_settings: aiotdlib.ClientProxySettings

    """

    api_id: int
    api_hash: pydantic.SecretStr
    database_encryption_key: Union[str, bytes] = "aiotdlib"
    phone_number: Optional[str] = None
    bot_token: Optional[pydantic.SecretStr] = None
    use_test_dc: bool = False
    system_language_code: str = "en"
    device_model: str = "aiotdlib"
    system_version: str = ""
    application_version: str = __version__
    files_directory: Path = Path(sys.argv[0]).parent
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[pydantic.SecretStr] = None
    library_path: Optional[str] = None
    tdlib_verbosity: TDLibLogVerbosity = TDLibLogVerbosity.FATAL
    parse_mode: ClientParseMode = ClientParseMode.HTML
    proxy_settings: Optional[ClientProxySettings] = None
    use_file_database: bool = True
    use_chat_info_database: bool = True
    use_message_database: bool = True
    use_secret_chats: bool = False
    options: Optional[ClientOptions] = ClientOptions()

    @model_validator(mode="before")
    @classmethod
    def check_phone_and_bot_token(cls, values):
        if not bool(values.get("phone_number")) and not bool(values.get("bot_token")):
            raise ValueError("Either phone_number or bot_token should be specified")

        return values

    @field_validator("parse_mode", mode="before")
    @classmethod
    def validator_parse_mode(cls, value):
        if isinstance(value, str):
            return value.lower()

        return value

    @field_validator("phone_number")
    @classmethod
    def validator_phone_number(cls, value):
        if bool(value):
            return strip_phone_number_symbols(value)

        return value

    @field_validator("database_encryption_key", mode="before")
    @classmethod
    def validator_database_encryption_key(cls, value):
        if not bool(value):
            return value

        return str_to_base64(value)

    @field_validator("files_directory", mode="after")
    @classmethod
    def validator_files_directory(cls, value, info: pydantic.ValidationInfo):
        values = info.data

        if not bool(value):
            value = Path.cwd().parent

        md5_hash = hashlib.md5()
        phone_number = values.get("phone_number")
        bot_token = values.get("bot_token")

        if bool(phone_number):
            session_name = str(phone_number)
        elif bool(bot_token):
            session_name = str(bot_token)
        else:
            raise ValueError

        md5_hash.update(session_name.encode("utf-8"))
        directory_name = md5_hash.hexdigest()

        return value / ".aiotdlib" / directory_name

    model_config = pydantic_settings.SettingsConfigDict(
        env_file=".env",
        env_prefix="aiotdlib_",
        use_enum_values=True,
        populate_by_name=True,
        extra="ignore",
    )
