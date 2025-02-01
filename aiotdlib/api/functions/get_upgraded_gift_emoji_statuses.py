# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUpgradedGiftEmojiStatuses(BaseObject):
    """
    Returns available upgraded gift emoji statuses for self status
    """

    ID: typing.Literal["getUpgradedGiftEmojiStatuses"] = Field(
        "getUpgradedGiftEmojiStatuses", validation_alias="@type", alias="@type"
    )
