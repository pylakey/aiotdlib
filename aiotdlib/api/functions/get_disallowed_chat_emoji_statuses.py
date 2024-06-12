# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetDisallowedChatEmojiStatuses(BaseObject):
    """
    Returns the list of emoji statuses, which can't be used as chat emoji status, even they are from a sticker set with is_allowed_as_chat_emoji_status == true
    """

    ID: typing.Literal["getDisallowedChatEmojiStatuses"] = Field(
        "getDisallowedChatEmojiStatuses", validation_alias="@type", alias="@type"
    )
