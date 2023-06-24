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
    PremiumLimitType,
)


class GetPremiumLimit(BaseObject):
    """
    Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown

    :param limit_type: Type of the limit
    :type limit_type: :class:`PremiumLimitType`
    """

    ID: typing.Literal["getPremiumLimit"] = "getPremiumLimit"
    limit_type: PremiumLimitType
