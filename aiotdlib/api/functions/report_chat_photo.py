# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatReportReason
from ..base_object import BaseObject


class ReportChatPhoto(BaseObject):
    """
    Reports a chat photo to the Telegram moderators. A chat photo can be reported only if this is a private chat with a bot, a private chat with a user sharing their location, a supergroup, or a channel, since other chats can't be checked by moderators
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param file_id: Identifier of the photo to report. Only full photos from chatPhoto can be reported
    :type file_id: :class:`int`
    
    :param reason: The reason for reporting the chat photo
    :type reason: :class:`ChatReportReason`
    
    :param text: Additional report details; 0-1024 characters, defaults to None
    :type text: :class:`str`, optional
    
    """

    ID: str = Field("reportChatPhoto", alias="@type")
    chat_id: int
    file_id: int
    reason: ChatReportReason
    text: typing.Optional[str] = Field(None, max_length=1024)

    @staticmethod
    def read(q: dict) -> ReportChatPhoto:
        return ReportChatPhoto.construct(**q)
