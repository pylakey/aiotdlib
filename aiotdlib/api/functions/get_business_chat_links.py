# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBusinessChatLinks(BaseObject):
    """
    Returns business chat links created for the current account
    """

    ID: typing.Literal["getBusinessChatLinks"] = Field("getBusinessChatLinks", validation_alias="@type", alias="@type")
