# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetTdlibParameters(BaseObject):
    """
    Sets the parameters for TDLib initialization. Works only when the current authorization state is authorizationStateWaitTdlibParameters

    :param database_directory: The path to the directory for the persistent database; if empty, the current working directory will be used
    :type database_directory: :class:`String`
    :param files_directory: The path to the directory for storing files; if empty, database_directory will be used
    :type files_directory: :class:`String`
    :param database_encryption_key: Encryption key for the database. If the encryption key is invalid, then an error with code 401 will be returned
    :type database_encryption_key: :class:`Bytes`
    :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
    :type api_id: :class:`Int32`
    :param api_hash: Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
    :type api_hash: :class:`String`
    :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
    :type system_language_code: :class:`String`
    :param device_model: Model of the device the application is being run on; must be non-empty
    :type device_model: :class:`String`
    :param system_version: Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
    :type system_version: :class:`String`
    :param application_version: Application version; must be non-empty
    :type application_version: :class:`String`
    :param use_test_dc: Pass true to use Telegram test environment instead of the production environment
    :type use_test_dc: :class:`Bool`
    :param use_file_database: Pass true to keep information about downloaded and uploaded files between application restarts
    :type use_file_database: :class:`Bool`
    :param use_chat_info_database: Pass true to keep cache of users, basic groups, supergroups, channels and secret chats between restarts. Implies use_file_database
    :type use_chat_info_database: :class:`Bool`
    :param use_message_database: Pass true to keep cache of chats and messages between restarts. Implies use_chat_info_database
    :type use_message_database: :class:`Bool`
    :param use_secret_chats: Pass true to enable support for secret chats
    :type use_secret_chats: :class:`Bool`
    :param enable_storage_optimizer: Pass true to automatically delete old files in background
    :type enable_storage_optimizer: :class:`Bool`
    :param ignore_file_names: Pass true to ignore original file names for downloaded files. Otherwise, downloaded files are saved under names as close as possible to the original name
    :type ignore_file_names: :class:`Bool`
    """

    ID: typing.Literal["setTdlibParameters"] = "setTdlibParameters"
    database_directory: String
    files_directory: String
    database_encryption_key: Bytes
    api_id: Int32
    api_hash: String
    system_language_code: String
    device_model: String
    system_version: String
    application_version: String
    use_test_dc: Bool = False
    use_file_database: Bool = False
    use_chat_info_database: Bool = False
    use_message_database: Bool = False
    use_secret_chats: Bool = False
    enable_storage_optimizer: Bool = False
    ignore_file_names: Bool = False
