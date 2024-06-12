# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetGreetingStickers(BaseObject):
    """
    Returns greeting stickers from regular sticker sets that can be used for the start page of other users
    """

    ID: typing.Literal["getGreetingStickers"] = Field("getGreetingStickers", validation_alias="@type", alias="@type")
