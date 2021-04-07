# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TdlibParameters(BaseObject):
    """
    Contains parameters for TDLib initialization
    
    Params:
        use_test_dc (:class:`bool`)
            If set to true, the Telegram test environment will be used instead of the production environment
        
        database_directory (:class:`str`)
            The path to the directory for the persistent database; if empty, the current working directory will be used
        
        files_directory (:class:`str`)
            The path to the directory for storing files; if empty, database_directory will be used
        
        use_file_database (:class:`bool`)
            If set to true, information about downloaded and uploaded files will be saved between application restarts
        
        use_chat_info_database (:class:`bool`)
            If set to true, the library will maintain a cache of users, basic groups, supergroups, channels and secret chats. Implies use_file_database
        
        use_message_database (:class:`bool`)
            If set to true, the library will maintain a cache of chats and messages. Implies use_chat_info_database
        
        use_secret_chats (:class:`bool`)
            If set to true, support for secret chats will be enabled
        
        api_id (:class:`int`)
            Application identifier for Telegram API access, which can be obtained at https://my.telegram.org
        
        api_hash (:class:`str`)
            Application identifier hash for Telegram API access, which can be obtained at https://my.telegram.org
        
        system_language_code (:class:`str`)
            IETF language tag of the user's operating system language; must be non-empty
        
        device_model (:class:`str`)
            Model of the device the application is being run on; must be non-empty
        
        system_version (:class:`str`)
            Version of the operating system the application is being run on. If empty, the version is automatically detected by TDLib
        
        application_version (:class:`str`)
            Application version; must be non-empty
        
        enable_storage_optimizer (:class:`bool`)
            If set to true, old files will automatically be deleted
        
        ignore_file_names (:class:`bool`)
            If set to true, original file names will be ignored. Otherwise, downloaded files will be saved under names as close as possible to the original name
        
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
