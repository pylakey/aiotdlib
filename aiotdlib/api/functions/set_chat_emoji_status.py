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
    EmojiStatus,
)


class SetChatEmojiStatus(BaseObject):
    """
    Changes the emoji status of a chat. Use chatBoostLevelFeatures.can_set_emoji_status to check whether an emoji status can be set. Requires can_change_info administrator right

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param emoji_status: New emoji status; pass null to remove emoji status, defaults to None
    :type emoji_status: :class:`EmojiStatus`, optional
    """

    ID: typing.Literal["setChatEmojiStatus"] = Field("setChatEmojiStatus", validation_alias="@type", alias="@type")
    chat_id: Int53
    emoji_status: typing.Optional[EmojiStatus] = None
