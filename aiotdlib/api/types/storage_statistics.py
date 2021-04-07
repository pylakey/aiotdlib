# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .storage_statistics_by_chat import StorageStatisticsByChat
from ..base_object import BaseObject


class StorageStatistics(BaseObject):
    """
    Contains the exact storage usage statistics split by chats and file type
    
    Params:
        size (:class:`int`)
            Total size of files
        
        count (:class:`int`)
            Total number of files
        
        by_chat (:obj:`list[StorageStatisticsByChat]`)
            Statistics split by chats
        
    """

    ID: str = Field("storageStatistics", alias="@type")
    size: int
    count: int
    by_chat: list[StorageStatisticsByChat]

    @staticmethod
    def read(q: dict) -> StorageStatistics:
        return StorageStatistics.construct(**q)
