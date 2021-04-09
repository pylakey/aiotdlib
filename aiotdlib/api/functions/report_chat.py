# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatReportReason


class ReportChat(BaseObject):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if this is a private chat with a bot, a private chat with a user sharing their location, a supergroup, or a channel, since other chats can't be checked by moderators
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_ids (:obj:`list[int]`)
            Identifiers of reported messages, if any
        
        reason (:class:`ChatReportReason`)
            The reason for reporting the chat
        
        text (:class:`str`)
            Additional report details; 0-1024 characters
        
    """

    ID: str = Field("reportChat", alias="@type")
    chat_id: int
    message_ids: list[int]
    reason: ChatReportReason
    text: typing.Optional[str] = Field(None, max_length=1024)

    @staticmethod
    def read(q: dict) -> ReportChat:
        return ReportChat.construct(**q)
