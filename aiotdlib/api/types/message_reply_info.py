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
    
    :param reply_count: Number of times the message was directly or indirectly replied
    :type reply_count: :class:`int`
    
    :param recent_replier_ids: Identifiers of at most 3 recent repliers to the message; available in channels with a discussion supergroup. The users and chats are expected to be inaccessible: only their photo and name will be available
    :type recent_replier_ids: :class:`list[MessageSender]`
    
    :param last_read_inbox_message_id: Identifier of the last read incoming reply to the message
    :type last_read_inbox_message_id: :class:`int`
    
    :param last_read_outbox_message_id: Identifier of the last read outgoing reply to the message
    :type last_read_outbox_message_id: :class:`int`
    
    :param last_message_id: Identifier of the last reply to the message
    :type last_message_id: :class:`int`
    
    """

    ID: str = Field("messageReplyInfo", alias="@type")
    reply_count: int
    recent_replier_ids: list[MessageSender]
    last_read_inbox_message_id: int
    last_read_outbox_message_id: int
    last_message_id: int

    @staticmethod
    def read(q: dict) -> MessageReplyInfo:
        return MessageReplyInfo.construct(**q)
