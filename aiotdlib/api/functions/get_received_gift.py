# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetReceivedGift(BaseObject):
    """
    Returns information about a received gift

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    """

    ID: typing.Literal["getReceivedGift"] = Field("getReceivedGift", validation_alias="@type", alias="@type")
    received_gift_id: String
