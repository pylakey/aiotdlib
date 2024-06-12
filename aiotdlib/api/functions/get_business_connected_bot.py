# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetBusinessConnectedBot(BaseObject):
    """
    Returns the business bot that is connected to the current user account. Returns a 404 error if there is no connected bot
    """

    ID: typing.Literal["getBusinessConnectedBot"] = Field(
        "getBusinessConnectedBot", validation_alias="@type", alias="@type"
    )
