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
    PremiumSource,
)


class GetPremiumFeatures(BaseObject):
    """
    Returns information about features, available to Premium users

    :param source: Source of the request; pass null if the method is called from some non-standard source, defaults to None
    :type source: :class:`PremiumSource`, optional
    """

    ID: typing.Literal["getPremiumFeatures"] = "getPremiumFeatures"
    source: typing.Optional[PremiumSource] = None
