# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ReportReason,
)


class ReportChat(BaseObject):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param reason: The reason for reporting the chat
    :type reason: :class:`ReportReason`
    :param message_ids: Identifiers of reported messages; may be empty to report the whole chat
    :type message_ids: :class:`Vector[Int53]`
    :param text: Additional report details; 0-1024 characters
    :type text: :class:`String`
    """

    ID: typing.Literal["reportChat"] = "reportChat"
    chat_id: Int53
    reason: ReportReason
    message_ids: Vector[Int53] = []
    text: String = Field("", max_length=1024)
