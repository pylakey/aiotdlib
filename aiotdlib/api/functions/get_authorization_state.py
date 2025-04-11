# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAuthorizationState(BaseObject):
    """
    Returns the current authorization state. This is an offline method. For informational purposes only. Use updateAuthorizationState instead to maintain the current authorization state. Can be called before initialization
    """

    ID: typing.Literal["getAuthorizationState"] = Field(
        "getAuthorizationState", validation_alias="@type", alias="@type"
    )
