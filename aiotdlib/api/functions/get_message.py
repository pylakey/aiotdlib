# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessage(BaseObject):
    """
    Returns information about a message
    
    :param chat_id: Identifier of the chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message to get
    :type message_id: :class:`int`
    
    """

    ID: str = Field("getMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetMessage:
        return GetMessage.construct(**q)
