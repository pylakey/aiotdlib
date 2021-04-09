# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .draft_message import DraftMessage
from .message import Message
from .message_reply_info import MessageReplyInfo
from ..base_object import BaseObject


class MessageThreadInfo(BaseObject):
    """
    Contains information about a message thread
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the message thread belongs
        
        message_thread_id (:class:`int`)
            Message thread identifier, unique within the chat
        
        reply_info (:class:`MessageReplyInfo`)
            Contains information about the message thread
        
        messages (:obj:`list[Message]`)
            The messages from which the thread starts. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
        
        draft_message (:class:`DraftMessage`)
            A draft of a message in the message thread; may be null
        
    """

    ID: str = Field("messageThreadInfo", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_info: MessageReplyInfo
    messages: list[Message]
    draft_message: typing.Optional[DraftMessage] = None

    @staticmethod
    def read(q: dict) -> MessageThreadInfo:
        return MessageThreadInfo.construct(**q)
