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
    
    :param chat_filter_ids: Identifiers of chat filters in the new correct order
    :type chat_filter_ids: :class:`list[int]`
    
    :param main_chat_list_position: Position of the main chat list among chat filters, 0-based. Can be non-zero only for Premium users
    :type main_chat_list_position: :class:`int`
    
    """

    ID: str = Field("reorderChatFilters", alias="@type")
    chat_filter_ids: list[int]
    main_chat_list_position: int

    @staticmethod
    def read(q: dict) -> ReorderChatFilters:
        return ReorderChatFilters.construct(**q)
