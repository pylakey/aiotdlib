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
    AffiliateType,
)


class ConnectAffiliateProgram(BaseObject):
    """
    Connects an affiliate program to the given affiliate. Returns information about the connected affiliate program

    :param affiliate: The affiliate to which the affiliate program will be connected
    :type affiliate: :class:`AffiliateType`
    :param bot_user_id: Identifier of the bot, which affiliate program is connected
    :type bot_user_id: :class:`Int53`
    """

    ID: typing.Literal["connectAffiliateProgram"] = Field(
        "connectAffiliateProgram", validation_alias="@type", alias="@type"
    )
    affiliate: AffiliateType
    bot_user_id: Int53
