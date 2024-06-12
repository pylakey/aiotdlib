# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecommendedChats(BaseObject):
    """
    Returns a list of channel chats recommended to the current user
    """

    ID: typing.Literal["getRecommendedChats"] = Field("getRecommendedChats", validation_alias="@type", alias="@type")
