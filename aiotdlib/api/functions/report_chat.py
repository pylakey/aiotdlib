# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReportChat(BaseObject):
    """
    Reports a chat to the Telegram moderators. A chat can be reported only from the chat action bar, or if chat.can_be_reported

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param option_id: Option identifier chosen by the user; leave empty for the initial request
    :type option_id: :class:`Bytes`
    :param message_ids: Identifiers of reported messages. Use messageProperties.can_report_chat to check whether the message can be reported
    :type message_ids: :class:`Vector[Int53]`
    :param text: Additional report details if asked by the server; 0-1024 characters; leave empty for the initial request
    :type text: :class:`String`
    """

    ID: typing.Literal["reportChat"] = Field("reportChat", validation_alias="@type", alias="@type")
    chat_id: Int53
    option_id: Bytes
    message_ids: Vector[Int53]
    text: String = Field("", max_length=1024)
