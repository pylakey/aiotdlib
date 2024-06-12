# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class HideContactCloseBirthdays(BaseObject):
    """
    Hides the list of contacts that have close birthdays for 24 hours
    """

    ID: typing.Literal["hideContactCloseBirthdays"] = Field(
        "hideContactCloseBirthdays", validation_alias="@type", alias="@type"
    )
