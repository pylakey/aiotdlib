# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .storage_statistics_by_file_type import StorageStatisticsByFileType
from ..base_object import BaseObject


class StorageStatisticsByChat(BaseObject):
    """
    Contains the storage usage statistics for a specific chat
    
    :param chat_id: Chat identifier; 0 if none
    :type chat_id: :class:`int`
    
    :param size: Total size of the files in the chat, in bytes
    :type size: :class:`int`
    
    :param count: Total number of files in the chat
    :type count: :class:`int`
    
    :param by_file_type: Statistics split by file types
    :type by_file_type: :class:`list[StorageStatisticsByFileType]`
    
    """

    ID: str = Field("storageStatisticsByChat", alias="@type")
    chat_id: int
    size: int
    count: int
    by_file_type: list[StorageStatisticsByFileType]

    @staticmethod
    def read(q: dict) -> StorageStatisticsByChat:
        return StorageStatisticsByChat.construct(**q)
