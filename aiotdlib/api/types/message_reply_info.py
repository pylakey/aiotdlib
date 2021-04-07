# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class MessageReplyInfo(BaseObject):
    """
    Contains information about replies to a message
    
    Params:
        reply_count (:class:`int`)
            Number of times the message was directly or indirectly replied
        
        recent_repliers (:obj:`list[MessageSender]`)
            Recent repliers to the message; available in channels with a discussion supergroup
        
        last_read_inbox_message_id (:class:`int`)
            Identifier of the last read incoming reply to the message
        
        last_read_outbox_message_id (:class:`int`)
            Identifier of the last read outgoing reply to the message
        
        last_message_id (:class:`int`)
            Identifier of the last reply to the message
        
    """

    ID: str = Field("messageReplyInfo", alias="@type")
    reply_count: int
    recent_repliers: list[MessageSender]
    last_read_inbox_message_id: int
    last_read_outbox_message_id: int
    last_message_id: int

    @staticmethod
    def read(q: dict) -> MessageReplyInfo:
        return MessageReplyInfo.construct(**q)
