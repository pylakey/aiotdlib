# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DeleteChatFilter(BaseObject):
    """
    Deletes existing chat filter
    
    Params:
        chat_filter_id (:class:`int`)
            Chat filter identifier
        
    """

    ID: str = Field("deleteChatFilter", alias="@type")
    chat_filter_id: int

    @staticmethod
    def read(q: dict) -> DeleteChatFilter:
        return DeleteChatFilter.construct(**q)
