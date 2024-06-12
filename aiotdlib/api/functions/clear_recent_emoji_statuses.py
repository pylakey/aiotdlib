# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearRecentEmojiStatuses(BaseObject):
    """
    Clears the list of recently used emoji statuses for self status
    """

    ID: typing.Literal["clearRecentEmojiStatuses"] = Field(
        "clearRecentEmojiStatuses", validation_alias="@type", alias="@type"
    )
