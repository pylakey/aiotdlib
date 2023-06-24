# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendChatScreenshotTakenNotification(BaseObject):
    """
    Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["sendChatScreenshotTakenNotification"] = "sendChatScreenshotTakenNotification"
    chat_id: Int53
