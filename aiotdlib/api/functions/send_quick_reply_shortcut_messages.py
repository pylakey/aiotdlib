# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SendQuickReplyShortcutMessages(BaseObject):
    """
    Sends messages from a quick reply shortcut. Requires Telegram Business subscription. Can't be used to send paid messages

    :param chat_id: Identifier of the chat to which to send messages. The chat must be a private chat with a regular user
    :type chat_id: :class:`Int53`
    :param shortcut_id: Unique identifier of the quick reply shortcut
    :type shortcut_id: :class:`Int32`
    :param sending_id: Non-persistent identifier, which will be returned back in messageSendingStatePending object and can be used to match sent messages and corresponding updateNewMessage updates
    :type sending_id: :class:`Int32`
    """

    ID: typing.Literal["sendQuickReplyShortcutMessages"] = Field(
        "sendQuickReplyShortcutMessages", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    shortcut_id: Int32
    sending_id: Int32
