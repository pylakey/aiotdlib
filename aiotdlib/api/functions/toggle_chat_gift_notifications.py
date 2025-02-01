# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleChatGiftNotifications(BaseObject):
    """
    Toggles whether notifications for new gifts received by a channel chat are sent to the current user; requires can_post_messages administrator right in the chat

    :param chat_id: Identifier of the channel chat
    :type chat_id: :class:`Int53`
    :param are_enabled: Pass true to enable notifications about new gifts owned by the channel chat; pass false to disable the notifications
    :type are_enabled: :class:`Bool`
    """

    ID: typing.Literal["toggleChatGiftNotifications"] = Field(
        "toggleChatGiftNotifications", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    are_enabled: Bool = False
