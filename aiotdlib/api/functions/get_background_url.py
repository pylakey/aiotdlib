# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    BackgroundType,
)


class GetBackgroundUrl(BaseObject):
    """
    Constructs a persistent HTTP URL for a background

    :param name: Background name
    :type name: :class:`String`
    :param type_: Background type
    :type type_: :class:`BackgroundType`
    """

    ID: typing.Literal["getBackgroundUrl"] = "getBackgroundUrl"
    name: String
    type_: BackgroundType = Field(..., alias="type")
