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


class GetConnectedAffiliatePrograms(BaseObject):
    """
    Returns affiliate programs that were connected to the given affiliate

    :param affiliate: The affiliate to which the affiliate program were connected
    :type affiliate: :class:`AffiliateType`
    :param offset: Offset of the first affiliate program to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of affiliate programs to return
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getConnectedAffiliatePrograms"] = Field(
        "getConnectedAffiliatePrograms", validation_alias="@type", alias="@type"
    )
    affiliate: AffiliateType
    offset: String
    limit: Int32
