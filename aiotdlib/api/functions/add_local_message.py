# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent
from ..types import MessageSender


class AddLocalMessage(BaseObject):
    """
    Adds a local message to a chat. The message is persistent across application restarts only if the message database is used. Returns the added message
    
    Params:
        chat_id (:class:`int`)
            Target chat
        
        sender (:class:`MessageSender`)
            The sender sender of the message
        
        reply_to_message_id (:class:`int`)
            Identifier of the message to reply to or 0
        
        disable_notification (:class:`bool`)
            Pass true to disable notification for the message
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be added
        
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
