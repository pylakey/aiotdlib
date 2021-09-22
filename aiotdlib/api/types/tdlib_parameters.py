# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class TdlibParameters(BaseObject):
    """
    Contains parameters for TDLib initialization
    
    :param use_test_dc: If set to true, the Telegram test environment will be used instead of the production environment
    :type use_test_dc: :class:`bool`
    
    :param database_directory: The path to the directory for the persistent database; if empty, the current working directory will be used
    :type database_directory: :class:`str`
    
    :param files_directory: The path to the directory for storing files; if empty, database_directory will be used
    :type files_directory: :class:`str`
    
    :param use_file_database: If set to true, information about downloaded and uploaded files will be saved between application restarts
    :type use_file_database: :class:`bool`
    
    :param use_chat_info_database: If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies use_file_database
    :type use_chat_info_database: :class:`bool`
    
    :param use_message_database: If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database
    :type use_message_database: :class:`bool`
    
    :param use_secret_chats: If set to true, support for secret chats will be enabled
    :type use_secret_chats: :class:`bool`
    
    :param api_id: Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
    :type api_id: :class:`int`
    
    :param api_hash: Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
    :type api_hash: :class:`str`
    
    :param system_language_code: IETF language tag of the user's operating system language; must be non-empty
    :type system_language_code: :class:`str`
    
    :param device_model: Model of the device the application is being run on; must be non-empty
    :type device_model: :class:`str`
    
    :param system_version: Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
    :type system_version: :class:`str`
    
    :param application_version: Application version; must be non-empty
    :type application_version: :class:`str`
    
    :param enable_storage_optimizer: If set to true, old files will automatically be deleted
    :type enable_storage_optimizer: :class:`bool`
    
    :param ignore_file_names: If set to true, original file names will be ignored. Otherwise, downloaded files will be saved under names as close as possible to the original name
    :type ignore_file_names: :class:`bool`
    
    """

    ID: str = Field("tdlibParameters", alias="@type")
    use_test_dc: bool
    database_directory: str
    files_directory: str
    use_file_database: bool
    use_chat_info_database: bool
    use_message_database: bool
    use_secret_chats: bool
    api_id: int
    api_hash: str
    system_language_code: str
    device_model: str
    system_version: str
    application_version: str
    enable_storage_optimizer: bool
    ignore_file_names: bool

    @staticmethod
    def read(q: dict) -> TdlibParameters:
        return TdlibParameters.construct(**q)
