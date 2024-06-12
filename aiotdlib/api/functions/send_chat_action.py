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
    ChatAction,
)


class SendChatAction(BaseObject):
    """
    Sends a notification about user activity in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request; for bots only
    :type business_connection_id: :class:`String`
    :param message_thread_id: If not 0, the message thread identifier in which the action was performed
    :type message_thread_id: :class:`Int53`
    :param action: The action description; pass null to cancel the currently active action, defaults to None
    :type action: :class:`ChatAction`, optional
    """

    ID: typing.Literal["sendChatAction"] = Field("sendChatAction", validation_alias="@type", alias="@type")
    chat_id: Int53
    business_connection_id: String
    message_thread_id: Int53 = 0
    action: typing.Optional[ChatAction] = None
