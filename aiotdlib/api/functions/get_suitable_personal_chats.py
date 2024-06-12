# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSuitablePersonalChats(BaseObject):
    """
    Returns a list of channel chats, which can be used as a personal chat
    """

    ID: typing.Literal["getSuitablePersonalChats"] = Field(
        "getSuitablePersonalChats", validation_alias="@type", alias="@type"
    )
