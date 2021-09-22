# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatFilter
from ..base_object import BaseObject


class EditChatFilter(BaseObject):
    """
    Edits existing chat filter. Returns information about the edited chat filter
    
    :param chat_filter_id: Chat filter identifier
    :type chat_filter_id: :class:`int`
    
    :param filter_: The edited chat filter
    :type filter_: :class:`ChatFilter`
    
    """

    ID: str = Field("editChatFilter", alias="@type")
    chat_filter_id: int
    filter_: ChatFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> EditChatFilter:
        return EditChatFilter.construct(**q)
