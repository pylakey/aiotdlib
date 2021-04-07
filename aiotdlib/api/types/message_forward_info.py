# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_forward_origin import MessageForwardOrigin
from ..base_object import BaseObject


class MessageForwardInfo(BaseObject):
    """
    Contains information about a forwarded message
    
    Params:
        origin (:class:`MessageForwardOrigin`)
            Origin of a forwarded message
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the message was originally sent
        
        public_service_announcement_type (:class:`str`)
            The type of a public service announcement for the forwarded message
        
        from_chat_id (:class:`int`)
            For messages forwarded to the chat with the current user (Saved Messages), to the Replies bot chat, or to the channel's discussion group, the identifier of the chat from which the message was forwarded last time; 0 if unknown
        
        from_message_id (:class:`int`)
            For messages forwarded to the chat with the current user (Saved Messages), to the Replies bot chat, or to the channel's discussion group, the identifier of the original message from which the new message was forwarded last time; 0 if unknown
        
    """

    ID: str = Field("messageForwardInfo", alias="@type")
    origin: MessageForwardOrigin
    date: int
    public_service_announcement_type: str
    from_chat_id: int
    from_message_id: int

    @staticmethod
    def read(q: dict) -> MessageForwardInfo:
        return MessageForwardInfo.construct(**q)
