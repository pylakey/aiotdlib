# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatFilter(BaseObject):
    """
    Returns information about a chat filter by its identifier
    
    Params:
        chat_filter_id (:class:`int`)
            Chat filter identifier
        
    """

    ID: str = Field("getChatFilter", alias="@type")
    chat_filter_id: int

    @staticmethod
    def read(q: dict) -> GetChatFilter:
        return GetChatFilter.construct(**q)
