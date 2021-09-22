# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatMessageByDate(BaseObject):
    """
    Returns the last message sent in a chat no later than the specified date
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) relative to which to search for messages
    :type date: :class:`int`
    
    """

    ID: str = Field("getChatMessageByDate", alias="@type")
    chat_id: int
    date: int

    @staticmethod
    def read(q: dict) -> GetChatMessageByDate:
        return GetChatMessageByDate.construct(**q)
