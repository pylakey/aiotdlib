# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetGiftUpgradePreview(BaseObject):
    """
    Returns examples of possible upgraded gifts for a regular gift

    :param gift_id: Identifier of the gift
    :type gift_id: :class:`Int64`
    """

    ID: typing.Literal["getGiftUpgradePreview"] = Field(
        "getGiftUpgradePreview", validation_alias="@type", alias="@type"
    )
    gift_id: Int64
