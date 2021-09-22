# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessagePublicForwards(BaseObject):
    """
    Returns forwarded copies of a channel message to different public channels. For optimal performance, the number of returned messages is chosen by TDLib
    
    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
    :type offset: :class:`str`
    
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    """

    ID: str = Field("getMessagePublicForwards", alias="@type")
    chat_id: int
    message_id: int
    offset: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetMessagePublicForwards:
        return GetMessagePublicForwards.construct(**q)
