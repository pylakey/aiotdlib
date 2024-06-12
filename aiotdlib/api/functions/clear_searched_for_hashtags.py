# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ClearSearchedForHashtags(BaseObject):
    """
    Clears the list of recently searched for hashtags
    """

    ID: typing.Literal["clearSearchedForHashtags"] = Field(
        "clearSearchedForHashtags", validation_alias="@type", alias="@type"
    )
