# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageViewers(BaseObject):
    """
    Returns viewers of a recent outgoing message in a basic group or a supergroup chat. For video notes and voice notes only users, opened content of the message, are returned. The method can be called if message.can_get_viewers == true
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    """

    ID: str = Field("getMessageViewers", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetMessageViewers:
        return GetMessageViewers.construct(**q)
