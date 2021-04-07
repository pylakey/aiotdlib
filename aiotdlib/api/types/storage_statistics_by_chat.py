# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .storage_statistics_by_file_type import StorageStatisticsByFileType
from ..base_object import BaseObject


class StorageStatisticsByChat(BaseObject):
    """
    Contains the storage usage statistics for a specific chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier; 0 if none
        
        size (:class:`int`)
            Total size of the files in the chat
        
        count (:class:`int`)
            Total number of files in the chat
        
        by_file_type (:obj:`list[StorageStatisticsByFileType]`)
            Statistics split by file types
        
    """

    ID: str = Field("storageStatisticsByChat", alias="@type")
    chat_id: int
    size: int
    count: int
    by_file_type: list[StorageStatisticsByFileType]

    @staticmethod
    def read(q: dict) -> StorageStatisticsByChat:
        return StorageStatisticsByChat.construct(**q)
