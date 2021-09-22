# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class MessageSender(BaseObject):
    """
    Contains information about the sender of a message
    
    """

    ID: str = Field("messageSender", alias="@type")


class MessageSenderChat(MessageSender):
    """
    The message was sent on behalf of a chat
    
    :param chat_id: Identifier of the chat that sent the message
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("messageSenderChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> MessageSenderChat:
        return MessageSenderChat.construct(**q)


class MessageSenderUser(MessageSender):
    """
    The message was sent by a known user
    
    :param user_id: Identifier of the user that sent the message
    :type user_id: :class:`int`
    
    """

    ID: str = Field("messageSenderUser", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> MessageSenderUser:
        return MessageSenderUser.construct(**q)
