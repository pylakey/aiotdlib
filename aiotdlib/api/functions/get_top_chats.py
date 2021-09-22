# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import TopChatCategory
from ..base_object import BaseObject


class GetTopChats(BaseObject):
    """
    Returns a list of frequently used chats. Supported only if the chat info database is enabled
    
    :param category: Category of chats to be returned
    :type category: :class:`TopChatCategory`
    
    :param limit: The maximum number of chats to be returned; up to 30
    :type limit: :class:`int`
    
    """

    ID: str = Field("getTopChats", alias="@type")
    category: TopChatCategory
    limit: int

    @staticmethod
    def read(q: dict) -> GetTopChats:
        return GetTopChats.construct(**q)
