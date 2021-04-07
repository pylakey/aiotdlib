# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReorderChatFilters(BaseObject):
    """
    Changes the order of chat filters
    
    Params:
        chat_filter_ids (:obj:`list[int]`)
            Identifiers of chat filters in the new correct order
        
    """

    ID: str = Field("reorderChatFilters", alias="@type")
    chat_filter_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReorderChatFilters:
        return ReorderChatFilters.construct(**q)
