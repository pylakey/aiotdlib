# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetOwnedBots(BaseObject):
    """
    Returns the list of bots owned by the current user
    """

    ID: typing.Literal["getOwnedBots"] = Field("getOwnedBots", validation_alias="@type", alias="@type")
