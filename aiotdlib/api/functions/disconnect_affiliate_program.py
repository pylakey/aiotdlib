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


class DisconnectAffiliateProgram(BaseObject):
    """
    Disconnects an affiliate program from the given affiliate and immediately deactivates its referral link. Returns updated information about the disconnected affiliate program

    :param affiliate: The affiliate to which the affiliate program is connected
    :type affiliate: :class:`AffiliateType`
    :param url: The referral link of the affiliate program
    :type url: :class:`String`
    """

    ID: typing.Literal["disconnectAffiliateProgram"] = Field(
        "disconnectAffiliateProgram", validation_alias="@type", alias="@type"
    )
    affiliate: AffiliateType
    url: String
