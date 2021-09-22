# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import SearchMessagesFilter
from ..base_object import BaseObject


class GetChatMessageCount(BaseObject):
    """
    Returns approximate number of messages of the specified type in the chat
    
    :param chat_id: Identifier of the chat in which to count messages
    :type chat_id: :class:`int`
    
    :param filter_: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    
    :param return_local: If true, returns count that is available locally without sending network requests, returning -1 if the number of messages is unknown
    :type return_local: :class:`bool`
    
    """

    ID: str = Field("getChatMessageCount", alias="@type")
    chat_id: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    return_local: bool

    @staticmethod
    def read(q: dict) -> GetChatMessageCount:
        return GetChatMessageCount.construct(**q)
