# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetStorageStatistics(BaseObject):
    """
    Returns storage usage statistics. Can be called before authorization
    
    Params:
        chat_limit (:class:`int`)
            The maximum number of chats with the largest storage usage for which separate statistics should be returned. All other chats will be grouped in entries with chat_id == 0. If the chat info database is not used, the chat_limit is ignored and is always set to 0
        
    """

    ID: str = Field("getStorageStatistics", alias="@type")
    chat_limit: int

    @staticmethod
    def read(q: dict) -> GetStorageStatistics:
        return GetStorageStatistics.construct(**q)
