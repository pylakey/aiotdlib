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
    
    :param chat_id: Identifier of the chat to which the message thread belongs
    :type chat_id: :class:`int`
    
    :param message_thread_id: Message thread identifier, unique within the chat
    :type message_thread_id: :class:`int`
    
    :param reply_info: Contains information about the message thread
    :type reply_info: :class:`MessageReplyInfo`
    
    :param unread_message_count: Approximate number of unread messages in the message thread
    :type unread_message_count: :class:`int`
    
    :param messages: The messages from which the thread starts. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
    :type messages: :class:`list[Message]`
    
    :param draft_message: A draft of a message in the message thread; may be null, defaults to None
    :type draft_message: :class:`DraftMessage`, optional
    
    """

    ID: str = Field("messageThreadInfo", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_info: MessageReplyInfo
    unread_message_count: int
    messages: list[Message]
    draft_message: typing.Optional[DraftMessage] = None

    @staticmethod
    def read(q: dict) -> MessageThreadInfo:
        return MessageThreadInfo.construct(**q)
