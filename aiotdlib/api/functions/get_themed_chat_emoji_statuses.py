# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetThemedChatEmojiStatuses(BaseObject):
    """
    Returns up to 8 emoji statuses, which must be shown in the emoji status list for chats
    """

    ID: typing.Literal["getThemedChatEmojiStatuses"] = Field(
        "getThemedChatEmojiStatuses", validation_alias="@type", alias="@type"
    )
