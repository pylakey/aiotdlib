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
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_ids: Identifiers of reported messages; may be empty to report the whole chat
    :type message_ids: :class:`list[int]`
    
    :param reason: The reason for reporting the chat
    :type reason: :class:`ChatReportReason`
    
    :param text: Additional report details; 0-1024 characters, defaults to None
    :type text: :class:`str`, optional
    
    """

    ID: str = Field("reportChat", alias="@type")
    chat_id: int
    message_ids: list[int]
    reason: ChatReportReason
    text: typing.Optional[str] = Field(None, max_length=1024)

    @staticmethod
    def read(q: dict) -> ReportChat:
        return ReportChat.construct(**q)
