# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .storage_statistics_by_chat import StorageStatisticsByChat
from ..base_object import BaseObject


class StorageStatistics(BaseObject):
    """
    Contains the exact storage usage statistics split by chats and file type
    
    :param size: Total size of files, in bytes
    :type size: :class:`int`
    
    :param count: Total number of files
    :type count: :class:`int`
    
    :param by_chat: Statistics split by chats
    :type by_chat: :class:`list[StorageStatisticsByChat]`
    
    """

    ID: str = Field("storageStatistics", alias="@type")
    size: int
    count: int
    by_chat: list[StorageStatisticsByChat]

    @staticmethod
    def read(q: dict) -> StorageStatistics:
        return StorageStatistics.construct(**q)
