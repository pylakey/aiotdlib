# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import PremiumLimitType


class GetPremiumLimit(BaseObject):
    """
    Returns information about a limit, increased for Premium users. Returns a 404 error if the limit is unknown
    
    :param limit_type: Type of the limit
    :type limit_type: :class:`PremiumLimitType`
    
    """

    ID: str = Field("getPremiumLimit", alias="@type")
    limit_type: PremiumLimitType

    @staticmethod
    def read(q: dict) -> GetPremiumLimit:
        return GetPremiumLimit.construct(**q)
