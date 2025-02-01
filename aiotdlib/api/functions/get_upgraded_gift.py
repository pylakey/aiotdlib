# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUpgradedGift(BaseObject):
    """
    Returns information about an upgraded gift by its name

    :param name: Unique name of the upgraded gift
    :type name: :class:`String`
    """

    ID: typing.Literal["getUpgradedGift"] = Field("getUpgradedGift", validation_alias="@type", alias="@type")
    name: String
