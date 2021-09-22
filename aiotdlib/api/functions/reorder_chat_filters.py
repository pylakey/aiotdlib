# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ReorderChatFilters(BaseObject):
    """
    Changes the order of chat filters
    
    :param chat_filter_ids: Identifiers of chat filters in the new correct order
    :type chat_filter_ids: :class:`list[int]`
    
    """

    ID: str = Field("reorderChatFilters", alias="@type")
    chat_filter_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReorderChatFilters:
        return ReorderChatFilters.construct(**q)
