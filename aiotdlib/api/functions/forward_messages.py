# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSendOptions


class ForwardMessages(BaseObject):
    """
    Forwards previously sent messages. Returns the forwarded messages in the same order as the message identifiers passed in message_ids. If a message can't be forwarded, null will be returned instead of the message
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which to forward messages
        
        from_chat_id (:class:`int`)
            Identifier of the chat from which to forward messages
        
        message_ids (:obj:`list[int]`)
            Identifiers of the messages to forward. Message identifiers must be in a strictly increasing order. At most 100 messages can be forwarded simultaneously
        
        options (:class:`MessageSendOptions`)
            Options to be used to send the messages
        
        send_copy (:class:`bool`)
            True, if content of the messages needs to be copied without links to the original messages. Always true if the messages are forwarded to a secret chat
        
        remove_caption (:class:`bool`)
            True, if media caption of message copies needs to be removed. Ignored if send_copy is false
        
    """

    ID: str = Field("forwardMessages", alias="@type")
    chat_id: int
    from_chat_id: int
    message_ids: list[int]
    options: MessageSendOptions
    send_copy: bool
    remove_caption: bool

    @staticmethod
    def read(q: dict) -> ForwardMessages:
        return ForwardMessages.construct(**q)
