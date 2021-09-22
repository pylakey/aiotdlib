# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputMessageContent
from ..types import MessageSender
from ..base_object import BaseObject


class AddLocalMessage(BaseObject):
    """
    Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
    
    :param chat_id: Target chat
    :type chat_id: :class:`int`
    
    :param sender: The sender sender of the message
    :type sender: :class:`MessageSender`
    
    :param reply_to_message_id: Identifier of the message to reply to or 0
    :type reply_to_message_id: :class:`int`
    
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`bool`
    
    :param input_message_content: The content of the message to be added
    :type input_message_content: :class:`InputMessageContent`
    
    """

    ID: str = Field("addLocalMessage", alias="@type")
    chat_id: int
    sender: MessageSender
    reply_to_message_id: int
    disable_notification: bool
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> AddLocalMessage:
        return AddLocalMessage.construct(**q)
