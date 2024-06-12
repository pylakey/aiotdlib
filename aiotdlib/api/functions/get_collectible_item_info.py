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
    CollectibleItemType,
)


class GetCollectibleItemInfo(BaseObject):
    """
    Returns information about a given collectible item that was purchased at https://fragment.com

    :param type_: Type of the collectible item. The item must be used by a user and must be visible to the current user
    :type type_: :class:`CollectibleItemType`
    """

    ID: typing.Literal["getCollectibleItemInfo"] = Field(
        "getCollectibleItemInfo", validation_alias="@type", alias="@type"
    )
    type_: CollectibleItemType = Field(..., alias="type")
