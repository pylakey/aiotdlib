# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAvailableGifts(BaseObject):
    """
    Returns gifts that can be sent to other users and channel chats
    """

    ID: typing.Literal["getAvailableGifts"] = Field("getAvailableGifts", validation_alias="@type", alias="@type")
