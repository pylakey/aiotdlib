# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPaidMessageRevenue(BaseObject):
    """
    Returns the total number of Telegram Stars received by the current user for paid messages from the given user

    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getPaidMessageRevenue"] = Field(
        "getPaidMessageRevenue", validation_alias="@type", alias="@type"
    )
    user_id: Int53
